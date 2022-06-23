
import os

shutter = input("Sure you wanna shutdown your PC? (y/n): ").lower()

if shutter == 'n':
	exit()
else:
	os.system("shutdown P/p/r")