import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# BInd IP with Host
ip = "127.0.0.1"
host = 12345

client.connect((ip, host))
print("Client connected to Server")

while True:
    msg = input("Client : ")
    client.send(msg.encode())

    data = client.recv(1024).decode()
    print(f"Server : {data}")