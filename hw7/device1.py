from socket import *
import random

BUFSIZE = 1024
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 2500))

while True:
    rec = s.recv(BUFSIZE)
    msg = rec.decode()

    if not msg:
        break
    elif msg =="quit":
        break
    elif msg == "1":
        temp =  random.randint(0,40)  
        humid = random.randint(0,100)  
        linum = random.randint(70,150)  
        msg = "Device1: Temp={}, Humid={}, linum={}".format(temp, humid, linum)
        s.send(msg.encode())     
        
s.close()      
      

