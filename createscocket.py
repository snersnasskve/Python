##	createscocket.py
import socket

## AF_INET = communicate on internet - always use this
## SOCK_STREAM = TCP connection - more reliable, use this not UDP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
