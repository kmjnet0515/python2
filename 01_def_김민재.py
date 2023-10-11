'''
작성일 : 2023년 10월 4일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : def 예약어를 이용하여 함수 작성하고 호출하기
'''
print("def 예약어를 이용하여 함수 작성하고 호출하기")

#함수 선언
def print_address():
    print("부산시 사상구")
    print("괘법동 산 1-1번지")
    print("신라대학교 국제교육관 552호")
    
print_address()
'''
    함수에 값을 넘겨주고 일을 시킨다.
    인자와 매개변수
'''
print("인자와 매개변수")
def welcome(name):
    print("{}님 안녕하세요.".format(name))
welcome(input("이름을 입력하세요. : "))