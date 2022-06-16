import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",8080))

msg = client.recv(1024)
print(msg.decode("utf-8"))