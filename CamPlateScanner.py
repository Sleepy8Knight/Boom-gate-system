from PIL import Image
import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;	
import time

cam = cv2.VideoCapture(0)

def timeToString(specificTime):
    currentTime = time.localtime(specificTime)
    return f"{currentTime[2]}/{currentTime[1]}/{currentTime[0]}:{currentTime[3]}:{currentTime[4]}:{currentTime[5]}"


while True:

    check, frame = cam.read()
    img = cv2.resize(frame,(320,240))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_empty = np.zeros((img.shape[0], img.shape[1]))
    img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)
    img3 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]
    img4 = cv2.GaussianBlur(img3, (3, 3), 0)

    text = pytesseract.image_to_string(img4)

    # Output

    cv2.imshow("Original", img)

    #cv2.imshow("Normalized", img2)

    cv2.imshow("Threshold", img3)

    cv2.imshow("Blurred", img4)

    print(text, mytime)

    #print(time.time())
    #print(time.localtime(time.time()))
    mytime = str(timeToString(time.time()))
    #print(mytime)
    file = open("camReadTime.txt", "w")
    file.write(mytime)

    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

cam.release()

cv2.destroyAllWindows()
