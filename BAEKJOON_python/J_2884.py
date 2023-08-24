H, M = map(int, input().split())

if M < 45 :	
    if H == 0 :
        H = 23
        M += 15
    else :
        H -= 1	
        M += 15
        
<<<<<<< HEAD:J_25304.py
print(H, M)
=======
print(H, M-45)
>>>>>>> 5531101104750237a5ab6710ab977fda3f0035fc:BAEKJOON_python/J_2884.py
