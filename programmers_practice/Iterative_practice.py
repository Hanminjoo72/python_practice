# 10까지의 피보나치 수열을 출력
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b
