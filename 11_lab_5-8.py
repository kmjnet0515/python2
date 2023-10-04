'''
작성일 : 2023년 10월 4일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : while 문으로 별 그리기를 해보자
'''
import turtle as t
t.color('red') # 색깔 지정하기
t.shape('turtle')   #모양 지정하기
t.bgcolor('black')  #배경색 지정하기
t.speed(5)  #속도 지정하기
count = 1 #1부터
while count <= 5: #5가되기까지
    t.forward(50) #50만큼 이동
    t.right(144) #144도 회전
    count += 1 #증가값
t.mainloop()