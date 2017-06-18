import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

outpin = 7

GPIO.setup(outputpin, GPIO.OUT)

flipflop = True

while True:
	if flipflop:
		flipflop = False
		GPIO.output(outputpin, GPIO.HIGH)
		print("light on")
	else:
		flipflop = True
		GPIO.output(outputpin, GPIO.LOW)
		print("light off")
