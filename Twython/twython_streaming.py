

#extension of TwythonStreamer
class MyStreamer(TwythonStreamer):
    #on_success is a callback
    #called when a tweet is found matching your search criteria
    #data is a dictionary
    def on_success(self, data):
        #there is a key in data called text
        if 'text' in data:
            print("Found it!")
            
        
    
