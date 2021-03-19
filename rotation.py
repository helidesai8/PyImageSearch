import numpy as np
import argparse
import imutils
import cv2
# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(h,w)=image.shape[:2]
(cX,cY)=(50,50)

M=cv2.getRotationMatrix2D((cX,cY),88,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated 45 Degrees",rotated)
cv2.waitKey(0)
'''
rotated = imutils.rotate(image, 110)
cv2.imshow("Rotated by 180 Degrees", rotated)
'''
(b,g,r)=rotated[10,10]
print(r,g,b)
cv2.waitKey(0)