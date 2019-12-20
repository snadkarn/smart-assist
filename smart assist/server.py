#import socket
#
#
#TCP_IP = ' 192.168.43.248'
#TCP_PORT = 5005
#BUFFER_SIZE = 20  # Normally 1024, but we want fast response
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
#s.listen(1)
#
#conn, addr = s.accept()
#print ('Connection address:', addr)
#while 1:
#    data = conn.recv(BUFFER_SIZE)
#    if not data: break
#    print ("received data:", data)
#    conn.send(data)  # echo
#conn.close()
import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host_name = socket.gethostname() 
#host_ip = socket.gethostbyname(host_name)      
ip='192.168.43.248'  #Note the extra letters "by"
                  

port = 9999                                           
addr=(ip,port)
# bind to the port
serversocket.bind(addr)                                  

# queue up to 5 requests
serversocket.listen(1) 
print('strated listening')                                          

while True:
   # establish a connection
   clientsocket,addr1 = serversocket.accept()      

   print("Got a connection from %s" % str(addr1))
    
   msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()