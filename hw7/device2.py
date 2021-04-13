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
    elif msg == "2":
        heart =  random.randint(40,140)  
        steps = random.randint(2000,6000)  
        cal = random.randint(1000,4000)  
        msg = "Device2: Heartbeat={}, Steps={}, Cal={}".format(heart, steps, cal)
        s.send(msg.encode())     
        
s.close()      
      

