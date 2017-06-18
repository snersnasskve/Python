##	Use putty to open two separate windows on pi

## on the server side use 
##		nc -l 1234   ## netcap listen on port 1234

##	This is the client side
##	createbindcocket.py
import socket

## AF_INET = communicate on internet - always use this
## SOCK_STREAM = TCP connection - more reliable, use this not UDP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	## Loopback address = 127.0.0.1

##	127.0.0.1 = loopback address port 1234
##	 socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])
ainfo = socket.getaddrinfo("127.0.0.1", 1234)
print(ainfo)
## This shows a list of three fivetuples of which the fifth (of the 5) is the ip & port
print(ainfo[0][4])
##	This is the address we want to connect to
mysock.connect(ainfo[0][4])
##	Need to send data, not strings
mysock.sendall(b"Hello raspo")
##	Do'nt forget to close
mysock.close()
