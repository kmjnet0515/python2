'''
작성일 : 2023년 9월 20일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 터틀 그래픽으로 여러개의 원을 그려보자
'''
import turtle as t
t.color('red') # 색깔 지정하기
t.shape('turtle')   #모양 지정하기
t.bgcolor('black')  #배경색 지정하기
t.speed(5)  #속도 지정하기
#원 하나 그리기
#t.circle(100)
num = 10
for count in range(num):
    t.circle(100)
    t.left(360/num)

