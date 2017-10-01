from twython import Twython
from twython import TwythonStreamer
twitter = Twython()

C_KEY = "1XYEbHDiBoD5iHiw2LK70ZE5U"
C_SECRET = "6mCfasKF4iNNrY4j60nm9Enlq7Ggb4AVs9xPloJT8xrEVUTgDy"
A_TOKEN = "88620543-fPtczMK8OUVVek684JaNVR6SMsjDGbvvBS7VIymBO"
A_SECRET = "0twTxMWtoK6DF6d4TC4tdOrRPnArTjM4IcOHrkbeoHgX0"

#   Define a new class which extends TwythonStreamer
class MyStreamer(TwythonStreamer):
    #Callback called on_success()
    def on_success(self, data):
        if 'text' in data:
            print("Found it!")


stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track="Harris")
