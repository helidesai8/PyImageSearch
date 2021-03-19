import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask,(90,100),(290,450),255,-1)
cv2.imshow("mask",mask)

masked = cv2.bitwise_or( image,image,mask=mask )
cv2.imshow("masked rectangle",masked)

mask = np.zeros(image.shape[:2],dtype="uint8")
cv2.circle(mask,(145,200),100,255,-1)
masked = cv2.bitwise_or(image,image,mask=mask)

cv2.imshow("masked circle",masked)

cv2.waitKey()