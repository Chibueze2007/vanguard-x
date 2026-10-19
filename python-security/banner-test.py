import socket

target = "192.168.56.104"
ports = range(20,8181)

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    result = sock.connect_ex((target, port))

    if result == 0:
        try:
            data = sock.recv(1024)
            print(f"Port {port}: Open: {data.decode(errors='replace')}")
        except socket.timeout:
            print(f"Port {port}: No banner received")
    sock.close()



