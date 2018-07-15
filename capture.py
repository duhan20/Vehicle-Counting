import cv2, time

#1. Create an object.Zero for external camera
video=cv2. VideoCapture(0)

#1. a variable
a=0

while True:
	a=a+1

	#3. Create frame object
	check,  frame = video.read()

	print(check)
	print(frame) # Reprsenting image

	#6. converting to grascale
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#4. shadow the frame
	cv2.imshow("Capturing", gray)


	#5. for press any key to out (milisecond)
	#cv2.waitKey(0)


	#7. for playing
	key=cv2.waitKey(1)
	
	if key==ord('q'):
		break
	
print (a)

#2. Shutdown the camera
video.release() 

cv2.destroyAllWindows
 