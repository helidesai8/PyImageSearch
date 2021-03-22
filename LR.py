import argparse
import cv2
from pyzbar import pyzbar

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

barcodes = pyzbar.decode(image)


for barcode in barcodes:
    (x,y,w,h) = barcode.rect
    cv2.rectangle(image,(x,y+20),(x+200,y),(0,0,200),2)
    barcodeData = barcode.data.decode("utf-8")
    code = "{}".format(barcodeData)
    cv2.putText(image,code,(x+200,y),cv2.FONT_HERSHEY_PLAIN,2,(0,0,200),2)
    print(barcode)

cv2.imshow("Image", image)
cv2.waitKey()