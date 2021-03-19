import argparse
import numpy as np
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="your image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))

resized_width = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)
cv2.imshow("resized image with width", resized_width)

r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)
resized_height = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)
cv2.imshow("resized image by height", resized_height)

resized_height_width = imutils.resize(image, height=image.shape[0]*2,width=image.shape[1]*2, inter=cv2.INTER_CUBIC)
(b,g,r) = resized_height_width[367,170]
print(r,g,b)
cv2.imshow("resized using imutils", resized_height_width)
cv2.waitKey()
