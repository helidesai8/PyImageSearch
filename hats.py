import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

rectkernel= cv2.getStructuringElement(cv2.MORPH_RECT,(13,5))
blackhat = cv2.morphologyEx(gray,cv2.MORPH_BLACKHAT,rectkernel)

tophat = cv2.morphologyEx(gray,cv2.MORPH_TOPHAT,rectkernel)

cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey()
