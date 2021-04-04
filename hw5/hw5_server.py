from socket import *

def calculator(Data):
        val1, val2  = int(Data[0]), int(Data[2])
        if Data[1] == '+':
            value = val1 + val2
        elif Data[1] =='-':
             value = val1 - val2
        elif Data[1] =='*':
             value = val1 * val2
        elif Data[1] =='/':
            value = val1 / val2
        return value


sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 3000))
sock.listen(1)

while True:
    client, addr = sock.accept()
    #연결 확인
    print('connection from', addr)
    client.send(b'Hello ' + addr[0].encode())

    while True:
        data = client.recv(1024)
        if not data:
            break
        
        #받은 데이터 디코드
        data_d = data.decode()
        print("receive: ", data_d)

        # 공백기준으로 나누기 
        data_sp = data_d.split(' ')
        print(data_sp)

        #연산자 기준으로 피연산자 계산시키고, 결과 전송하기
        result = calculator(data_sp)
        client.send((str(result)).encode())
client.close()
sock.close()
        