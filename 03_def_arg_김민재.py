'''
작성일 : 2023년 10월 4일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 함수에 여러 개의 값 넘겨주기

두 수를 입력받아 함수를 호출하여 두 수 사이의 합을 계산하여 돌려주는 함수

[알고리즘]
(함수)
    3. 두 수를 전달받아 매개변수에 저장한다.
    4. 두 수 사이의 합을 계산한다.
    5. 계산된 합을 함수를 호출한 곳으로 돌려준다.
    
(메인)
    1. 두 수를 입력 받는다.
    2. 두 수를 가지고 함수를 호출한다.
    6. 돌려받은 합을 출력한다.
'''
def add(start,end):
    result = 0
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        result += i
    return result
num1 = int(input("첫 번째 수를 입력하세요. "))
num2 = int(input("두 번째 수를 입력하세요."))
print("{}부터 {}까지 원소는 : {}, 합은 {}입니다.".format(num1, num2, ([i for i in range(num1, num2 + 1)]) if num1 <= num2 else [i for i in range(num1, num2 - 1 , -1)], add(num1,num2)))