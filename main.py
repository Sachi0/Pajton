import numpy as np
import cv2

camera = cv2.VideoCapture(0)

while True:
	ret, frame = camera.read(False)
	frame = cv2.flip(frame,1)
	

	cv2.imshow('image', frame)
	key = cv2.waitKey(1)
	if key == 27:
		break


cv2.destroyAllWindows()