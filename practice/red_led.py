from gpiozero import LED
import time

red_led = LED(25)
red_led.on()
time.sleep(5)