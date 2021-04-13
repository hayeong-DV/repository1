from socket import *
import time

port = 2500
BUFSIZE= 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(3)

c1, addr1 = s.accept()
c2, addr2 = s.accept()
print('Connection from ', addr1)
print('Connection from ', addr2)
while True:


    msg = input("Input 1 or 2: ")

    if msg == "quit":
        c1.send(msg.encode())
        c2.send(msg.encode())
        break

    elif msg == "1":
        c1.send(msg.encode())
        rev_data1 = c1.recv(BUFSIZE)
        if not rev_data1:
            break
        print(rev_data1.decode())
        f = open("data.txt", "a")
        t = time.strftime('%c', time.localtime(time.time()))
        rev_1 = rev_data1.decode()
        f.write("{0}:{1}\r\n".format(t, rev_1))
        f.close()


    elif msg == "2":
        c2.send(msg.encode())
        rev_data2 = c2.recv(BUFSIZE)
        if not rev_data2:
            break
        print(rev_data2.decode())
        f = open("data.txt", "a")
        t = time.strftime('%c', time.localtime(time.time()))
        rev_2 = rev_data2.decode()
        f.write("{0}:{1}\r\n".format(t, rev_2))
        f.close()
    continue

s.close()

