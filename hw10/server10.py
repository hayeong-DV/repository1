from socket import *
import threading
import time

port = 3333
BUFFSIZE = 1024
clients=[]

def checkTask(conn):
    while True:
        msg = conn.recv(BUFFSIZE)
        if not msg:
            break

        elif 'quit' in msg.decode():
            if conn in clients:
                print(conn, 'exited')
                clients.remove(conn)

        for client in clients:
            if client != conn:
                client.send(msg) 
        print(time.asctime() + str(addr) + ':' + msg.decode())
       
  
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(4)

print('Server Started')
          
while True:
    conn, addr = sock.accept()

    th = threading.Thread(target=checkTask, args=(conn,))
    th.start()

    if addr not in clients:
        print('new client', addr)
        clients.append(conn)

    




