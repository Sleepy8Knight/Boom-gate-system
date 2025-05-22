from PIL import Image
import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;	
import time
from gpiozero import DistanceSensor
from time import sleep
from RPLCD.i2c import CharLCD
from gpiozero import Servo
import re
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

passage = False
car = False

servo = Servo(17)
servo.min()


lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)

ultrasonic = DistanceSensor(echo=12, trigger=23) 


cam = cv2.VideoCapture(0)

def timeToString(specificTime):
    currentTime = time.localtime(specificTime)
    return f"{currentTime[2]}/{currentTime[1]}/{currentTime[0]}:{currentTime[3]}:{currentTime[4]}"

# dissen = ultrasonic.distance * 100




while True:

    dissen = ultrasonic.distance * 100
    #print(dissen)


    if passage == True:
        if car == True:
            servo.max()


        


        if dissen < 8:
            car = True
        
        if car == True:
          if dissen > 8:
             servo.min()
             car = False




    id, money = reader.read()
    #print(id)
    print(money)




    check, frame = cam.read()
    img = cv2.resize(frame,(320,240))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    img_empty = np.zeros((img.shape[0], img.shape[1]))

    img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)

    img3 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

    img4 = cv2.GaussianBlur(img3, (3, 3), 0)

    text = pytesseract.image_to_string(img4)

    
    clean_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    print(clean_text)



    # Output

    cv2.imshow("Original", img)

    #cv2.imshow("Normalized", img2)

    cv2.imshow("Threshold", img3)

    cv2.imshow("Blurred", img4)

    #print(text)


    mytime = str(timeToString(time.time()))
    #print(mytime)
    file = open("camReadTime.txt", "w")
    file.write(mytime)


    lcd.clear()

    lcd.write_string('you owe: ')
    lcd.write_string('$10')
    lcd.crlf()
    lcd.write_string(mytime)

    if print(clean_text):
        passage = True
        print('true')


    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

#print(time.time())
    #print(time.localtime(time.time()))





cam.release()

cv2.destroyAllWindows()