from random import randint
'''
작성일 : 2023년 9월 20일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 선택문 if~else
        random을 이용한 가위바위보 게임.
'''
name1 = input("사용자1 이름을 입력하세요.")
name2 = input("사용자2 이름을 입력하세요.")
list1 = ['가위', '바위', '보']
while True:
    num1 = randint(1,3)
    num2 = randint(1,3)
    print("{} : {}, {} : {}".format(name1,name2,list1[num1-1], list1[num2-1]))
    # 사용자가 입력한 것에 해당되는 숫자가 사용자 2가 입력한 수보다 크거나 그 둘의 차가 -2(사용자가 가위, 사용자2 보)일 때 그리고 그 둘의 차가 2는 아닐 때(사용자가 보 사용자2가 가위)

    if (num1 > num2 or num1 - num2 == -2) and num1 - num2 != 2 :
        #이겼습니다.출력
        print(f"{name1}이 이겼습니다.")
        print(f"{name2}가 졌습니다.")
    #같다면
    elif num1 == num2:
        #비겼습니다 출력
        print(f"{name1}과 {name2}가 비겼습니다.")
    #아니면
    else:
        #졌습니다. 출력
        print(f"{name1}이 졌습니다")
        print(f"{name2}가 이겼습니다.")
    print('\n\n')