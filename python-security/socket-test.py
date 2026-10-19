import socket
target = "192.168.56.104"
ports= range(1,1025)
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target,port))
    if result ==0:
       print(f"Port {port} is open")
    #else:
        #print(f"Port {port} is closed")
    sock.close()
