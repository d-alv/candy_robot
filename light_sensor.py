from gpiozero import LightSensor, LED
import numpy as np
from random import choice
from time import sleep


class LightSense:
    """A class to call light and check sensors"""

    def __init__(self):
        """Initialize the light and sensors + movement"""
        # lights and sensors
        self.ldr = LightSensor(18)
        self.ldr1 = LightSensor(26)
        self.yellow1 = LED(25)
        self.yellow = LED(23)

        # defined variables for the light game
        self.sleep = sleep
        self.np = np
        self.choice = choice
        self.wait_time = []
        
        # define candy method
        
        

    def check_sensor(self):
        """Check the status of the photocell."""
        
        print(f"light sensor 1 has a reading of {self.ldr.value}")
        print(f"light sensor 2 has a reading of {self.ldr1.value}")
        if self.ldr.value >= .2:
            print("woah that's bright!")
            self.yellow.on()
        else:
            self.yellow.off()
            
        if self.ldr1.value >= .2:
            print("woah that's bright!")
            self.yellow1.on()
        else:
            self.yellow1.off()


    def _game_math(self):
        """Helper method for exponential eq."""
        x = list(self.np.arange(.01, 4.8, .25))
        for num in x:
            wait = (.1*(1/(.5 **num)))
            self.wait_time.append(wait)


    def _random_pick(self):
        """Random led picker for game"""
        leds = [self.yellow, self.yellow1]
        self.first = self.choice(leds)

        leds.remove(self.first)
        self.second = leds[0]

    def game(self):
        """Game with the lights"""
        self._game_math()
        self._random_pick()
        sel = 0
        add = 1

        self.first.off(), self.second.off()
        self.sleep(2)

        while True:
            self.first.on()
            self.sleep(self.wait_time[sel])
            self.first.off()
            sel = sel + add
            self.second.on()
            self.sleep(self.wait_time[sel])
            self.second.off()
            sel = sel + add

            if sel > 11:
                add = 2
            if sel > 17:
                self.second.off()
                self.first.blink()
                self.sleep(4)
                
                if self.first == self.yellow:
                    spin = 'a'
                else:
                    spin = 'b'
                    
                self.first.off()
                return spin
                break