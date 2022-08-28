import numpy as np
from gpiozero import LED
from random import choice
from time import sleep

yellow = LED(25)
yellow1 = LED(23)

yellow.off()
yellow1.off()
x = list(np.arange(.01, 4.8, .25))

wait_time = []
leds = [yellow, yellow1]
first_led = choice([yellow, yellow1])


first = first_led
leds.remove(first)

second = leds[0]

for num in x:
    wait = (.1*(1/(.5 **num)))
    wait_time.append(wait)

def game(wait_time, first, second):
    """Game with the lights"""
    first.off()
    second.off()
    sel = 0
    add = 1
    while True:
        first.on()
        sleep(wait_time[sel])
        first.off()
        sel = sel + add
        second.on()
        sleep(wait_time[sel])
        second.off()
        sel = sel + add

        if sel > 11:
            add = 2
        if sel > 17:
            second.off()
            first.blink()
            sleep(7)
            first.off()
            break

game_1 = game(wait_time, first, second)