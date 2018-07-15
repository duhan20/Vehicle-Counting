import numpy as np
import cv2

cap = cv2.VideoCapture('traf.mp4') #Open video file

while(cap.isOpened()):
    ret, frame = cap.read() #read a frame
    try:        
        cv2.imshow('Frame',frame)
        frame2 = frame
    except:
        #if there are no more frames to show...
        print('EOF')
        break

    line1 = np.array([[100,100],[300,100],[350,200]], np.int32).reshape((-1,1,2))
    line2 = np.array([[400,50],[450,300]], np.int32).reshape((-1,1,2))

    frame2 = cv2.polylines(frame2,[line1],False,(255,0,0),thickness=2)
    frame2 = cv2.polylines(frame2,[line2],False,(0,0,255),thickness=1)
    
    cv2.imshow('Frame 2',frame2)
    
    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows