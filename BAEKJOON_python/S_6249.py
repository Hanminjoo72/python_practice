num = int(input())
count = [0] * 10

while num > 0:
    count[num%10] += 1
    num = num // 10

print(" ".join(map(str,[i for i in range(10)])))
print(" ".join(map(str,count)))