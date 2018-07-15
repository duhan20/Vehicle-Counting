import numpy as np
import cv2

cap = cv2.VideoCapture('traf.mp4') #Open video file

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True) #Create the background substractor

while(cap.isOpened()):
    ret, frame = cap.read() #read a frame
    
    fgmask = fgbg.apply(frame) #Use the substractor
    
    try:        
        cv2.imshow('Frame',frame)
        cv2.imshow('Background Substraction',fgmask)
    except:
        #if there are no more frames to show...
        print('EOF')
        break
    
    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows