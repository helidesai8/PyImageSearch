import cv2

image = cv2.imread("florida_trip.png")
cv2.imshow("original image",image)
face = image[124:212, 225:380]
cv2.imshow("Face crop",face)
cv2.waitKey()
