from pynput.keyboard import Key, Listener

class KeyReturns:
    
    def __init__(self):
        self.key = Key()
        self.listener = Listener()
        
    def on_press(key):
        print('{0} pressed'.format(key))
    
    def on_release(key):
        print('{0} release'.format(key))
        if key == Key.esc:
            # stop listener
            return False
    
    # collect events until released
    with Listener(
            on_press = on_press,
            on_release = on_release) as listener:
        listener.join()
        