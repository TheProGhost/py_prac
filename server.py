import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1" , 8080))

server.listen(5)

while True:
    clt, addr = server.accept()
    print(f"Connection to {addr}")
    clt.send(bytes("Hello Client", "utf-8"))