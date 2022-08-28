import gpiozero
from time import sleep

class Movement:
    """class for the robot's movements"""
    
    def __init__(self):
        """define robot movements"""
        
        self.sleep = sleep
        # driving motors
        self.robot = gpiozero.Robot(right = (4, 17), left = (27, 22))
        
        # candy motors
        self.motor = gpiozero.Motor(16, 20)
        self.motor1 = gpiozero.Motor(7, 24)
        
        # movement flags
        self.move_forward = False
        self.move_left = False
        self.move_right = False
        self.move_backwards = False
        
        self.arrows = [
            self.move_forward,
            self.move_left,
            self.move_right,
            self.move_backwards,
                       ]
        self.on = []
        
        # create adjustable time variable
        self.t = .6
        
    def _stop_():
        """ This will stop the robot before crash"""
        robot = gpiozero.Robot(right = (4, 17), left = (27, 22))
        robot.stop()
        motor2 = gpiozero.Motor(16, 20)
        motor3 = gpiozero.Motor(7, 24)
        motor2.stop()
        motor3.stop()
        
    def update(self):
        """
        If the flags are true, the motors will turn on.
        """
        self._check_status()
        if self.move_forward:
            self.robot.forward()
        if self.move_left:
            self.robot.left()
        if self.move_right:
            self.robot.right()
        if self.move_backwards:
            self.robot.backward()
        
        
        
    def _check_status(self):
        """checks if all the motors are false"""
        for item in self.arrows:
            if item == True:
                self.on.append(item)
                
        for value in self.on:
            if value == False:
                del self.on[0]
                       
        while True:
            if len(self.on) == 0:
                self.robot.stop()
                break
    
    def candy(self):
        """Controls motors to dispense candy #1"""
        self.motor.forward()
        self.sleep(self.t+.07)
        self.motor.stop()
            
    def candy1(self):
        """controls motors to dispense candy #2"""
        self.motor1.forward()
        self.sleep(self.t)
        self.motor1.stop()