#1번
from random import randint

x = 50

while True:
    coin = randint(1,2)
    if (x<=0 or x>=100):
        break
    else:
        if coin ==1:
            x+=9
        else:
            x-=10
if(x<=0):
    print("돈을 모두 잃었습니다")
else:
    print("$100 채움")

