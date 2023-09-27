'''
작성일 : 2023년 9월 20일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 터틀 그래픽으로 여러개의 원을 그려보자
        사용자로부터 그리고 싶은 도형의 변의 수를 입력받아 도형을 그린다.
'''
import turtle as t
import math
t.color('red') # 색깔 지정하기
t.shape('turtle')   #모양 지정하기
t.bgcolor('black')  #배경색 지정하기
t.speed(5)  #속도 지정하기
t.penup()
num = int(t.textinput("","몇 각형의 도형을 그릴까요?"))
length = 100
#가운데에 출력하기
t.left(90 + (360/num)/2)
t.forward(((length**2)**(1/2)/(2*(1-math.cos(2*math.pi/num)))**(1/2)))
t.left(90 + (360/num)/2)
t.pendown()
for i in range(num):
    t.forward(100)
    t.left(360/num)
t.mainloop()

