# 10번째 값을 출력
a, b = 0, 1
for _ in range(9):
    a, b = b, a + b
print(a)
