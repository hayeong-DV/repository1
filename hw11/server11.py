from socket import *
import time
import socket, select

socks=[] #소켓 리스트
port = 2500
BUFFSIZE = 1024

s_sock = socket.socket()
s_sock.bind(('', port))
s_sock.listen(5)

socks.append(s_sock) #서버 소켓 우선 추가
print(str(port)+'에서 접속 대기 중')

while True:
    r_sock, w_sock, e_sock = select.select(socks,socks,[])

    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            if c_sock not in socks:
                print('new Client', addr)
                socks.append(c_sock)
        else:
            data = s.recv(BUFFSIZE)
            if not data:
                break
            elif 'quit' in data.decode():
                print(s, 'exited')
                s.close()
                socks.remove(s)
                continue
            
            for c in w_sock:
                if s != c:
                    c.send(data)
            print(time.asctime() +str(addr)+ ':' + data.decode())
