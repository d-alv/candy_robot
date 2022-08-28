import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

sides = input("How many sides?")
size = input("How big?")
full_turn=.97*4

for x range(0,sides):
    GPIO.output(7,True)
    GPIO.output(13,True)
    time.sleep(size)
    GPIO.output(7,False)
    GPIO.output(13,False)
    time.sleep(.5)
    GPIO.output(7,True)
    GPIO.output(15,True)
    time.sleep(full_turn/sides)
    GPIO.output(7,False)
    GPIO.output(15,False)

GPIO.cleanup()