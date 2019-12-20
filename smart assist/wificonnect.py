import socket
 
s = socket.socket()         
 
s.bind(('127.0.0.1', 8090 ))
s.listen(0)                 
 
while True:
 
    client, addr = s.accept()
    