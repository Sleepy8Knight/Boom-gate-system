#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


#while True:
    #text = input('New data')
    #print('tag')
    #reader.write(text)
    #print('written')

    #break
#GPIO.cleanup()

while True:
    id, text = reader.read()
    print(id)
    print(text)

    break
GPIO.cleanup()