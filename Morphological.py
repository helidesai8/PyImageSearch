import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image",gray)
kernelSizes = [(3,3),(5,5),(7,7)]


for i in range(0,3):
    eroded = cv2.erode(gray.copy(),None,iterations=i+1)
    cv2.imshow("Eroded {} time".format(i+1),eroded)
    cv2.waitKey()

cv2.destroyAllWindows()
cv2.imshow("original",gray)

for i in range(0,3):
    dilated = cv2.dilate(gray.copy(),None,iterations=i+1)
    cv2.imshow("Dilated {} time".format(i+1),dilated)
    cv2.waitKey()

cv2.destroyAllWindows()
cv2.imshow("original",gray)


for kernelsize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,kernelsize)
    opening = cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel)
    cv2.imshow("Opening {}, {}".format(kernelsize[0],kernelsize[1]),opening)
    cv2.waitKey()

cv2.destroyAllWindows()
cv2.imshow("Original",gray)

for kernelsize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,kernelsize)
    closing = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
    cv2.imshow("Closing {} {}".format(kernelsize[0],kernelsize[1]),closing)
    cv2.waitKey()

for kernelsize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,kernelsize)
    closing = cv2.morphologyEx(gray,cv2.MORPH_GRADIENT,kernel)
    cv2.imshow("Gradient {} {}".format(kernelsize[0],kernelsize[1]),closing)
    cv2.waitKey()