#2번
a = int(input("숫자 입력: "))
b = int(input("숫자 입력: "))

if a < b: 
    a, b = b, a 
while b != 0:
    a, b = b, a % b 

print(a)
