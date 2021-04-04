import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 3000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

while True:
    msg = input('Input like "20 + 17": ')
    if msg == 'q':
        print('close')
        break
    sock.send(msg.encode())

    result = (sock.recv(1024)).decode()
    print('Received result:', format( float(result), ".1f" ))
sock.close()
 
