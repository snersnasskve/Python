import socket

## AF_INET = communicate on internet - always use this
## SOCK_STREAM = TCP connection - more reliable, use this not UDP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	## Loopback address = 127.0.0.1

##	127.0.0.1 = loopback address port 1234
##	 socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])
ainfo = socket.getaddrinfo(None, 1234)
try:    
    mysock.bind(ainfo[-1][4])
except socket.error:
    print("Failed to bind")
    sys.exit()

mysock.listen(5)	## max 5 concurrent connections

while True:
	## Returns a connection (for sending/receiving) and an address (IP, port)
	## conn = connection
	## addr = address, ip + port
	conn, addr = mysock.accept()
	data = conn.recv(1000)
	if not data:
		break
	print("Got a request!")
conn.close()
mysock.close()
