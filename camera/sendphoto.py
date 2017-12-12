import picamera
import socket
camera = picamera.PiCamera()

# What if you want to send to a remote site?
#   Home security system
# Capture and image, send it on a connection
mysocket = socket.socket()
mysocket.connect(('aserver', 8000))
# wb = permissions
# this makes conn look like a file to camera, but look like a connection to socket
conn = mysocket.makefile('wb')
camera.capture(conn, 'jpeg')

# take photos over time
# camera.capture_continuous()
# you can add {counter} or {timestamp}
camera = picamera.PiCamera()
for filename in
    camera.capture_continuous("picture{counter}.jpg"):
      time.sleep(300)   # 5 minute delay between images