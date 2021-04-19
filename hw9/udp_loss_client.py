from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

c = socket(AF_INET, SOCK_DGRAM)
c.connect(('localhost', port))
print('connecnt')

while True:
    msg = input('-> ') 
    reqx = 0

    while reqx <= 3:
        reQx = str(reqx) + " " + msg
        c.sendto(reQx.encode(),('localhost', port))
        c.settimeout(2)
        
        try:
            data, addr = c.recvfrom(BUFF_SIZE)
            if data.decode() == "ack":
                break
        except timeout:
            reqx += 1
            continue
        else:
            break

    c.settimeout(None)
    while True:
        data, addr = c.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            c.sendto(b'ack', ('localhost', port))
            print('<-', data.decode())
            break

       
c.close()
