import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##	Arbitrary port
try:
	mysock.bind("", 1234)
except socket.error:
	print("Failed to bind")
	sys.exit()

mysock.listen(5)

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
