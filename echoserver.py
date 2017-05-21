##	createbindcocket.py
import socket

## AF_INET = communicate on internet - always use this
## SOCK_STREAM = TCP connection - more reliable, use this not UDP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##	Arbitrary port
mysock.bind("", 1234)
## Listen and accept
##	5 is backlog, the number of requests allowed to wait for service
mysock.listen(5)
## Returns a connection (for sending/receiving) and an address (IP, port)
## conn = connection
## addr = address, ip + port
conn, addr = mysock.accept()

##	echoserver.py
data = conn.recv(1000)
conn.sendall(data)
conn.close()
mysock.close()