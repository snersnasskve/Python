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
            print_recur(data)


    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

    def print_recur(py_item):
        for key, value in py_item.items():
            print key
            if type(value) == dict:
                print_recur(value)
            else:
                print value
        
stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track="Harris")


