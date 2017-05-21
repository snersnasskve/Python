
def setLedState(outputState):
    GPIO.output(13, outputState);
    time.sleep(1)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

outputState = False

inputpin = 7

GPIO.setup(inputpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

while True:
    if GPIO.input(inputpin):
        outputState = 1
        print ("On all the time")
    else:
        outputState = not(outputState)
        print ("Blinking")
    setLedState(outputState)

        
