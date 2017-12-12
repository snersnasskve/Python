import picamera
camera = picamera.PiCamera()

# Take a picture
camera.capture("pict.jpg")

# Take a picture
camera.capture("pict.jpg")

# horizontal flip
camera.hflip = True

# vertical flip
camera.vflip = True

camera.brightness = 50 # 0 to 100
camera.sharpness = 0

# video
# doesn't save = straight to screen
camera.start_preview()
camera.stop_preview()

import picamera
import time
camera.start_recording("vid.h264")
time.sleep(10)
camera.stop_recording()