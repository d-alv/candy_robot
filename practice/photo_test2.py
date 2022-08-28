from gpiozero import LightSensor, RGBLED
from time import sleep

ldr = LightSensor(18)
led = RGBLED(red=6, green=26, blue=5)
led.red = 1
sleep(1)
led.red = .5
sleep(1)



while True:
    led.color = (1,1,1)
    print(ldr.value)
    if ldr.value > .2:
        print("Woah that's bright")
    