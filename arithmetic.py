import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

Sum = cv2.add(np.uint8([1]), np.uint8([251]))
Sub = str(cv2.subtract(np.uint8([1]), np.uint8([251])))

print("Sum is : ", str(Sum))
print("Sub is: ",str(Sub))

Sum = (np.uint8([200]) + np.uint8([68]))
Sub = str(np.uint8([1]) - np.uint8([251]))

print("Sum is : ", str(Sum))
print("Sub is: ",str(Sub))

M = np.ones(image.shape, dtype = "uint8") * 75
added = cv2.add(image, M)
cv2.imshow("Added", added)

(b,g,r) = added[152,61]
print(r,g,b)

M = np.ones(image.shape, dtype = "uint8") * 100
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)