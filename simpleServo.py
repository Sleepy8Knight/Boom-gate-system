from gpiozero import Servo
from time import sleep


servo = Servo(12)
servo.min()

while True:
    servo.min()
    Servo.off()
    sleep(5)
    servo.mid()
    sleep(5)
    servo.max()
    sleep(5)
