from PIL import Image
import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;

#Find the execution path and join it with the direct reference
def execution_path(filename):
  return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), filename)			

filename = execution_path("3_python-ocr.jpg")
image = cv2.imread(filename)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("otsu", thresh)


img = np.array(Image.open(filename))


img_empty = np.zeros((img.shape[0], img.shape[1]))

img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)
img3 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)[1]
img4 = cv2.GaussianBlur(img3, (1, 1), 0)

text = pytesseract.image_to_string(img4)

cv2.imshow("Original", img)

#cv2.imshow("Normalized", img2)

#cv2.imshow("Threshold", img3)

#cv2.imshow("Blurred", img4)

print(text)

cv2.waitKey(0)
