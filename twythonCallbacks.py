#   Define a new class which extends TwythonStreamer
class MyStreamer(TwythonStreamer):
    #Callback called on_success()
    def on_success(self, data):
        if 'text' in data:
            print("Found it!")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track="Harris")
