import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

outputState = False

while True:
    GPIO.output(13, outputState);
    outputState = not(outputState)
    time.sleep(1)
