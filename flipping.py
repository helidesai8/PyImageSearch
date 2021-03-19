import argparse
import cv2
import imutils
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="input image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("original image",image)

flipped_h = cv2.flip(image,1)
cv2.imshow("horizontal flip",flipped_h)



flipped_hv = cv2.flip(image,-1)
cv2.imshow("vertically and horizontally flip",flipped_hv)

rotated = imutils.rotate(flipped_h,45)


flipped_v = cv2.flip(rotated,0)
cv2.imshow("vertically flip",flipped_v)

(b,g,r) = flipped_v[189,441]
print(r,g,b)
cv2.waitKey()