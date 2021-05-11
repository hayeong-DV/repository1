from socket import *
import threading

port = 2500
address = ('localhost', port)
BUFFSIZE = 1024

def recvTask(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(address)

my_id = input('ID를 입력하세요: ')
sock.send(('['+my_id+']').encode())

th = threading.Thread(target=recvTask, args=(sock,))
th.start()

while True:
    msg = '['+ my_id + ']' + input()
    sock.send(msg.encode())

  
