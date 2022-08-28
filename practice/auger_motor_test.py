from gpiozero import Motor
from time import sleep

auger = Motor(16, 20)
auger1 = Motor(7, 24)


while True:
    auger.forward()




