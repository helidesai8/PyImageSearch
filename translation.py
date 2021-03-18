import argparse
import numpy as np
import imutils
import cv2

#argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="for image name/path")
args = vars(ap.parse_args())

#load image and show
image = cv2.imread(args["image"])
cv2.imshow("original",image)

M=np.float32([[1,0,25],[0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted down and right",shifted)

cv2.waitKey(0)
