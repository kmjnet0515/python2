'''
작성일 : 2023년 10월 4일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 조건에 따라 반복하는 while문
'''
# while 조건식: ':' 사용
#    들여쓰기로 반복하면서 할일 작성
# 반복문에서는 반드시 종료 조건이 있어야 한다.
# while True : 무한 반복
under_construction = True
#True일 때동안 계속 반복
while under_construction:
    response = input("공사가 완료 되었습니까?")
    if response == '예':
        under_construction = False
print("루프 탈출")