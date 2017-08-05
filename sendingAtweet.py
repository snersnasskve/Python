# sudo apt-get update
# sudo apt-get install python-pip
# sudo pip install twython

# won't work on the mac for whatever


from twython import Twython
from requests_oauthlib import requests_oauthlib
twitter = Twython()

C_KEY = "1XYEbHDiBoD5iHiw2LK70ZE5U"
C_SECRET = "6mCfasKF4iNNrY4j60nm9Enlq7Ggb4AVs9xPloJT8xrEVUTgDy"
A_TOKEN = "88620543-fPtczMK8OUVVek684JaNVR6SMsjDGbvvBS7VIymBO"
A_SECRET = "0twTxMWtoK6DF6d4TC4tdOrRPnArTjM4IcOHrkbeoHgX0"

api = Twython(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

api.update_status("Python is cool - if this tweet arrives, that is!")
