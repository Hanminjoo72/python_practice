a = int(input())

def fac(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    print(result)

fac(a)