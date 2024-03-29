import turtle as t1
import time
import random

# 스크린 사이즈
t1.setup(width = 800, height = 800)
t1.bgcolor('steelblue')
t1.color('orange')

# 거북이 사이즈
t1.turtlesize(2)

t1.shape('turtle')
t1.penup()
t2 = t1.clone() # 거북이 복제해서 t2에 저장
t2.color('tomato')

# 거북이들 준비 위치로 이동
t1.goto(-400, 200)
t2.goto(-400, -200)

# 출발
while True:
    t1.forward(random.randint(1,100))
    t2.forward(random.randint(1,100))
    time.sleep(1)
    # 도착 체크
    if t1.xcor() > 400:
        t1.goto(0,0)
        t1.write("       winner!" , font=('Arial',20))
        break
    elif t2.xcor() > 400:
        t2.goto(0,0)
        t2.write("       winner!" , font=('Arial',20))
        break
t1.exitonclick()
