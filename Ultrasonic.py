from gpiozero import DistanceSensor
from time import sleep

ultrasonic = DistanceSensor(echo=12, trigger=23) 


while True:
    print(ultrasonic.distance)
    sleep(1)
    dissen = ultrasonic.distance * 100
    print(dissen)
    sleep(1)