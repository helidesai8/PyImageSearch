import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original image", image)

KernelSizes = [(3, 3), (5, 5), (9, 9), (15, 15)]
for (Kx, Ky) in KernelSizes:
    blurred = cv2.blur(image, (Kx, Ky))
    cv2.imshow("Image {} {}".format(Kx, Ky), blurred)
    cv2.waitKey()
for (Kx, Ky) in KernelSizes:
    blurred = cv2.GaussianBlur(image, (Kx, Ky), 0)
    cv2.imshow("Gaussian Blur Image {} {}".format(Kx, Ky), blurred)
    cv2.waitKey()

for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)
    cv2.waitKey()

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)
