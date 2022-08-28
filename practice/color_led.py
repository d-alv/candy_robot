from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=6, green=26, blue=5)
led.red = 1
sleep(6)
led.green = 1
sleep(6)
led.blue = 1
sleep(6)
led.color = (1,0,1)
sleep(6)
led.color = (0,1,1)
sleep(6)
led.color = (1,1,0)
sleep(6)


while True:
    led.color = (1,1,1)
