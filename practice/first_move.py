import gpiozero
import time
import pygame



robot = gpiozero.Robot(right = (4, 17), left = (27, 22))



for i in range(8):
    robot.forward()
    time.sleep(.5)
    robot.right()
    time.sleep(.25)
    
    
    
    
    
    
   