from random import randint
'''
작성일 : 2023년 9월 20일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 선택문 if~else
        random을 이용한 가위바위보 게임.
'''
#가위바위보가 담긴 리스트 생성
list1 = ['가위', '바위', '보']
while True:
    # 사용자는 가위, 바위, 보를 입력한다.
    name = input("가위, 바위 , 보 중에 입력하세요.")
    #컴퓨터가 내는 수를 랜덤으로 1에서 3까지 숫자로 받기
    name2 = randint(1,3)
    #출력하기
    print("사용자 : {}, 컴퓨터 : {}".format(name, list1[name2-1]))
    # 사용자가 입력한 것에 해당되는 숫자가 컴퓨터가 낸 수에서 1을 뺀(list는 0부터 시작) 수보다 크거나 그 둘의 차가 -2(사용자가 가위, 컴퓨터 보)일 때 그리고 그 둘의 차가 2는 아닐 때(사용자가 보 컴퓨터가 가위)
    if name in list1:
        if (list1.index(name) > name2 - 1 or list1.index(name) - (name2 - 1) == -2) and list1.index(name) - (name2 - 1) != 2 :
            #이겼습니다.출력
            print("이겼습니다.")
        #같다면
        elif list1.index(name) == name2 - 1:
            #비겼습니다 출력
            print("비겼습니다.")
        #아니면
        else:
            #졌습니다. 출력
            print("졌습니다.")