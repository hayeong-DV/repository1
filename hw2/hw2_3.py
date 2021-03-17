#3번
str = input("Your word: ")
index = str.find('a')+1
last = len(str)-index

print(str[:index])
print(str[index:])