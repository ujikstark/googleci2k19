## Created By Ujikstark

#!/usr/bin/env python3
import socket
from termcolor import colored
 
host = input("Enter your ip: ")
strip = '-'*40

def scanner(host, port):
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((host, port))
			
	except:
		return False
	
	else:
		return True
			
for port in range(1,91):
	if scanner(host, port):
		print(colored(f"Port {port} is open","blue"))
		print(colored(f"{strip}\nDetail Information\n{strip}","green"))
		if port == 80:	
			get = sock.sendall(b'GET / HTTP/1.0\r\n\r\n')
			result = sock.recv(132)
			result_list = result.decode('utf-8')
			print(colored(result_list + strip, "green"))

	else:
		print("Port", port, "is closed")


	
