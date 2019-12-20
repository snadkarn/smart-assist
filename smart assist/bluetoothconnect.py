
import socket
import time

##hostMACAddress = '98:d3:51:f5:bb:6d' # The MAC     address of a Bluetooth adapter on the server
hostMACAddress = 'FC:A8:9A:00:3C:A6'
port = 1 
size = 1024
s=socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
s.connect((hostMACAddress,port))
s.send("a".encode())
time.sleep(5)
s.send("d".encode())
s.close()

