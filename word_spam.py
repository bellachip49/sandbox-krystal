#Author: Krystal Kwan
#Date: 11/28/20
#Description: Spreading my Itto propaganda

import time
import threading
from pynput.keyboard import Key, Controller

delay = 1
button = Button.left
start_stop_key = KeyCode(char='s') #start
exit_key = KeyCode(char='e') #exit

def on_press(key):
    if key == start_stop_key:
        keyboard.type('Itto')
        keyboard.press('enter')
        time.sleep(5)
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
  listener.join()
