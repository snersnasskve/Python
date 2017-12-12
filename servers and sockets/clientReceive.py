##	Use putty to open two separate windows on pi
#####afterthought - is this really client???
## on the server side use 
##		nc -l 1234   ## netcap listen on port 1234

##	This is the client side
##	createbindsocket.py
import socket

## AF_INET = communicate on internet - always use this
## SOCK_STREAM = TCP connection - more reliable, use this not UDP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	## Loopback address = 127.0.0.1

##	127.0.0.1 = loopback address port 1234
##	 socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])
ainfo = socket.getaddrinfo(None, 1234)
print(ainfo)
## This shows a list of three fivetuples of which the fifth (of the 5) is the ip & port
print(ainfo[-1][4])
##		You're looking for a tuple of two - ip and port
##	This is the address we want to connect to
mysock.bind(ainfo[-1][4])
mysock.listen(5)	## max 5 concurrent connections
conn, addr = mysock.accept()

## In the second window, call 
##		nc 127.0.0.1 1234
##		Hello raspo##	Do'nt forget to close

print(data)
conn.close()
mysock.close()
