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
    first.off(), second.off()
    first.on()
    sleep(wait_time[0])
    first.off()
    second.on()
    sleep(wait_time[1])
    second.off()
    first.on()
    sleep(wait_time[2])
    first.off()
    second.on()
    sleep(wait_time[3])
    second.off()
    first.on()
    sleep(wait_time[4])
    first.off()
    second.on()
    sleep(wait_time[5])
    second.off()
    first.on()
    sleep(wait_time[6])
    first.off()
    second.on()
    sleep(wait_time[7])
    second.off()
    first.on()
    sleep(wait_time[8])
    first.off()
    second.on()
    sleep(wait_time[9])
    second.off()
    first.on()
    sleep(wait_time[10])
    first.off()
    second.on()
    sleep(wait_time[11])
    second.off()
    first.on()
    sleep(wait_time[13])
    first.off()
    second.on()
    sleep(wait_time[15])
    second.off()
    first.on()
    sleep(wait_time[17])
    first.off()
    second.on()
    sleep(wait_time[18])
    second.off()
    first.blink()
    sleep(7)
    first.off()

game_1 = game(wait_time, first, second)