N, K = map(int, input().split())

result = 0

for i in range(1, N + 1):
    if N % i == 0:
        K -= 1
        if K == 0:
            result = i
            break

print(result)

'''
(6,3)
6 % 1 == 0
2
6 % 2 == 0
1
6 % 3 == 0
0
result = 3

(25,4)
25 % 1 == 0
3
25 % 5 == 0
2
25 % 25 == 0
1
result = 0

(2735,1)
2735 % 1 == 0
0
result = 1

'''
