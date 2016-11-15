#!/usr/bin/python
# import packages
from tempimage import TempImage
from picamera.array import PiRGBArray
from picamera import PiCamera
import warnings
import datetime
import imutils
import time
import cv2
import visualAlert 
import TCP


#variables
ipAddress = "170.140.153.111"

# filter warnings
warnings.filterwarnings("ignore")

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = tuple([640, 480])
camera.framerate = 5
rawCapture = PiRGBArray(camera, size=tuple([640, 480]))
 
# allow the camera to warmup, then initialize the average frame,and frame motion counter
time.sleep(2.5)
avg = None
alertcount = 0


# capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image and initialize
	# the occupied/unoccupied text
	frame = f.array
	text = "Unoccupied"
	time.sleep(0.1) #have the script pause between loops

	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
	# if the average frame is None, initialize it
	if avg is None: 
		avg = gray.copy().astype("float")
		rawCapture.truncate(0)
		continue
 
	# accumulate the weighted average between the current frame and
	# previous frames, then compute the difference between the current
	# frame and running average
	cv2.accumulateWeighted(gray, avg, 0.5)
	frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
	# threshold the delta image, dilate the thresholded image to fill
	# in holes, then find contours on thresholded image
	thresh = cv2.threshold(frameDelta, 5, 255, 
		cv2.THRESH_BINARY)[1] #second argument is delta thresh, change for false positives.
	thresh = cv2.dilate(thresh, None, iterations=2)
	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
 
	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < 5000: #this is the minimum area of perturbation. Modify this in case of false positives, negatives.
			continue
 
		# update the text
		text = "Occupied"

		# check to see if the room is occupied
	if text == "Occupied":
		if alertcount <40: #increment the alertcount
			alertcount = alertcount +2
		if alertcount == 4: #if there have been 2 alertcounts, make alert.
			TCP.send( b"O1", ipAddress)
			visualAlert.blink()

	# otherwise, the room is not occupied
	elif alertcount > 0:
		alertcount -= 1
	
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
