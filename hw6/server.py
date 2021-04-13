from socket import *
import re


s=socket(AF_INET, SOCK_STREAM)
s.bind(('',80))
s.listen(10)


while True:
    c,addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    #print(req[0])

    re_s = re.split(" |/", req[0])
    #print(re_s)

    data = re_s[2]
    print(data)
   
    #웹 서버 코드 작성
    #각 객체(파일,문자열) 전송후, 소켓닫기
    if(data == 'index.html'):
        f = open('index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'

        r_data = f.read()
        c.send(b'HTTP/1.1 200 ok\r\n')
        c.send(b'Content-Type:' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(r_data.encode())

    elif(data == 'iot.png'):
        f = open('iot.png', 'rb')
        mimeType = 'image/png'

        r_data = f.read()
        c.send(b'HTTP/1.1 200 ok\r\n')
        c.send(b'Content-Type:' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(r_data)

    elif(data == 'favicon.ico'):
        f = open('favicon.ico', 'rb')
        mimeType = 'image/x-icon'
        
        r_data = f.read()
        c.send(b'HTTP/1.1 200 ok\r\n')
        c.send(b'Content-Type:' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(r_data)

    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')

s.close()