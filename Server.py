import socket, threading
ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssocket.bind(("192.168.0.168", 5000))
ssocket.listen(1)
clients = {}
client, address = ssocket.accept()
while True:
            clients[client] = address
            message = input("Message for client> ")
            client.send(f'{message}'.encode('utf-8'))
            client.setblocking(False)
