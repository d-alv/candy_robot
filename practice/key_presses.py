from pynput.keyboard import Key, Listener
from robot_movement import Movement

class KeyPress:
    """Class for key presses"""
    
    def __init__(self):
        self.keys = Key()
        self.listener = Listener()
        self.movement = Movement()
        
        self.key_listener = self.listener(on_press=self.on_press,
                on_release=self.on_release)
            
    def on_press(self, key):
        print('{0} pressed'.format(key))
  
    
    def on_release(self, key):
        print('{0} release'.format(key))
    
        if key == Key.esc:
            # stop listener
            return False
        
   


  
    
    
            

            
