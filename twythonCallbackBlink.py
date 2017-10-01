from twython import Twython
from twython import TwythonStreamer
twitter = Twython()

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

C_KEY = "1XYEbHDiBoD5iHiw2LK70ZE5U"
C_SECRET = "6mCfasKF4iNNrY4j60nm9Enlq7Ggb4AVs9xPloJT8xrEVUTgDy"
A_TOKEN = "88620543-fPtczMK8OUVVek684JaNVR6SMsjDGbvvBS7VIymBO"
A_SECRET = "0twTxMWtoK6DF6d4TC4tdOrRPnArTjM4IcOHrkbeoHgX0"

#   Define a new class which extends TwythonStreamer
class MyStreamer(TwythonStreamer):
    #Callback called on_success()
    def on_success(self, data):
        if 'text' in data:
            blink()


    def on_error(self, status_code, data):
        print status_code
        self.disconnect()
        # Error 420 is you've reached your limit. Super sux. Did hardly any

def blink():
    GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(13, GPIO.LOW)

        
stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track="rain")


