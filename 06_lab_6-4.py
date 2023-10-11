'''
작성일 : 2023년 10월 4일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.

리스트에 10개의 값을 랜덤으로 생성하고, max 또는 min을 입력 받아 최대, 최솟값을 찾아 돌려주는 함수.
(함수)
    5) 두 값을 전달 받아 매개 변수에 저장.
    6) 최댓값 또는 최솟값을 찾는다.
    7. 돌려준다.
(메인)
1. 무한반복
    1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성
    2) 생성된 리스트를 출력
    3) 사용자로부터 최댓값을 알고 싶은지 최솟갑승ㄹ 알고 싶은지 묻는다.
        사용자가 입력한 값은 max or min
    4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
    8) 돌려받은 최댓값 또는 최솟값을 출력한다.
'''
def findmaxmin(list1, solution):
    return max(list1) if solution =='max' else min(list1)

from random import randint
while True:
    list1 = [randint(10, 99) for i in range(10)]
    print(list1)
    solution = input("max 또는 min을 입력하세요.")
    if solution not in ['max', 'min']:
        continue
    print("{}값은 {}입니다.".format(solution, findmaxmin(list1, solution)))