# 10까지의 피보나치 수열을 출력
def fibo(n):
   if n == 0:
      return 0
   elif n == 1 or n == 2:
      return 1
   else:
      return fibo(n-1) + fibo(n-2)
for i in range(0, 10): 
    print(fibo(i))
