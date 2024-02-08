T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = " ")

'''
bin 함수는 10진수를 2진수로 바꿔주는 함수

1
13

0 1 2 3

print(n[-1]) # 1
print(n[-2]) # 0
print(n[-3]) # 1
print(n[-4]) # 1

print(i, end=' ') # 0 2 3
'''