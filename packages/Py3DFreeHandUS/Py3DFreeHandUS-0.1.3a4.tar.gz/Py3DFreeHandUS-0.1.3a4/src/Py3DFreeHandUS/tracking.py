# -*- coding: utf-8 -*-
"""
.. module:: tracking
   :synopsis: module for features tracking (e.g. muscle-tendon junction)

"""

import guidata
from guidata.dataset.datatypes import DataSet, BeginGroup, EndGroup, ValueProp
from guidata.dataset.dataitems import ButtonItem, FloatItem, IntItem, BoolItem, ChoiceItem, FileSaveItem, FileOpenItem, DirectoryItem
import tempfile, atexit, shutil
from image_utils import *
from converters import *
from particle_filter import ParticleFilter
import numpy as np
import cv2
import SimpleITK as sitk
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import Normalize, LogNorm
from scipy import signal
from skimage import feature
                                     



def showImageQualityStatsPreOF(I, show=True):
    """Creates quality indices for before optical flow computation.
    
    .. note::
    
        These considerations are important: 
        
        - Better to use a greyscale images, so that the eye does not focus on the 
          type of color but only on the value;
          
        - For Shi-Tomasi corner response, better to use a logarithmic scale to 
          smooth the left/right border effect (high values). Moreover, some image 
          types (e.g. US) might have artificial symbols on it, bringing intrinsic
          high corner response;
          
        - For the sake of function generality, min and max for each image are not 
          normalized to fixed values, since these may depend on the input type.
    
    Parameters
    ----------
    I : np.ndarray
        2D grey-scale image.
    
    show : bool
        Plot results window or not.      
        
    """

    
    # Plot original image
    plt.subplot(2, 2, 1)
    plt.imshow(I, cmap=plt.cm.gray)
    plt.grid()
    plt.colorbar()
    plt.title('Original')
    
#    # Compute Harris corner measure response image.
#    Ihar = feature.corner_harris(I, method='k', k=0.05, eps=1e-06, sigma=3)
#    plt.subplot(2, 2, 2)
#    #plt.imshow(Ihar, cmap=plt.cm.gray, norm=LogNorm())
#    plt.imshow(Ihar, cmap=plt.cm.gray)
#    plt.grid()
#    plt.colorbar()
#    plt.title('Harris response')
    
    # Compute Shi-Tomasi (Kanade-Tomasi) corner measure response image.
    Isht = feature.corner_shi_tomasi(I, sigma=3)
    plt.subplot(2, 2, 3)
    plt.imshow(Isht, cmap=plt.cm.gray, norm=LogNorm())
    #plt.imshow(Isht, cmap=plt.cm.gray)
    plt.grid()
    plt.colorbar()
    plt.title('Shi-Tomasi response')
    
    # Compute Marquez-Valle condition number.
    Axx, Axy, Ayy = feature.structure_tensor(I, sigma=3)
    l1, l2 = feature.structure_tensor_eigvals(Axx, Axy, Ayy)
    Icon = l1 / l2
    plt.subplot(2, 2, 4)
    plt.imshow(Icon, cmap=plt.cm.gray)
    plt.grid()
    plt.colorbar()
    plt.title('Condition number')
    
    # Show plots
    if show:
        plt.show(True)
    
    
    

    
def enhanceMTJForTracking(img, method, enhanceArgs, enhanceKwargs):
    """Function for enhancing the image containing muscle-tendon junction (MTJ)
    for tracking purpose. Two characteristics can be enhanced: 
    
    - contrast (by histogram equalization)
    
    - signal-to-noise ratio (by smoothing)
    
    Parameters
    ----------
    img : np.ndarray
        Image to be enhanced.

    method : str
        Method for enhancing the image:
        
        - 'histeq': histogram equalization.
        
        - 'clahe': Contrast-Limited Adaptive Histogram Equalization
          (see ``cv2.createCLAHE()``). It uses ``enhanceKwargs``.
        
        - 'smooth': smoothing with Gaussian kernel
          (see ``cv2.GaussianBlur()``). It uses ``enhanceArgs``.
        
        There are other methods, where '_opt' is happended, that do not need
        further (further) arguments. Here, we are experimenting optimal settings.
        
    enhanceArgs : tuple
        List of arguments that can be needed by the enhancing functions.
        
    enhanceKwargs : dict
        List of keyword arguments that can be needed by the enhancing functions.

    Returns
    -------
    np.ndarray
        Enhance image.
    
    """
    if method == 'histeq':
        img2 = cv2.equalizeHist(img)
    elif method == 'clahe':
        clahe = cv2.createCLAHE(**enhanceKwargs)
        img2 = clahe.apply(img)
    elif method == 'clahe_opt':
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img2 = clahe.apply(img)
    elif method == 'smooth':
        img2 = cv2.GaussianBlur(img, *enhanceArgs)
    elif method == 'smooth_opt':
        img2 = cv2.GaussianBlur(img,(7,7),0)
    return img2
    

    
def calcVelocityLee2008(allDx, allDy, pctEx, pctIn, direction='max_avg_vel'):
    """Implements the method described in the article of Lee et al 2008
    for calculating the muscle-tendon junction (MTJ) velocity vector (u, v) 
    between a frame and the next one.
    
    Parameters
    ----------
    allDx, allDy : np.ndarray
        X and Y component for velocities from for pixel in the rectangle mask.

    pctEx : float
        Number (between 0 and 1) indicating the percentage of velocities, in the
        beginning and end of sorted lists, to exclude. In the original article,
        this value was 0.1.
        
    pctIn : float
        Number (between 0 and 1) indicating the percentage of velocities, in the
        beginning and end of remaining sorted lists, to use for the average. 
        In the original article, this value was 0.05.
        
    direction : string
        It defines which of the 2 average velocities (beginning and end of list)
        to use as final velocity.
        If 'max_avg_vel', the choice is determined by the absolute magnitude of 
        the average velocity (as in the original article by Lee).
        If 'pct_sign', the choice is determined by the dominant number of 
        velocitied concording in sign. If there is an equal number of positive
        and negative velocities, then the algorithm proceeds as for 'max_avg_vel'.

    Returns
    -------
    tuple
        Velocity vector (u, v) for the MTJ.
    
    """
    
    mask_u = np.empty_like(allDx)
    mask_u[:] = 2
    mask_v = np.empty_like(allDy)
    mask_v[:] = 2
    all_u = np.sort(allDx)
    all_v = np.sort(allDy)
    idx_u_ = np.argsort(allDx)
    idx_v_ = np.argsort(allDy)
    Np = all_u.shape[0] / 55. * 100.
    if int(Np*pctEx) > 0:
        all_u = all_u[int(Np*pctEx):int(-Np*pctEx)]
        idx_u = idx_u_[int(Np*pctEx):int(-Np*pctEx)]
        mask_u[idx_u] = 0
        all_v = all_v[int(Np*pctEx):int(-Np*pctEx)]
        idx_v = idx_v_[int(Np*pctEx):int(-Np*pctEx)]
        mask_v[idx_v] = 0
    u_avg_1 = all_u[:int(Np*pctIn)].mean()
    v_avg_1 = all_v[:int(Np*pctIn)].mean()
    u_avg_2 = all_u[int(-Np*pctIn):].mean()
    v_avg_2 = all_v[int(-Np*pctIn):].mean()
    if direction == 'max_avg_vel':
        if np.abs(u_avg_1) > np.abs(u_avg_2):
            u = u_avg_1
            mask_u[idx_u[:int(Np*pctIn)]] = 1
            mask_u[idx_u_[:int(Np*pctEx)]] = 3
        else:
            u = u_avg_2
            mask_u[idx_u[int(-Np*pctIn):]] = 1
            mask_u[idx_u_[int(-Np*pctEx):]] = 3
        if np.abs(v_avg_1) > np.abs(v_avg_2):
            v = v_avg_1
            mask_v[idx_v[:int(Np*pctIn)]] = 1
            mask_v[idx_v_[:int(Np*pctEx)]] = 3
        else:
            v = v_avg_2
            mask_v[idx_v[int(-Np*pctIn):]] = 1
            mask_v[idx_v_[int(-Np*pctEx):]] = 3
    elif direction == 'pct_sign':
        direction_u = np.sign(all_u).sum()
        direction_v = np.sign(all_v).sum()
        if direction_u < 0:
            u = u_avg_1
            mask_u[idx_u[:int(Np*pctIn)]] = 1
            mask_u[idx_u_[:int(Np*pctEx)]] = 3
        elif direction_u > 0:
            u = u_avg_2
            mask_u[idx_u[int(-Np*pctIn):]] = 1
            mask_u[idx_u_[int(-Np*pctEx):]] = 3
        else:
            if np.abs(u_avg_1) > np.abs(u_avg_2):
                u = u_avg_1
                mask_u[idx_u[:int(Np*pctIn)]] = 1
                mask_u[idx_u_[:int(Np*pctEx)]] = 3
            else:
                u = u_avg_2
                mask_u[idx_u[int(-Np*pctIn):]] = 1
                mask_u[idx_u_[int(-Np*pctEx):]] = 3
        if direction_v < 0:
            v = v_avg_1
            mask_v[idx_v[:int(Np*pctIn)]] = 1
            mask_u[idx_u_[:int(Np*pctEx)]] = 3
        elif direction_v > 0:
            v = v_avg_2
            mask_v[idx_v[int(-Np*pctIn):]] = 1
            mask_v[idx_v_[int(-Np*pctEx):]] = 3
        else:
            if np.abs(v_avg_1) > np.abs(v_avg_2):
                v = v_avg_1
                mask_v[idx_v[:int(Np*pctIn)]] = 1
                mask_v[idx_v_[:int(Np*pctEx)]] = 3
            else:
                v = v_avg_2
                mask_v[idx_v[int(-Np*pctIn):]] = 1
                mask_v[idx_v_[int(-Np*pctEx):]] = 3
            
    return u, v, mask_u, mask_v
    
    

def trackMTJ_gui():
    """Opens a GUI to set most of the important options for MTJ tracking.

    Returns
    -------
    dcmFile : str
        File path of the input DICOM file.
        
    p : dict
        Dictionary of optional arguments to be give to ``trackMTJ()``.
        
    resFile : str
        File path of the output .res file.
    
    """
    
    TEMPDIR = tempfile.mkdtemp(prefix="test_")
    atexit.register(shutil.rmtree, TEMPDIR)
    FILE_DCM = tempfile.NamedTemporaryFile(suffix=".dcm", dir=TEMPDIR)
    atexit.register(FILE_DCM.close)
    FILE_AVI = tempfile.NamedTemporaryFile(suffix=".avi", dir=TEMPDIR)
    atexit.register(FILE_AVI.close)
    FILE_RES = tempfile.NamedTemporaryFile(suffix=".res", dir=TEMPDIR)
    atexit.register(FILE_RES.close)
    
    canManuallyAdjust = ValueProp(False)
    canSaveTechniqueResTo = ValueProp(False)
    
    class TrackParameters(DataSet):
        
        def openFile(instance, item, value):
            try:
                I, metadata = readImage(str(value), reader='sitk')
                instance.I = I
                TrackParameters.f2.set_prop("data", max=I.shape[0])
                instance.f1 = 0
                instance.f2 = I.shape[0] - 1
                TrackParameters.x2.set_prop("data", max=I.shape[2])
                instance.x1 = 0
                instance.x2 = I.shape[2] - 1
                TrackParameters.y2.set_prop("data", max=I.shape[1])
                instance.y1 = 0
                instance.y2 = I.shape[1] - 1
            except e:
                print('Error reading DCM file')
            
        def getCenter(dataset, item, value, parent):
            w, h = dataset.w, dataset.h
            f1 = dataset.f1
            x1, x2 = dataset.x1, dataset.x2
            y1, y2 = dataset.y1, dataset.y2
            frame = dataset.I[f1,y1:y2,x1:x2]
            global _cx, _cy
            cx, cy = dataset.cx, dataset.cy
            _cx, _cy = cx, cy
            def onmouseRect(event, x, y, flags, param):
                global _cx,_cy,p0
                if flags & cv2.EVENT_FLAG_LBUTTON:
                    _cx, _cy = int(x), int(y)
                    p0 = createCenteredMaskCoords(_cx, _cy, h, w)[:,None,:]
                    pts = p0[:,0,:]
                    a, b = pts[:,0].min(), pts[:,1].min()
                    c, d = pts[:,0].max(), pts[:,1].max()
                    area_col = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                    area_col2 = cv2.rectangle(area_col, (a,b),(c,d), (0,0,255), 1)
                    if area_col2 is not None:
                        area_col = area_col2
                    cv2.imshow(win, area_col)        
            win = 'Click on window center'
            cv2.imshow(win, frame)
            global p0  
            p0 = None
            cv2.setMouseCallback(win, onmouseRect)
            if cx is None or cy is None:
                cx, cy = w/2, h/2
            onmouseRect(None, cx, cy, True, None)   # to show rectangle on prompt
            cv2.waitKey()
            cv2.destroyAllWindows()
            cx, cy = _cx, _cy
            dataset.cx, dataset.cy = cx, cy
            
        
        def getOffset(dataset, item, value, parent):
            f1 = dataset.f1
            x1, x2 = dataset.x1, dataset.x2
            y1, y2 = dataset.y1, dataset.y2
            frame = dataset.I[f1,y1:y2,x1:x2]
            global _cxo, _cyo
            cx, cy = dataset.cx, dataset.cy
            cxOffset, cyOffset = dataset.cxOffset, dataset.cyOffset
            _cxo, _cyo = cxOffset + cx, cyOffset + cy
            def onmouseOffset(event, x, y, flags, param):
                global _cxo,_cyo
                if flags & cv2.EVENT_FLAG_LBUTTON:
                    _cxo, _cyo = int(x), int(y)
                    area_col = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                    area_col2 = cv2.circle(area_col,(int(_cxo),int(_cyo)),5,(0,0,255),1)
                    if area_col2 is not None:
                        area_col = area_col2
                    cv2.imshow(win, area_col)        
            win = 'Click on offset point'
            cv2.imshow(win, frame)
            cv2.setMouseCallback(win, onmouseOffset)
            onmouseOffset(None, _cxo, _cyo, True, None)   # to show point on prompt
            cv2.waitKey()
            cv2.destroyAllWindows()
            cxOffset, cyOffset = _cxo-cx, _cyo-cy
            dataset.cxOffset, dataset.cyOffset = cxOffset, cyOffset
            
        def getDataCut(dataset, item, value, parent):
            f1, f2 = dataset.f1, dataset.f2
            x1, x2 = dataset.x1, dataset.x2
            y1, y2 = dataset.y1, dataset.y2
            def nothing(x):
                pass
            cv2.namedWindow('image')
            cv2.createTrackbar('f1','image',f1,dataset.I.shape[0]-1,nothing)
            cv2.createTrackbar('f2','image',f2,dataset.I.shape[0]-1,nothing)
            cv2.createTrackbar('x1','image',x1,dataset.I.shape[2]-1,nothing)
            cv2.createTrackbar('x2','image',x2,dataset.I.shape[2]-1,nothing)
            cv2.createTrackbar('y1','image',y1,dataset.I.shape[1]-1,nothing)
            cv2.createTrackbar('y2','image',y2,dataset.I.shape[1]-1,nothing)
            while(1):
                frame1 = dataset.I[f1].copy()
                frame2 = dataset.I[f2].copy()
                frame1[:,:x1], frame1[:,x2:] = 0, 0
                frame2[:,:x1], frame2[:,x2:] = 0, 0
                frame = np.hstack((frame1, frame2))
                frame[:y1,:], frame[y2:,:] = 0, 0
                cv2.imshow('image',frame)
                k = cv2.waitKey(1) & 0xFF
                cw = cv2.getWindowProperty('image', 1) < 0
                if k == 27 or cw:
                    break
                f1 = cv2.getTrackbarPos('f1','image')
                f2 = cv2.getTrackbarPos('f2','image')
                x1 = cv2.getTrackbarPos('x1','image')
                x2 = cv2.getTrackbarPos('x2','image')
                y1 = cv2.getTrackbarPos('y1','image')
                y2 = cv2.getTrackbarPos('y2','image')
                dataset.f1, dataset.f2 = f1, f2
                dataset.x1, dataset.x2 = x1, x2
                dataset.y1, dataset.y2 = y1, y2
            cv2.destroyAllWindows()
        
        # https://groups.google.com/forum/#!topic/guidata_guiqwt/9qk0TPGLMzk
        img = FileOpenItem("DICOM file:", ("dcm",)).set_prop("display", callback=openFile)
        _bdc = BeginGroup("Data cut")
        f1 = IntItem("First time frame:", default=0, min=0).set_pos(col=0)
        f2 = IntItem("Last time frame:", default=0, min=0).set_pos(col=1)
        x1 = IntItem("Left-most x (px):", default=0, min=0).set_pos(col=2)
        x2 = IntItem("Right-most x (px):", default=0, min=0).set_pos(col=3)
        y1 = IntItem("Top-most y (px):", default=0, min=0).set_pos(col=4)
        y2 = IntItem("Bottom-most y (px):", default=0, min=0).set_pos(col=5)
        bDataCut = ButtonItem('Edit', getDataCut).set_pos(col=6)
        _edc = EndGroup("Data cut")
        
        _bic = BeginGroup("Initial condition")
        _btw = BeginGroup("Tracking window")
        w = IntItem("Width (px):", default=11, min=0).set_pos(col=0)
        h = IntItem("Height (px):", default=5, min=0).set_pos(col=1)
        cx = IntItem("Window center x (px):", default=68, min=0).set_pos(col=2)
        cy = IntItem("Window center y (px):", default=35, min=0).set_pos(col=3)
        cxOffset = IntItem("MTJ x offset from window center (px):", default=0).set_pos(col=4)
        cyOffset = IntItem("MTJ y offset from window center (px):", default=0).set_pos(col=5)
        bCenter = ButtonItem('Edit', getCenter).set_pos(col=2, colspan=2)
        bCenterOffset = ButtonItem('Edit', getOffset).set_pos(col=4, colspan=2)
        _etw = EndGroup("Tracking window")
        _eic = EndGroup("Initial condition")
        
        _bt = BeginGroup("Tracking")
        plotImageInTracking = BoolItem("Plot image while tracking", default=True).set_pos(col=0)
        adjustManuallyCxyOnTracking = BoolItem("Manually adjust MTJ point while tracking", default=False).set_prop("display", store=canManuallyAdjust).set_pos(col=1)
        adjustManuallyCxyOnTrackingCondOFStdUTh = FloatItem("if std dev on optical flow x velocity is greater than (px/s):", default=1, min=0).set_prop("display", active=canManuallyAdjust).set_pos(col=2)
        _blp = BeginGroup("Lee et al. parameters")
        techniqueParsLeeMethod = ChoiceItem("Algorithm:", [('Lee2008', "Lee2008 original"), ('Lee2008_v2', "Lee2008 modified")], default='Lee2008_v2').set_pos(col=0)
        techniqueParsLeePctEx = FloatItem("Velocity bands exclusion percentage (%):", default=0.02, min=0.001, max=1).set_pos(col=1)
        techniqueParsLeePctIn = FloatItem("Velocity bands inclusion percentage (%):", default=0.05, min=0.001, max=1).set_pos(col=2)
        _elp = EndGroup("Lee et al. parameters")
        _et = EndGroup("Tracking")
        
        _br = BeginGroup("Results")
        _bid = BeginGroup("Intermediate data")
        saveTechniqueResToEnabled = BoolItem("Enabled", default=False).set_prop("display", store=canSaveTechniqueResTo)
        saveTechniqueResTo = DirectoryItem("Folder:").set_prop("display", active=canSaveTechniqueResTo)
        plotAddDataOFStdUTh0 = FloatItem("Optical flow x velocity std dev threshold (px/s):", default=2, min=0).set_prop("display", active=canSaveTechniqueResTo).set_pos(col=0)
        plotAddDataOFStdVTh0 = FloatItem("Optical flow y velocity std dev threshold (px/s):", default=0.15, min=0).set_prop("display", active=canSaveTechniqueResTo).set_pos(col=1)
        _eid = EndGroup("Intermediate data")   
        _bfd = BeginGroup("Final data")
        outFile = FileSaveItem("AVI file:", "avi")
        resFile = FileSaveItem("RES file:", "res")
        _efd = EndGroup("Final data")
        _er = EndGroup("Results")
        
    # Create QApplication
    _app = guidata.qapplication()
    e = TrackParameters()
    e.edit()
    
    dcmFile = str(e.img)
    p = {}
    p['plotRawInputImage'] = False
    p['f1'] = int(e.f1)
    p['f2'] = int(e.f2)
    p['y1'] = int(e.y1)
    p['y2'] = int(e.y2)
    p['x1'] = int(e.x1)
    p['x2'] = int(e.x2)
    p['lowpassFilterTime'] = False
    p['cx'] = e.cx
    p['cy'] = e.cy
    p['h'] = e.h
    p['w'] = e.w
    p['adjustManuallyCxy'] = False
    p['cxyHelp'] = {}
    p['adjustManuallyCxyOnTracking'] = e.adjustManuallyCxyOnTracking
    p['adjustManuallyCxyOnTrackingCond'] = ['optical_flow', 'stdU>th', e.adjustManuallyCxyOnTrackingCondOFStdUTh]
    p['cxOffset'] = e.cxOffset
    p['cyOffset'] = e.cyOffset
    p['adjustManuallyCxyOffset'] = False
    p['stepFramesN'] = 1
    p['technique'] = 'optical_flow'
    p['techniquePars'] = ('lk_opt', 'new_centered_mask', 'feature_opt', e.techniqueParsLeeMethod, e.techniqueParsLeePctEx, e.techniqueParsLeePctIn)
    p['plotImageInTracking'] = e.plotImageInTracking
    p['winName'] = ''
    p['timePerImage'] = 'auto'
    p['plotTrackedFeatures'] = False
    p['plotCircle'] = 'last'
    p['plotTechniqueRes'] = False
    p['plotTechniqueResAddData'] = {'OF_std_u_th': [e.plotAddDataOFStdUTh0], 'OF_std_v_th': [e.plotAddDataOFStdVTh0]}
    p['saveTechniqueResTo'] = str(e.saveTechniqueResTo) if e.saveTechniqueResToEnabled else None
    p['outFiles'] = [(str(e.outFile),'auto')]
    resFile = str(e.resFile)
    
    return dcmFile, p, resFile
    
    
    


def trackMTJ(
            img,
            plotRawInputImage=False,
            f1=None, f2=None, y1=None, y2=None, x1=None, x2=None,
            enhanceImage=False, enhancePars=[('smooth_opt',)],
            lowpassFilterTime=False, lowpassFilterTimePars=(4,0.25),
            cx=None, cy=None, h=71, w=131, adjustManuallyCxy=False, cxyHelp={},
            adjustManuallyCxyOnTracking=False, adjustManuallyCxyOnTrackingCond=['optical_flow','stdU>th',1.0],
            cxOffset=0, cyOffset=0, adjustManuallyCxyOffset=False,
            stepFramesN=1,
            technique='optical_flow', techniquePars=('lk_opt','new_centered_mask','feature_opt','kmeans_Lee2008',3,False,0.1,0.05),
            plotImageInTracking=True, winName='', timePerImage='auto', plotTrackedFeatures=False, plotCircle='last',
            plotTechniqueRes=False, plotTechniqueResAddData={}, saveTechniqueResTo=None,
            outFiles=[]     
            ):
                
    """Function for tracking muscle-tendon junction (MTJ) (semi)automatically.
    
    Parameters
    ----------
    img : mixed
        Full path to the 3D sequence file to open, or list containing 3D sequence
        data and metadata. See ``image_utils.readImage()`` for more details.
        
    plotRawInputImage : bool
        If True, 3D sequence will be shown. ImageJ is required in this case.
        
    f1, f2 : mixed
        If positive integer, the 3D sequence will be cut between frame f1 and f2.
        If f1 of f2 are None, respectively the beginning or end will not be cut.
        
    y1, y2 : mixed
        If positive integer, the 3D sequence will be cut between coordinates
        y1 and y2, in height. Image origin (0, 0) is at the top-left corner.
        If y1 of y2 are None, respectively the beginning or end will not be cut.
        
    x1, x2 : mixed
        If positive integer, the 3D sequence will be cut between coordinates
        x1 and x2, in width.
        If x1 of x2 are None, respectively the beginning or end will not be cut.
        
    enhanceImage : bool
        If True, each 2D image will be enhanced for tracking, using parameters 
        specified by ``enhancePars``.
        
    enhancePars : list
        List of tuples, each representing a step in the 2D images enhancing 
        process. Each tuple contains second, third and fourth arguments for
        the function ``enhanceMTJForTracking()``.
        
    lowpassFilterTime : bool
        If True, each 2D image pixel will be low-pass filtered in time, using
        parameters specified by ``lowpassFilterTimePars``.
        
    lowpassFilterTimePars : tuple
        List of parameters indicating the parameter for the Butterworth digital
        low-pass filter. The first one is the filter order, the second one the
        cut-off frequency.
        
    cx, cy : int
        Rectangular mask center position for frame ``f1`` (or 0). This mask is 
        used by the tracking algorithm (see details). If None, they will be set
        to the center of the frame.
    
    h, w : int
        Mask height and width.      
        
    adjustManuallyCxy : bool
        If True, the process will stop and allow the user to select manually
        the center of the mask, on the image ``f1`` (or 0). The window has to
        be close manually for proceeding.
        
    adjustManuallyCxyOnTracking : bool
        If True, the process will stop and allow the user to select manually
        the center of the mask during tracking, if some warning condition is 
        met (see ``adjustManuallyCxyOnTrackingCond``). The window has to be 
        close manually for proceeding.
        
    adjustManuallyCxyOnTrackingCond : list
        Condition on which the manual adjustment during tracking is prompted.
        This list must contain the following items:
        
            0.  The tracking technique (see ``technique``).
            
            1.  A string representing the condition to verify:
            
                - 'stdU>th' ('optical_flow' only): standard deviation of
                  horizontal velocities profile must be greater than a threshold.
                
            2.  From here down, list of parameters relative to point 1:
            
                - for 'stdU>th': threshold value to overcome.
                
        
    cxyHelp : dict
        Dictionary where keys are time frame indices and values are tuples
        containing x and y values for the rectangular mask center.
        If provided, the mask center will be set to this value, ignoring what
        the tracking algorithm found.
        
    cxOffset, cyOffset : int
        It represents the offset between the mask center and the MTJ point.
        
    adjustManuallyCxyOffset : bool
        If True, the process will stop and allow the user to select manually
        the MTJ location, on the image ``f1`` (or 0). The window has to
        be close manually for proceeding.
        
    stepFramesN : int
        It represents the number of frames to jump ahead after is performed
        for current image. If equal or greater than 2, (stepFramesN-1) frames
        will be skipped.
        It can be increased to simulate lower acquisition frequencies for the 
        input file, or larger motion velocities.
        
    technique : str
        String indicating the technique used (see parameter ``techniquePars``
        for details). Possible values are: 'optical_flow', 'template_match'.
        
    techniquePars : tuple
        List of parameters used by the tracking algorithm.
        If ``technique`` is 'optical_flow':
        
            0.  Lukas-Kanade parameters for optical field calculation.
                If dictionary, see keyword parameters for ``cv2.calcOpticalFlowPyrLK()``.
                If 'lk_opt', the optimal parameters will be used.
                
            1.  Features to be tracked.
                If 'new_centered_mask', a new mask will be created around the 
                detected MTJ, and all the points contained in the mask will be 
                tracked.
                If 'good_features', only the features detected as the trackable
                and tracked (**good features**) will be tracked.
                If 'corners_in_centered_mask', only the the Shi-Tomasi corners in
                a mask centered around the the detected MTJ will be tracked.
                If 'append_corners_to_new_good_features_in_centered_mask', 
                Shi-Tomasi corners in the new form will be appended to the good 
                features detected. This full list of features will be tracked.
                
            2.  Parameters for finding corners by using the Shi-Tomasi algorithm.
                If dictionary, see keyword parameters for ``cv2.goodFeaturesToTrack()``.
                If 'feature_opt', the optimal parameters will be used.
                
            3.  Algorithm for processing optical flow results.
                If 'Lee2008', the method described by Lee at all 2008 is applied
                (see ``calcVelocityLee2008(..., direction='max_avg_vel')``).
                If 'Lee2008_v2', the method described by Lee at all 2008 is
                applied, with some small modifications
                (see ``calcVelocityLee2008(..., direction='max_avg_vel')``).
                If 'avg_good_features', an average of the position of the good 
                features detected is calculated.
                If 'lrmost_x_good_features', these further parameters are used::
                
                    uTh = techniquePars[4]
                    nKeep = techniquePars[5]
                    
                For the good features, it calculates the median of the velocities 
                in the x direction. If the velocity is bigger in module than ``uTh``,
                then there is a condition of motion. In this case, only the rightmost
                or leftmost (depending if the motion is going respectively to the 
                right or left) ``nKeep`` good features are retained. And for these,
                the median position is calculated, this being the new MTJ position. 
                The other features are deleted from the list of good features. 
                If the velocity is smaller in module than ``uTh``, then there is a
                condition of rest. The median position for all the good features is 
                calculated.
                'lrmost_x_good_features_adv' is similar to 'lrmost_x_good_features',
                but with an auto-recovery procedure added in motion state. If
                the three previous velocites are, in average, in motion state
                as well but with opposite direction, then the point is not being
                properly tracked. In this case, the new MTJ position is set to the 
                current one, but the mask is enlarged (50% in both dimensions), to 
                ensure a bigger search zone for the next iteration.
                
                .. note::
        
                    Algorithms 'lrmost_x_good_features' and 'lrmost_x_good_features_adv'
                    were developed for the specific motion of the MTJ, that is:
                    
                    - mostly horizontal in the images, some vertical motion is allowed as well.
                    
                    - cyclic, from left to right or vice-versa.
                
                If 'kmeans_Lee2008', these further parameters are used::
                
                    nClusters = techniquePars[4]
                    clusterOnlyVelocity = techniquePars[5]
                    pctEx = techniquePars[6]
                    pctIn = techniquePars[7]
                    
                Firstly, the a k-means clustering is performed on the good features, 
                on both velocity and position, or velocity only, depending on the
                parameter ``clusterOnlyVelocity``. This last flag would allow the 
                user to have cluster that are separated in space. The number of 
                clusters must be specified manually, by ``nClusters``.
                Secondly, the cluster with the biggest number of points is selected.
                Lastly, the algorithm by Lee et al 2008 is applied on these points
                (see ``calcVelocityLee2008()``). ``pctEx`` and ``pctIn`` will be
                used.
                
            4.  From here down, these are parameters for the algorithm at point 3.
            
            
        If ``technique`` is 'template_match':
        
            0.  Allowed motion (in pixels) of the template in horizontal.

            1.  Allowed motion (in pixels) of the template in vertical.
            
            2.  A tuple cointaining the kind of similarity measure and an 
                optional dict  of addictional parameters (see parameters 
                ``meas`` and ``**kwargs`` for ``image_utils.matchTemplate()``).
                
                
        If ``technique`` is 'particle_filter':
        
            0.  Probability models.
                This is a list containing state transition model, observation 
                model, state estimation from weights only, a-posteriori 
                probability model (see ``particle_filter`` module).

            1.  Particles parameters.
                This is list containing the number of particles and a particle
                initializer.
            
            2.  The initial state.
                This is a list of state variable values for the initial frame.
                First 2 state variable must be the positional part of the state
                (x and y position, ``cxy``). If ``adjustManuallyCxy`` is True, 
                positional part is overwritten. State construction depends on
                the models that will use it.
                
            3.  Weights parameters.
                This is a list where the first parameter is a string indicating
                how to calculate particle weigths in case of re-initialization 
                of those (e.g. first frame or point set manually). 
                If 'from_observ_model', weights will be calculated by the
                observation model.
                If 'uniform', all weights will be given the same value.
                
            4.  Resample parameters.
                This is a list where the first parameter is a string indicating
                the particles resampling method (see method 
                ``particle_filter.ParticleFilter.resample()``).
                The second parameter is a string indicating when perform the
                resampling.
                If 'always', resamplingis performed at each iteration.
                If 'below_th', resampling is performed only when the effective
                number of particle goes below one third of the total number of
                particles.
            
        
    plotImageInTracking : bool
        If True, each 2D image is shown on screen during the tracking process.
        
    winName : str
        Name of the window showing sequence.
        
    timePerImage : mixed
        Time for which each 2D image is shown on screen.
        If 'auto', it is automatically calculated from the meta-data in
        ``img``. If not available here, an exception will thrown.
        If float, it must be indicated in milliseconds.
        If ``plotImageInTracking`` is False, this parameter is ignored.
        
    plotTrackedFeatures : bool
        If True, plot the features tracked by the optical flow algorithm.
        If ``technique`` is not 'optical_flow' or if ``plotImageInTracking`` is
        False, this parameter is ignored.
        
    plotCircle : str
        MTJ point is represented as the center of a circle.
        If 'all', image *i* contains the circles from image 0 to *i*.
        If 'last', only the circle in the current image is plotted.
        If ``plotImageInTracking`` is False, this parameter is ignored.
        
    plotTechniqueRes : bool
        If True, plot additional data produced during the tracking stage.
        Execution of the program *is interrupted* until the results windows
        are manually closed.
        If ``technique`` is 'optical_flow', the optical flow is plotted, where
        arrows represent the current (u, v) velocity vector field for the points
        inside the rectangle. Around the center of the rectangle, a blue arrow 
        is plotted, indicating the velocity of the MTJ towards the next image.
        Arrows lengths and directions have the same scale of the x-y axis.
        If the algorithm used is 'kmeans_Lee2008', arrows will be coloured 
        differently for different clusters. The biggest cluster is coloured in
        blue. For any other algorithm, velocities for good features are coloured
        in green, otherwise in red.
        If ``technique`` is 'template_match', template on the previous image
        (smaller rectangle), search window (bigger rectangle), matching indices
        (in greyscale), point with best match and its value are saved for each
        time frame. 
        
    plotTechniqueResAddData : dict
        Additional custom data to be used in plots generated if either
        ``plotTechniqueRes`` is True or ``saveTechniqueResTo`` is not None.
        If ``technique`` is 'optical_flow', the dictionary must contain the
        following keys:
        
        - 'OF_std_u_th', 'OF_std_v_th': list of values representing standard
          deviations from horizontal and vertical velocities calculated by the
          optical flow technique. It can be used as a value to check the 
          horizontal and vertical deformation of the feature tracked.
        
        
    saveTechniqueResTo : mixed
        Path for saving technique results. If None, no data will be saved.
        If str, it must specify the full folder path.
        If ``technique`` is 'optical_flow', the figures created by using the
        flag ``plotTechniqueRes`` are saved. Plus, numeric data about the
        velocities is saved as text files.
        If ``technique`` is 'template_match', the figures created by using the
        flag ``plotTechniqueRes`` are saved.        
        
    outFiles : list
        List of tuples, where each tuple represents an output video to be saved.
        The first element is the full path of the file to be saved. Supported
        formats: avi (Microsoft Video 1 (MSVC) codec).
        The second element is the frame rate. If 'auto', the frame rate of the
        input file. Otherwise, it must be a float number.
        
        

    Returns
    -------
    tuple
        cx, cy, horizontal and vertical position of the MTJ. Values are relative
        to the (0, 0) image corner. These Numpy vectors contain as many frames as
        the original input image. Frames outside the range (f1, f2) are set as
        np.nan.
    
    """

    # Read sequence
    I, metadata = readImage(img, reader='sitk')
            
    # Get time per image
    frame_rate = metadata['frame_rate']
    if timePerImage == 'auto':
        if frame_rate is not None:
            timePerImage = int(1000. / frame_rate)
        else:
            raise Exception('timePerImage cannot be calculated automatically')
    
    if plotRawInputImage:
        # Show images for exploration
        sitk.Show(metadata['raw_obj'])
    
    Nfr_orig = I.shape[0]
    
    # Crop image
    if f1 is None:
        f1 = 0
    if f2 is None:
        f2 = I.shape[0]
    if y1 is None:
        y1 = 0
    if y2 is None:
        y2 = I.shape[1]
    if x1 is None:
        x1 = 0
    if x2 is None:
        x2 = I.shape[2]
    I = I[f1:f2,y1:y2,x1:x2]
    
    # Enhance images
    Ienh = I.copy()
    if enhanceImage:
        for i in xrange(I.shape[0]):
            for enhanceStep in enhancePars:
                enhance_method, enhance_args, enhance_kwargs = enhanceStep + (None,) * (3 - len(enhanceStep))
                Ienh[i] = enhanceMTJForTracking(Ienh[i], enhance_method, enhance_args, enhance_kwargs)
    
    # Time-filter image
    if lowpassFilterTime:
        b, a = signal.butter(*lowpassFilterTimePars)
        Ienh = signal.filtfilt(b, a, Ienh, axis=0)
        Ienh[Ienh>255] = 255
        Ienh[Ienh<0] = 0
        Ienh = Ienh.astype(np.uint8)
        
    # Params for ShiTomasi corner detection
    if technique == 'optical_flow':
        if techniquePars[2] == 'feature_opt':
            feature_params = dict( maxCorners = 100,
                                   qualityLevel = 0.4,
                                   minDistance = 1,
                                   blockSize = 7 )
        else:
            feature_params = techniquePars[2]
    
    # Parameters for lucas kanade optical flow
    #http://stackoverflow.com/questions/23660409/what-is-the-criteria-epsilon-and-maxcount-from-calcopticalflowpyrlk
    if technique == 'optical_flow': 
        if techniquePars[0] == 'lk_opt':
            lk_params = dict( winSize  = (15,15),   # if very low, there will be unrealistic dx,dy
                              maxLevel = 2,
                              criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
        else:
            lk_params = techniquePars[0]         
    
    # Get first frame
    old_frame = Ienh[0]
    old_gray = old_frame
        
    # Define window center
    global _cx, _cy
    _cx, _cy = cx, cy
    def onmouseRect(event, x, y, flags, param):
        global _cx,_cy,p0
        if flags & cv2.EVENT_FLAG_LBUTTON:
            _cx, _cy = int(x), int(y)
            p0 = createCenteredMaskCoords(_cx, _cy, h, w)[:,None,:]
            pts = p0[:,0,:]
            a, b = pts[:,0].min(), pts[:,1].min()
            c, d = pts[:,0].max(), pts[:,1].max()
            area_col = cv2.cvtColor(old_gray, cv2.COLOR_GRAY2BGR)
            area_col2 = cv2.rectangle(area_col, (a,b),(c,d), (0,0,255), 1)
            if area_col2 is not None:
                area_col = area_col2
            cv2.imshow(win, area_col)        
    
    win = 'Click on window center'
    cv2.imshow(win, old_gray)
    global p0  
    p0 = None
    cv2.setMouseCallback(win, onmouseRect)
    if cx is None or cy is None:
        cx, cy = w/2, h/2
    onmouseRect(None, cx, cy, True, None)   # to show rectangle on prompt
    if adjustManuallyCxy:
        cv2.waitKey()
    cv2.destroyAllWindows()
    cx, cy = _cx, _cy
    print cx, cy
    
    # Define offset point
    global _cxo, _cyo
    _cxo, _cyo = cxOffset + cx, cyOffset + cy
    def onmouseOffset(event, x, y, flags, param):
        global _cxo,_cyo
        if flags & cv2.EVENT_FLAG_LBUTTON:
            _cxo, _cyo = int(x), int(y)
            area_col = cv2.cvtColor(old_gray, cv2.COLOR_GRAY2BGR)
            area_col2 = cv2.circle(area_col,(int(_cxo),int(_cyo)),5,(0,0,255),1)
            if area_col2 is not None:
                area_col = area_col2
            cv2.imshow(win, area_col)        
    
    win = 'Click on offset point'
    cv2.imshow(win, old_gray)
    cv2.setMouseCallback(win, onmouseOffset)
    onmouseOffset(None, _cxo, _cyo, True, None)   # to show point on prompt
    if adjustManuallyCxyOffset:
        cv2.waitKey()
    cv2.destroyAllWindows()
    cxo, cyo = _cxo-cx, _cyo-cy
    print cxo, cyo
    
    #features = 'corners_only'
    features = 'all_points'
    if features == 'all_points':
        pass
    elif features == 'corners_only':
        p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
        print p0
        
    # Parameters for particle filter
    if technique == 'particle_filter':
        
        # Create particle filter
        pf = ParticleFilter()
        
        # Set additional data (must be before observation model call)
        addData = {}
        addData['I'] = old_gray
        addData['boxSize'] = w,h
        addData['posManuallySet'] = False
        addData['otherPars'] = techniquePars[5]
        pf.setAdditionalData(addData)
        
        # Set models
        models = techniquePars[0]
        pf.setProbTransModel(models[0])
        pf.setProbObservModel(models[1])
        pf.setStateEstimatorFromWeightsFun(models[2])
        pf.setProbEstimModel(models[3])
        
        # Set initial state
        x0 = techniquePars[2].copy()
        x0[:2] = cx, cy
        xEst = x0[:,None]
        pf.setState(xEst)
        
        # Create initial particles set
        particlesPars = techniquePars[1]
        nParticles = particlesPars[0]
        particlesInitializer = particlesPars[1]
        xParticles = particlesInitializer(nParticles, xEst, addData)
        pf.setParticles(xParticles)
        
        # Set initial particle weights
        weightsPars = techniquePars[3]
        if weightsPars[0] == 'from_observ_model':
            #observModel = models[1]
            #wParticles = observModel(xParticles, xEst, None, addData)
            pf.update()
            wParticles = pf.getUpdatedParticleWeights()
        elif weightsPars[0] == 'uniform':
            wParticles = np.ones((nParticles,)) / nParticles
        pf.setParticleWeights(wParticles)

    
    # Create some random colors
    color = np.random.randint(0,255,(h*w,3))
    color_quiver = np.random.rand(1000,3)
    
    # Create a mask image for drawing purposes
    mask_good = np.zeros_like(old_frame)
    mask_good = cv2.cvtColor(mask_good, cv2.COLOR_GRAY2BGR)
    mask_circle = mask_good.copy()
    mask_empty = mask_good.copy()
    
    Nfr = Ienh.shape[0]
    cx_res = np.zeros((Nfr_orig,)) * np.nan
    cy_res = cx_res.copy()
    cx_res[f1], cy_res[f1] = cx + cxo, cy + cyo
     
    u_buffer = np.zeros((3,))
    Iout = np.empty_like(Ienh)
    Iout[0] = old_gray
    
    SNRu = np.zeros((Nfr,)) * np.nan
    SNRv = SNRu.copy()
    
    stdu = np.zeros((Nfr,)) * np.nan
    stdv = stdu.copy()
    
    for fr in xrange(1, Nfr, stepFramesN):
        
        print 'Frame: %d' % (f1+fr)
        
        # Get current frame
        frame = Ienh[fr]
        frame_gray = frame.copy()
        frame_col = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        
        # Update old point
        old_cx, old_cy = cx, cy
        
        # Get rectangle coordinates 
        all_old = createCenteredMaskCoords(cx, cy, h, w)
        #all_new_r, all_new_c = all_new[:,1].astype(np.int32), all_new[:,0].astype(np.int32)
        all_old_r, all_old_c = all_old[:,1].astype(np.int32), all_old[:,0].astype(np.int32)
        ar, br = all_old_c.min(), all_old_r.min()
    
        if technique == 'optical_flow':
            
            # Get rectangle borders
            a_rect, b_rect = p0[:,0,0].min(), p0[:,0,1].min()
            c_rect, d_rect = p0[:,0,0].max(), p0[:,0,1].max()
    
            # Calculate (sparse) optical flow
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
            
            # Select points
            good_new = p1[st==1]
            good_old = p0[st==1]
            bad_new = p1[st==0]
            bad_old = p0[st==0]
            all_new = p1[:,0,:]
            all_old = p0[:,0,:]
            all_new_r, all_new_c = all_new[:,1].astype(np.int32), all_new[:,0].astype(np.int32)
            #all_old_r, all_old_c = all_old[:,1].astype(np.int32), all_old[:,0].astype(np.int32)
            
            # Calculate error measures
            all_err_fun = err[:,0]
            mask_err_fun = np.zeros((h,w))
            mask_err_fun[all_old_r-br,all_old_c-ar] = all_err_fun
            mask_err_OF = np.zeros((h,w))
            mask_err_OF[all_old_r-br,all_old_c-ar] = np.abs(frame_gray[all_new_r,all_new_c].astype(np.float32) - 
                                                          old_gray[all_old_r,all_old_c].astype(np.float32))
            
            if plotTrackedFeatures:
                # draw the tracks
                for i,(new,old) in enumerate(zip(good_new,good_old)):
                    a,b = new.ravel()
                    c,d = old.ravel()
                    mask_good2 = cv2.line(mask_good, (a,b),(c,d), color[i].tolist(), 1)
                    if mask_good2 is not None:
                        mask_good = mask_good2
                        
    
            all_x = all_old[:,0]
            all_y = all_old[:,1]
            all_dx = all_new[:,0] - all_x
            all_dy = all_new[:,1] - all_y
            good_x = good_old[:,0]
            good_y = good_old[:,1]
            good_dx = good_new[:,0] - good_x
            good_dy = good_new[:,1] - good_y
            bad_x = bad_old[:,0]
            bad_y = bad_old[:,1]
            bad_dx = bad_new[:,0] - bad_x
            bad_dy = bad_new[:,1] - bad_y
            
            new_h, new_w = h, w
            
            method = techniquePars[3]
            
            if method == 'Lee2008':
                pctEx = techniquePars[4]
                pctIn = techniquePars[5]
                u, v, mask_u, mask_v = calcVelocityLee2008(all_dx, all_dy, pctEx, pctIn, direction='max_avg_vel')
                cx, cy = old_cx + u, old_cy + v
            elif method == 'Lee2008_v2':
                pctEx = techniquePars[4]
                pctIn = techniquePars[5]
                u, v, mask_u, mask_v = calcVelocityLee2008(all_dx, all_dy, pctEx, pctIn, direction='pct_sign')
                cx, cy = old_cx + u, old_cy + v                
            elif method == 'avg_good_features':
                cx = np.mean(good_new[:,0])
                cy = np.mean(good_new[:,1])
                u, v = cx - old_cx, cy - old_cy
            elif method == 'lrmost_x_good_features':
                u_th = techniquePars[4]
                N_keep = techniquePars[5]
                u_avg = np.median(good_dx)
                if np.abs(u_avg) > u_th:
                    if u_avg < 0:
                        idx_x = np.argsort(good_new[:,0])[:N_keep]
                    else:
                        idx_x = np.argsort(good_new[:,0])[-N_keep:]
                else:
                    idx_x = np.arange(good_new.shape[0])
                cx = np.median(good_new[idx_x,0])
                cy = np.median(good_new[idx_x,1])
                u, v = cx - old_cx, cy - old_cy
                good_new = good_new[idx_x,:]
            elif method == 'lrmost_x_good_features_adv':
                u_th = techniquePars[4]
                N_keep = techniquePars[5]
                u_avg = np.median(good_dx)
                u_avg_buffer = np.median(u_buffer)
                print 'horizontal avg velocity: %.2f' % u_avg
                # Decide upon velocity
                if np.abs(u_avg) > u_th: # "motion" state      
                    if np.sign(u_avg_buffer * u_avg) < 0 and np.abs(u_avg_buffer) > u_th: # opposite motion
                        new_w += int(0.5 * w)
                        new_h += int(0.5 * h)
                        cx, cy = old_cx, old_cy                        
                    else: # realistic
                        if u_avg < 0:
                            idx_x = np.argsort(good_new[:,0])[:N_keep]
                            cx = good_new[idx_x[0],0]
                            cy = good_new[idx_x[0],1]
                        else:
                            idx_x = np.argsort(good_new[:,0])[-N_keep:]
                            cx = good_new[idx_x[-1],0]
                            cy = good_new[idx_x[-1],1]
                        good_new = good_new[idx_x,:]
                else: # "resting" state
                    cx = np.median(good_new[:,0])
                    cy = np.median(good_new[:,1])
                u, v = cx - old_cx, cy - old_cy
                # Update velocity buffer
                u_buffer = np.roll(u_buffer, 1)
                u_buffer[0] = u
            elif method == 'kmeans_Lee2008':
                nClusters = techniquePars[4]
                clusterOnlyVelocity = techniquePars[5]
                pctEx = techniquePars[6]
                pctIn = techniquePars[7]
                # Run k-means clustering
                Z = np.vstack((good_dx,good_dy,good_x,good_y)).T
                Z = np.float32(Z)
                criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
                if clusterOnlyVelocity:
                    Zc = Z[:,:2]
                else:
                    Zc = Z
                ret_km,label_km,center_km=cv2.kmeans(Zc,nClusters,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
                # Search for biggest cluster                
                Npoints = 0            
                for l in xrange(0,nClusters):
                    D = Z[label_km.ravel()==l] 
                    if D.shape[0] > Npoints:
                        Npoints = D.shape[0]
                        l_max = l
                A = Z[label_km.ravel()==l_max]
                # Calc velocity
                u, v, mask_u, mask_v = calcVelocityLee2008(A[:,0], A[:,1], pctEx, pctIn)
                cx, cy = old_cx + u, old_cy + v
            else:
                u, v = np.nan, np.nan
                cx, cy = np.nan, np.nan
                
            # Use manually inputted cxy if existing
            if f1+fr in cxyHelp:
                cx, cy = cxyHelp[f1+fr][0] - x1 - cxo, cxyHelp[f1+fr][1] - y1 - cyo
                print 'Point adjusted manually'

            print 'Point velocity: (%.2f, %.2f)' % (u, v)
            print 'Point position: (%.2f, %.2f)' % (cx, cy)
            
            trackFeatures = techniquePars[1]
            if trackFeatures == 'new_centered_mask':
                new_mask, pts = createWhiteMask(frame_gray, cx, cy, new_h, new_w)
                p0 = pts[:,None,:]
            elif trackFeatures == 'good_features':
                p0 = good_new[:,None,:]
            elif trackFeatures == 'corners':
                p0 = cv2.goodFeaturesToTrack(frame_gray, mask=None, **feature_params)
            elif trackFeatures == 'corners_in_centered_mask':
                p0, new_mask = findCornersInMask(frame_gray, cx, cy, new_h, new_w, feature_params)
                if p0 is None:
                    raise Exception('No new corners to track')
            elif trackFeatures == 'append_corners_to_new_good_features_in_centered_mask':
                new_p0, new_mask = findCornersInMask(frame_gray, cx, cy, new_h, new_w, feature_params)
                if new_p0 is not None:
                    p0 = np.concatenate([good_new[:,None,:], new_p0])
                else:
                    p0 = good_new[:,None,:]
            if plotImageInTracking:
                if trackFeatures <> 'good_features' and trackFeatures <> 'corners':
                    cv2.imshow('Mask',new_mask)
                
                
            if plotTechniqueRes == True or saveTechniqueResTo is not None:

                # Plot quiver
                print 'Creating quiver plot ...'
                plt.figure(1)
                plt.clf()
                plt.subplot(212)
                quiver_params = dict(   angles = 'xy', 
                                        scale_units = 'xy',
                                        scale = 1
                                    )
                plt.hold(True)
                if method == 'kmeans_Lee2008':
                    patches = []
                    for l in xrange(0,nClusters):
                        D = Z[label_km.ravel()==l]
                        plt.quiver(D[:,2], D[:,3], D[:,0], D[:,1], color=color_quiver[l], **quiver_params)
                        label = 'Cluster %d' % (l+1)                        
                        if l == l_max:
                            label += ' (max)'
                        patches.append(mpatches.Patch(color=color_quiver[l], label=label))
                    plt.legend(handles=patches, framealpha=0.)
                else:
                    plt.quiver(good_x, good_y, good_dx, good_dy, color='g', **quiver_params)
                    plt.quiver(bad_x, bad_y, bad_dx, bad_dy, color='r', **quiver_params)
                plt.quiver(old_cx, old_cy, u, v, color='b', **quiver_params)
                plt.hold(False)
                plt.xlim(all_x.min(), all_x.max())
                plt.ylim(all_y.max(), all_y.min())
                plt.title('Quiver plot')
                # Plot current and previous image
                print 'Creating raw images plots ...'
                old_frame = old_gray.copy()
                old_frame2 = cv2.rectangle(old_frame, (a_rect,b_rect),(c_rect,d_rect), 255, 1)
                if old_frame2 is not None:
                    old_frame = old_frame2
                plt.subplot(211)
                plt.imshow(old_frame, cmap=plt.cm.gray)
                plt.hold(True)
                plt.plot(old_cx+cxo, old_cy+cyo, 'o', mfc='none', mec='b', scalex=False, scaley=False)
                plt.hold(False)
                plt.title('Previous image')
                if method == 'Lee2008' or method == 'Lee2008_v2':
                    # Plot ordered velocities for Lee method
                    plt.figure(2)
                    plt.clf()
                    idxU = np.argsort(all_dx)
                    idxV = np.argsort(all_dy)
                    U = all_dx
                    V = all_dy
                    x = np.arange(U.shape[0])
                    plt.subplot(121)
                    plt.bar(x, U[idxU])
                    ymin, ymax = plt.ylim()
                    maskLine = (ymin + (ymax - ymin) * 0.1 * mask_u[idxU])
                    plt.hold(True)
                    plt.plot(x, maskLine)
                    plt.ylim([ymin, ymax])
                    plt.xlim([x.min(), x.max()])
                    plt.title('u')
                    plt.hold(False)
                    plt.subplot(122)
                    plt.bar(x, V[idxV])
                    ymin, ymax = plt.ylim()
                    maskLine = (ymin + (ymax - ymin) * 0.1 * mask_v[idxV])
                    plt.hold(True)
                    plt.plot(x, maskLine)
                    plt.ylim([ymin, ymax])
                    plt.xlim([x.min(), x.max()])
                    plt.title('v')
                    plt.hold(False)

                
            if saveTechniqueResTo is not None:
                folderName = saveTechniqueResTo
                # Save velocity masks
                print 'Saving velocities ...'
                uMatrix = np.zeros((h,w))
                vMatrix = np.zeros((h,w))
                coordX = (all_x-all_x[0]).astype(np.int32)
                coordY = (all_y-all_y[0]).astype(np.int32)
                uMatrix[coordY, coordX] = all_dx
                vMatrix[coordY, coordX] = all_dy
                header = 'AVG: %+5.3f; MEDIAN: %+5.3f; STDDEV: %+5.3f; MIN: %+5.3f; MAX: %+5.3f;' \
                % (np.mean(uMatrix), np.median(uMatrix), np.std(uMatrix), np.min(uMatrix), np.max(uMatrix))
                filePath = folderName + '/%04d_U.txt' % (f1+fr)
                np.savetxt(filePath, uMatrix, delimiter='\t', fmt='%+5.3f', header=header)
                header = 'AVG: %+5.3f; MEDIAN: %+5.3f; STDDEV: %+5.3f; MIN: %+5.3f; MAX: %+5.3f;' \
                % (np.mean(vMatrix), np.median(vMatrix), np.std(vMatrix), np.min(vMatrix), np.max(vMatrix))
                filePath = folderName + '/%04d_V.txt' % (f1+fr)
                np.savetxt(filePath, vMatrix, delimiter='\t', fmt='%+5.3f', header=header)
                filePath = folderName + '/%04d_uv.txt' % (f1+fr)
                np.savetxt(filePath, (u, v), delimiter='\t', fmt='%+5.3f', header='Final (u, v)')
                if method == 'Lee2008' or method == 'Lee2008_v2':
                    # Save velocity masks
                    print 'Saving velocity masks ...'
                    uMaskMatrix = np.zeros((h,w))
                    vMaskMatrix = np.zeros((h,w))
                    uMatrix[coordY, coordX] = all_dx
                    vMatrix[coordY, coordX] = all_dy
                    uMaskMatrix[coordY, coordX] = mask_u
                    vMaskMatrix[coordY, coordX] = mask_v
                    header = '0: excluded (low); 1: used for avg; 2,3: excluded (high)'
                    filePath = folderName + '/%04d_U_mask.txt' % (f1+fr)
                    np.savetxt(filePath, uMaskMatrix, delimiter='\t', fmt='%1d', header=header)
                    filePath = folderName + '/%04d_V_mask.txt' % (f1+fr)
                    np.savetxt(filePath, vMaskMatrix, delimiter='\t', fmt='%1d', header=header)
                    # Save some indices
                    Uex = U[mask_u==3]
                    u_ex = np.mean(Uex)
                    idx1u = (u_ex - u) / u_ex
                    Vex = V[mask_v==3]
                    v_ex = np.mean(Vex)
                    idx1v = (v_ex - v) / v_ex
                    Ulow = U[mask_u==0]
                    u_low = np.mean(Ulow)
                    idx2u = (u - u_low) / u
                    Vlow = V[mask_v==0]
                    v_low = np.mean(Vlow)
                    idx2v = (v - v_low) / v
                    filePath = folderName + '/%04d_indices_check_Lee.txt' % (f1+fr)
                    with open(filePath, 'w') as f:
                        f.write('(AVG(Uex) - u) / AVG(Uex): %+5.3f\n' % idx1u)
                        f.write('(AVG(Vex) - v) / AVG(Vex): %+5.3f\n' % idx1v)
                        f.write('(u - AVG(Ulow)) / u: %+5.3f\n' % idx2u)
                        f.write('(v - AVG(Vlow)) / v: %+5.3f\n' % idx2v)
                # Save some indices
                SNRu[fr] = np.mean(all_dx) / np.std(all_dx)
                SNRv[fr] = np.mean(all_dy) / np.std(all_dy)
                stdu[fr] = np.std(all_dx)
                stdv[fr] = np.std(all_dy)
                filePath = folderName + '/%04d_indices_check.txt' % (f1+fr)
                with open(filePath, 'w') as f:
                    f.write('SNR u: %+5.3f\n' % SNRu[fr])
                    f.write('SNR v: %+5.3f\n' % SNRv[fr])
                    f.write('STD(U): %+5.3f\n' % stdu[fr])
                    f.write('STD(V): %+5.3f\n' % stdv[fr])
                # Save optical flow errors
                header = 'AVG: %+5.3f; MEDIAN: %+5.3f; STDDEV: %+5.3f; MIN: %+5.3f; MAX: %+5.3f;' \
                % (np.mean(mask_err_fun), np.median(mask_err_fun), np.std(mask_err_fun), np.min(mask_err_fun), np.max(mask_err_fun))
                filePath = folderName + '/%04d_err_LK_fun.txt' % (f1+fr)
                np.savetxt(filePath, mask_err_fun, delimiter='\t', fmt='%+5.3f', header=header)
                header = 'AVG: %+5.3f; MEDIAN: %+5.3f; STDDEV: %+5.3f; MIN: %+5.3f; MAX: %+5.3f;' \
                % (np.mean(mask_err_OF), np.median(mask_err_OF), np.std(mask_err_OF), np.min(mask_err_OF), np.max(mask_err_OF))
                filePath = folderName + '/%04d_err_brightness_constancy.txt' % (f1+fr)
                np.savetxt(filePath, mask_err_OF, delimiter='\t', fmt='%+5.3f', header=header)
                print 'Saving figures ...'
                plt.figure(1)
                filePath = folderName + '/%04d_OF.jpeg' % (f1+fr)
                plt.savefig(filePath, format='jpeg', dpi=300)
                if method == 'Lee2008' or method == 'Lee2008_v2':
                    plt.figure(2)
                    filePath = folderName + '/%04d_OF_vel_Lee.jpeg' % (f1+fr)
                    plt.savefig(filePath, format='jpeg', dpi=100)
                
#            if plotTechniqueRes:
#                print 'Plotting data ...'
#                plt.show()
                
        elif technique == 'template_match':
            
            a_rect, c_rect = old_cx-(w-1)/2, old_cx+(w-1)/2
            b_rect, d_rect = old_cy-(h-1)/2, old_cy+(h-1)/2
            template = old_gray[b_rect:d_rect+1,a_rect:c_rect+1]
            hSrch = techniquePars[0]
            wSrch = techniquePars[1]
            meas = techniquePars[2]
            a_rect2, c_rect2 = a_rect-wSrch, c_rect+1+wSrch
            b_rect2, d_rect2 = b_rect-hSrch, d_rect+1+hSrch
            search_win = frame_gray[b_rect2:d_rect2,a_rect2:c_rect2]
            #res = cv2.matchTemplate(search_win,template,cv2.TM_CCORR_NORMED)
            if len(meas) == 1:
                meas.append({})
            res = matchTemplate(search_win,template,meas[0],**meas[1])
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            cx = a_rect2 + top_left[0] + (w-1)/2
            cy = b_rect2 + top_left[1] + (h-1)/2
            new_h, new_w = h, w
            
            # Use manually inputted cxy if existing
            if f1+fr in cxyHelp:
                cx, cy = cxyHelp[f1+fr][0] - x1 - cxo, cxyHelp[f1+fr][1] - y1 - cyo
                print 'Point adjusted manually'
            
            if plotImageInTracking:
                cv2.imshow('Template',template)
            
            if plotTechniqueRes == True or saveTechniqueResTo is not None:
                plt.clf()
                # Plot images
                print 'Creating images plots ...'
                old_frame = old_gray.copy()
                old_frame2 = cv2.rectangle(old_frame, (a_rect,b_rect),(c_rect,d_rect), 255, 1)
                if old_frame2 is not None:
                    old_frame = old_frame2
                curr_frame = frame_gray.copy()
                curr_frame2 = cv2.rectangle(curr_frame, (a_rect2,b_rect2),(c_rect2,d_rect2), 255, 1)
                if curr_frame2 is not None:
                    curr_frame = curr_frame2
                plt.subplot(221)
                plt.imshow(old_frame, cmap=plt.cm.gray)
                plt.title('Previous image (template)')
                plt.subplot(222)
                plt.imshow(curr_frame, cmap=plt.cm.gray)
                plt.title('Current image (search win)')
                plt.hold(True)
                plt.plot(cx, cy, 'o', mfc='none', mec='r', scalex=False, scaley=False)
                plt.plot(cx+cxo, cy+cyo, 'o', mfc='none', mec='b', scalex=False, scaley=False)
                plt.hold(False)
                plt.subplot(224)
                plt.imshow(res, cmap=plt.cm.gray)
                plt.title('Similarity index (max = %.3f)' % max_val)
                plt.hold(True)
                plt.plot(top_left[0], top_left[1], 'o', mfc='none', mec='r', scalex=False, scaley=False)
                plt.hold(False)
                
            if saveTechniqueResTo is not None:
                print 'Saving figures ...'
                folderName = saveTechniqueResTo
                filePath = folderName + '/%04d_TM.jpeg' % (f1+fr)
                plt.savefig(filePath, format='jpeg', dpi=300)
                print 'Saving NCCs profile ...'
                filePath = folderName + '/%04d_%s.txt' % (f1+fr, meas[0])
                np.savetxt(filePath, res, delimiter='\t', fmt='%+5.3f')
                
#            if plotTechniqueRes:
#                print 'Plotting data ...'
#                plt.show()
                
        elif technique == 'particle_filter':
                      
            # Iterate particle filter state
            addData['I'] = frame_gray # must be before observation model call (update)
            addData['posManuallySet'] = False
            pf.predict()
            xParticles = pf.getPredictedParticles()
            print 'Particles predicted'
            nParticles = xParticles.shape[1]
            pf.update()
            wNextNorm = pf.getUpdatedParticleWeights()
            print 'Particle weights updated'
            pf.estimateStateFromWeights()
            print 'Next state estimated from weights only'
            xNextEst = pf.estimateNextState()
            print 'Next state estimated'
            
            # Append new estimated state to states history
            xEst = np.hstack((xEst, xNextEst[:,None]))
            
            # Get position from state
            cx, cy = xEst[0,-1], xEst[1,-1]
            
            # Resample particles
            nEffParticles = pf.getEffectParticlesNumber()
            print 'Effective particles number calculated'
            resamplePars = techniquePars[4]
            resampleMode = resamplePars[0]
            resampleWhen = resamplePars[1]
            condRes = False
            if resampleWhen == 'always':
                condRes = True
            elif resampleWhen == 'below_th':
                if nEffParticles < nParticles / 3:
                    condRes = True
            if condRes:
                xNextParticles = pf.resample(mode=resampleMode)
                print 'Particles resampling performed'
                    
            # Use manually inputted cxy if existing
            if f1+fr in cxyHelp:
                cx, cy = cxyHelp[f1+fr][0] - x1 - cxo, cxyHelp[f1+fr][1] - y1 - cyo
                print 'Point adjusted manually'
                addData['posManuallySet'] = True
                x0 = xNextEst.copy()    # apart from position, keep all the estimate
                x0[:2] = cx, cy
                xEst[:,-1] = x0
                print 'Positional data for new state added, non-positional data copied'
                xNextParticles = particlesInitializer(nParticles, xEst, addData)
                print 'Particles set reinitialized'
                #wNextNorm = observModel(xNextParticles, xEst, None, addData)
                pf.setParticles(xNextParticles)
                pf.update()
                wNextNorm = pf.getUpdatedParticleWeights()
                print 'Particle weights regenerated using observation model'
                pf.estimateStateFromWeights()
                print 'Next state estimated from weights only'
                xNextEst = pf.estimateNextState()
                print 'Next state estimated'
                xEst[:,-1] = xNextEst
            
            # Set particles for next iteration
            pf.setParticles(xNextParticles)
            pf.setParticleWeights(wNextNorm) # not necessary when resampling is done
            pf.setState(xEst)
            print 'Particle data set for next iteration'
            
            if plotTechniqueRes == True or saveTechniqueResTo is not None:
                plt.clf()
                # Plot images
                print 'Creating images plots ...'
                old_frame = old_gray.copy()
                plt.subplot(211)
                plt.imshow(frame_gray, cmap=plt.cm.gray)
                plt.title('Current image (particles)')
                plt.hold(True)
                plt.scatter(xParticles[0,:], xParticles[1,:], s=2, c=wNextNorm, cmap=plt.cm.jet, norm=Normalize(), lw=0)
                plt.plot(cx, cy, 'o', mfc='none', mec='r', scalex=False, scaley=False)
                plt.plot(cx+cxo, cy+cyo, 'o', mfc='none', mec='b', scalex=False, scaley=False)
                plt.hold(False)
                plt.subplot(212)
                plt.bar(np.arange(nParticles), wNextNorm)
                plt.title('Normalized weights (PDF), Neff = %d' % nEffParticles)
                plt.hold(False)
                
            if saveTechniqueResTo is not None:
                print 'Saving figures ...'
                folderName = saveTechniqueResTo
                filePath = folderName + '/%04d_PF.jpeg' % (f1+fr)
                plt.savefig(filePath, format='jpeg', dpi=100)
            
        else:
            
            cx, cy = np.nan, np.nan
             
            
        if np.isnan(cx) == False:
            # Show circle
            if plotCircle == 'all':
                mask_circle2 = cv2.circle(mask_circle,(int(cx+cxo),int(cy+cyo)),5,(0,0,255),1)
                if mask_circle2 is not None:
                    mask_circle = mask_circle2
            elif plotCircle == 'last':
                mask_empty2 = mask_empty.copy()
                mask2 = cv2.circle(mask_empty2,(int(cx+cxo),int(cy+cyo)),5,(0,0,255),1)
                if mask2 is not None:
                    mask_empty2 = mask2
                mask_circle = mask_empty2
            
        # Add good features mask to circle mask
        idx_nonblack = np.sum(mask_circle, axis=2) > 0
        mask = mask_good.copy()
        mask[idx_nonblack] = mask_circle[idx_nonblack]
        
        # Add mask to image
        idx_nonblack = np.sum(mask, axis=2) > 0
        img = frame_col.copy()
        img[idx_nonblack] = mask[idx_nonblack]
        
        # Convert image with tracked point plotted back to gray
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        Iout[fr] = img_gray
    
        # Show image
        if plotImageInTracking:
            cv2.imshow('Tracking '+winName,img)
            k = cv2.waitKey(int(timePerImage)) & 0xff
            if k == 27:
                break
            
        if technique == 'optical_flow' or technique == 'template_match':
            # Calculate general errors
            #all_new = p0[:,0,:]
            all_new = createCenteredMaskCoords(cx, cy, h, w)
            all_new_r, all_new_c = all_new[:,1].astype(np.int32), all_new[:,0].astype(np.int32)
            mask_err_patch = np.zeros((h,w))
            if new_h == h and new_w == w:
                mask_err_patch[all_old_r-br,all_old_c-ar] = np.abs(frame_gray[all_new_r,all_new_c].astype(np.float32) - 
                                                                   old_gray[all_old_r,all_old_c].astype(np.float32))
                
            if saveTechniqueResTo is not None:
                # Save general errors info  
                header = 'AVG: %+5.3f; MEDIAN: %+5.3f; STDDEV: %+5.3f; MIN: %+5.3f; MAX: %+5.3f;' \
                % (np.mean(mask_err_patch), np.median(mask_err_patch), np.std(mask_err_patch), np.min(mask_err_patch), np.max(mask_err_patch))
                filePath = folderName + '/%04d_err_patch.txt' % (f1+fr)
                np.savetxt(filePath, mask_err_patch, delimiter='\t', fmt='%+5.3f', header=header)
                
        if plotTechniqueRes:
            print 'Plotting data ...'
            plt.show()
            
        # Prompt live manual adjustment if necessary
        if adjustManuallyCxyOnTracking:
            cond = adjustManuallyCxyOnTrackingCond
            if cond[0] == technique:
                if cond[1] == 'stdU>th':
                    th = cond[2]
                    stdU = np.std(all_dx)
                    print 'Std. dev u: %+5.3f, th. u: %+5.3f' % (stdU, th)
                    if stdU > th:
                        # Show prompt to click point manually
                        win = 'Manually click on window center'
                        cv2.destroyAllWindows() # needed for the following waitKey() to work properly
                        cv2.imshow(win, old_gray)
                        _cx, _cy = cx, cy
                        cv2.setMouseCallback(win, onmouseRect)
                        #cv2.setMouseCallback(win, onmouseOffset)                        
                        onmouseRect(None, cx+cxOffset, cy+cyOffset, True, None)   # to show rectangle on prompt
                        #onmouseOffset(None, cx+cxOffset, cy+cyOffset, True, None)
                        cv2.waitKey()
                        cv2.destroyAllWindows()
                        cx, cy = _cx-cxOffset, _cy-cyOffset
    
        # Now update the previous frame
        old_gray = frame_gray.copy()
        
        cx_res[f1+fr], cy_res[f1+fr] = x1 + cx + cxo, y1 + cy + cyo
    
    cv2.destroyAllWindows()
    
    # Save some global indices
    if plotTechniqueRes == True or saveTechniqueResTo is not None:
        
        if technique == 'optical_flow':
            # Save SNR info
            header = 'AVG: %+5.3f; MEDIAN: %+5.3f; STDDEV: %+5.3f; MIN: %+5.3f; MAX: %+5.3f;' \
            % (np.nanmean(SNRu), np.nanmedian(SNRu), np.nanstd(SNRu), np.nanmin(SNRu), np.nanmax(SNRu))
            filePath = folderName + '/global_SNR_u.txt'
            np.savetxt(filePath, SNRu, delimiter='\t', fmt='%+5.3f', header=header)
            header = 'AVG: %+5.3f; MEDIAN: %+5.3f; STDDEV: %+5.3f; MIN: %+5.3f; MAX: %+5.3f;' \
            % (np.nanmean(SNRv), np.nanmedian(SNRv), np.nanstd(SNRv), np.nanmin(SNRv), np.nanmax(SNRv))
            filePath = folderName + '/global_SNR_v.txt'
            np.savetxt(filePath, SNRv, delimiter='\t', fmt='%+5.3f', header=header)   
            # Save graph for velocities std dev
            thu = plotTechniqueResAddData['OF_std_u_th']
            thv = plotTechniqueResAddData['OF_std_v_th']
            x = np.arange(Nfr) + f1
            xm = np.arange(Nfr, step=10) + f1
            plt.figure(3)
            ax = plt.subplot(211)
            plt.plot(x, stdu)
            plt.hold(True)
            for th in thu:
                plt.plot([x[0], x[-1]], [th, th], 'r-')
            ax.set_xticks(xm)
            ax.set_xticks(x, minor=True)
            ax.grid(which='both')
            plt.ylabel('Std dev U (pixels/frame)')
            ax = plt.subplot(212)
            plt.plot(x, stdv)
            plt.hold(True)
            for th in thv:
                plt.plot([x[0], x[-1]], [th, th], 'r-')
            ax.set_xticks(xm)
            ax.set_xticks(x, minor=True)
            ax.grid(which='both')
            plt.xlabel('Frame number')
            plt.ylabel('Std dev V (pixels/frame)')
            filePath = folderName + '/global_std_uv.jpeg'
            plt.savefig(filePath, format='jpeg', dpi=300)
            
    
    if plotTechniqueRes:
        print 'Plotting data ...'
        plt.show()
    
    # Export files
    for outFile in outFiles:
        file_name = outFile[0]
        fps = outFile[1]
        if fps == 'auto':
            fps = frame_rate
        arr2seqFile(file_name, Iout, fps)
    
    # Return data
    return cx_res, cy_res
    
    
    
    
    
def trackMTJMultiTrackers(
            img,
            trackersN,
            trackersPars=None,
            f1=None, f2=None, y1=None, y2=None, x1=None, x2=None,
            plotImageInTracking=True, timePerImage='auto', plotTrackedFeatures=True,
            plotTechniqueRes=False, saveTechniqueResTo=None, # to be used in the future
            outFiles=[],     
            ):
           
    """Function for tracking muscle-tendon junction (MTJ) (semi)automatically,
    by using N different trackers. Only one tracker at a time is run.
    
    Parameters
    ----------
    img : mixed
        Full path to the 3D sequence file to open, or list containing 3D sequence
        data and metadata. See ``image_utils.readImage()`` for more details.
        
    trackersN : int
        Number of trackers.
        
    trackersPars : list
        List where each element is a dict where keys are keyword elements of
        for function ``trackMTJ()``, and values are the respective parameters.
        Only the first ``trackersN`` will be used.
        
    f1, f2 : mixed
        If positive integer, the 3D sequence will be cut between frame f1 and f2.
        If f1 of f2 are None, respectively the beginning or end will not be cut.
        This parameter is only used for multi-track image display and video
        creation.
        
    y1, y2 : mixed
        If positive integer, the 3D sequence will be cut between coordinates
        y1 and y2, in height. Image origin (0, 0) is at the top-left corner.
        If y1 of y2 are None, respectively the beginning or end will not be cut.
        This parameter is only used for multi-track image display and video
        creation.
        
    x1, x2 : mixed
        If positive integer, the 3D sequence will be cut between coordinates
        x1 and x2, in width.
        If x1 of x2 are None, respectively the beginning or end will not be cut.
        This parameter is only used for multi-track image display and video
        creation.
        
    plotImageInTracking : bool
        If True, each 2D image is shown on screen during the tracking process.
        
    timePerImage : mixed
        Time for which each 2D image is shown on screen.
        If 'auto', it is automatically calculated from the meta-data in
        ``img``. If not available here, an exception will thrown.
        If float, it must be indicated in milliseconds.
        If ``plotImageInTracking`` is False, this parameter is ignored.
        
    plotTrackedFeatures : bool
        If True, plot the result of each tracker with a circle and the number
        of the tracker (starting from 0). Trackers order follow the order in
        ``trackersPars``.
        
    outFiles : list
        List of tuples, where each tuple represents an output video to be saved.
        The first element is the full path of the file to be saved. Supported
        formats: avi (Microsoft Video 1 (MSVC) codec).
        The second element is the frame rate. If 'auto', the frame rate of the
        input file. Otherwise, it must be a float number.
        The video contains data as shown with ``plotTrackedFeatures`` set to 
        true, the original raw sequence otherwise.
        

    Returns
    -------
    tuple
        cx, cy, horizontal and vertical position of the MTJ. Values are relative
        to the (0, 0) image corner. These Numpy tables vectors contain as many 
        rows as the number of time frames in the original input image, and as
        many columns as the number of trackers. Columns orders follows the 
        order of ``trackersPars``. Frames outside the range (f1, f2) are set as
        np.nan.

        
    """

    # Read sequence
    I, metadata = readImage(img, reader='sitk')
            
    # Get time per image
    frame_rate = metadata['frame_rate']
    if timePerImage == 'auto':
        if frame_rate is not None:
            timePerImage = int(1000. / frame_rate)
        else:
            raise Exception('timePerImage cannot be calculated automatically')
            
    # Loop for different trackers
    Nfr = I.shape[0]
    cxRes = np.zeros((Nfr,trackersN)) * np.nan
    cyRes = cxRes.copy()
    for i in xrange(trackersN):
        # Assemble parameter for tracker
        if trackersPars is None:
            trackerPars = {}
        else:
            trackerPars = trackersPars[i]
        # Run tracker
        print 'Running tracker %d ...' % i
        cx, cy = trackMTJ([I, metadata], **trackerPars)
        print 'Tracker %d terminated' % i
        # Set results
        cxRes[:,i] = cx
        cyRes[:,i] = cy
        
    # Set sequence boundaries
    if f1 is None:
        f1 = 0
    if f2 is None:
        f2 = I.shape[0]
    if y1 is None:
        y1 = 0
    if y2 is None:
        y2 = I.shape[1]
    if x1 is None:
        x1 = 0
    if x2 is None:
        x2 = I.shape[2]
        
    # Show image

    if plotImageInTracking:  
        
        for fr in xrange(f1, f2):
            
            # Get current image
            image = I[fr,:,:]    
            
            if plotTrackedFeatures:        
            
                # Write data to image
                for i in xrange(trackersN):
                    cx = int(cxRes[fr,i])
                    cy = int(cyRes[fr,i])
                    # Write tracker circle
                    image2 = cv2.circle(image, (cx,cy), 5, 255, 1)
                    if image2 is not None:
                        image = image2
                    # Write tracker number
                    image2 = cv2.putText(image, '%d' % i, (cx,cy-7), cv2.FONT_HERSHEY_SIMPLEX, 0.4, 255)
                    if image2 is not None:
                        image = image2
                I[fr,:,:] = image
            
            # Show image
            cv2.imshow('Trackers results',image[y1:y2,x1:x2])
            cv2.waitKey(int(timePerImage))
        
    # Crop image
    Iout = I[f1:f2,y1:y2,x1:x2]
    
    # Export files
    for outFile in outFiles:
        file_name = outFile[0]
        fps = outFile[1]
        if fps == 'auto':
            fps = frame_rate
        arr2seqFile(file_name, Iout, fps)
    
    return cxRes, cyRes
                 

                 
                 
                 
                 
                 
                 