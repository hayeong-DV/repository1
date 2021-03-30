import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connectio from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    #이름 수신 후 출력
    name = client.recv(1024)
    print(name.decode())
    #학번을 전송
    client.send((20181511).to_bytes(4, 'big'))
    client.close()