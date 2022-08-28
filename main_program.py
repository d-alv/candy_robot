from robot_movement import Movement
from light_sensor import LightSense
stopm = Movement._stop_()

from pynput.keyboard import Key, Listener

class MainClass:
    """Main class to run the programs"""
    def __init__(self):
        self.movement = Movement()
        self.ls = LightSense()
        self.honest = True

    def run_program(self):
        """function to run the program"""

        while self.honest:
            self.listen()

    def listen(self):
         # initialize the listener
        with Listener(
                on_press = self.on_press,
                on_release = self.on_release) as listener:
            # collect events until released
            listener.join()

    def _key_down(self, key):
        """Set movement flags to true"""

        if key == Key.up:
            self.movement.move_forward = True
        elif key == Key.down:
            self.movement.move_backwards = True
        elif key == Key.left:
            self.movement.move_left = True
        elif key == Key.right:
            self.movement.move_right = True
        try:
            if key.char == 'r':
                spin = self.ls.game()
                if spin == 'a':
                    self.movement.candy()
                else:
                    self.movement.candy1()
                
                    
            elif key.char == 'a':
                self.movement.candy()
            elif key.char == 'b':
                self.movement.candy1()
        except AttributeError:
            pass

        self.movement.update()

    def _key_up(self, key):
        """
        Set movement flags to false when released.
        """
        if key == Key.up:
            self.movement.move_forward = False
        elif key == Key.down:
            self.movement.move_backwards = False
        elif key == Key.left:
            self.movement.move_left = False
        elif key == Key.right:
            self.movement.move_right = False

        self.movement.update()


    def on_press(self, key):
        """recognize pressed keys"""
        print('{0} pressed'.format(key))
        self.ls.check_sensor()

        self._key_down(key)

    def on_release(self, key):
        """recognize pressed keys"""
        print('{0} released'.format(key))
        self._key_up(key)
        if key == Key.esc:

            # set flag 'honest'
            self.honest = False
            # end with return false
            return False


if __name__ == "__main__":
    mc = MainClass()
    mc.run_program()