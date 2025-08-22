import socket

# Create Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# BInd IP with Host
ip = "127.0.0.1"
host = 12345

server.bind((ip, host))

# Start Listening
server.listen(1)
print("Server ready, waiting for client...")

# Accept client connection

conn, addr = server.accept()
print(f"Connected to {addr}")

# Chat Loop
while True:
    data = conn.recv(1024).decode()
    print(f"Client : {data}")

    if not data:
        break

    reply = input("Server : ")
    conn.send(reply.encode())

conn.close()
