import socket

port =2500
BUFFSIZE =1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
    
mboxID={}

while True:
    recvMSG, addr = sock.recvfrom(BUFFSIZE)
    msg = recvMSG.decode()

    if msg == "quit":
        break
    msg = msg.split(' ')

    if msg[0] == 'send':
        plusmsg = msg[2:]
        finalmsg =' '.join(plusmsg)

        if msg[1] in mboxID:
            mboxID[msg[1]] += [finalmsg]
            print(mboxID)
            sock.sendto(b'ok', addr)
            
        else:
            mboxID[msg[1]] = [finalmsg]
            print(mboxID)
            sock.sendto(b'ok', addr)

    elif msg[0] == "receive":
        if msg[1] in mboxID:
            word = mboxID.get([msg[1]][0])

            if word == []:
                sock.sendto(b'No Messages', addr)
            else:
                sendMSG = mboxID[msg[1]][0]
                sock.sendto(sendMSG.encode(),addr)
                del mboxID[msg[1]][0]
                print(mboxID)
        else:
            sock.sendto(b'No Messages', addr)


sock.close()    
