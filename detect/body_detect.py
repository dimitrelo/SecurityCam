import cv2
import sys

if len(sys.argv) < 2:
	print "Improper Usage. Need photo File."
	sys.exit(0)


cascPath = "/home/pi/CV/opencv-2.4.10/data/haarcascades/"
alg = "haarcascade_mcs_upperbody.xml"

faceCascade = cv2.CascadeClassifier(cascPath + alg)

img = cv2.imread(sys.argv[1])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Faces Detected:", faces