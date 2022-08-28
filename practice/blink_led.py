import gpiozero
import time

led = gpiozero.LED(5)

while True:
    led.on()
    time.sleep(.5)
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(1)
    led.off()