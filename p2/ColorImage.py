import cv2
import numpy as np
import sys

image = cv2.imread(sys.argv[1])
cv2.namedWindow("Original image", cv2.WINDOW_NORMAL)
cv2.imshow("Original image", image)

[red,green,blue] = cv2.split(image)

RGBpixel = image[20,25]
print(RGBpixel)

cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.imshow("Blue", blue)


ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
y, cb, cr = cv2.split(ycrcb_image)

YCRCBpixel = ycrcb_image[20,25]
print(YCRCBpixel)

cv2.imshow("Y",   y)
cv2.imshow("Cb",  cb)
cv2.imshow("Cr",  cr)


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)

HSVpixel = hsv_image[20,25]
print(HSVpixel)

cv2.imshow("Hue", h)
cv2.imshow("Saturation", s)
cv2.imshow("Value", v)


cv2.waitKey(0)

cv2.imwrite("Red.png", red)
cv2.imwrite("Green.png", green)
cv2.imwrite("Blue.png", blue)
cv2.imwrite("Y.png", y)
cv2.imwrite("Cb.png", cb)
cv2.imwrite("Cr.png", cr)
cv2.imwrite("Hue.png", h)
cv2.imwrite("Saturation.png", s)
cv2.imwrite("Value.png", v)