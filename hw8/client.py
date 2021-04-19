from socket import *

BUFFSIZE = 1024
port = 2500

c = socket(AF_INET, SOCK_DGRAM)
c.connect(('localhost', port))

while True:
    request = input('send or receive +num +string: ')
    if request == "quit":
        c.send(request.encode())
        break

    c.send(request.encode())
    recv = c.recv(BUFFSIZE)
    data = recv.decode()

    print(data)

c.close()