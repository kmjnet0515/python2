import string

from random import randint
'''
작성일 : 2023년 11월 8일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 집합 set()
'''
number = set()
#숫자 3개로 이루어진 집합
number1 = {2,1,3}
print("집합 : ", number1)
number2 = set([i for i in range(0,101,3)])
number3 = set([i for i in range(0,101, 4)])
print("합집합 : ", number2 | number3)
print("교집합 : ", number2 & number3)
print("차집합 : ", number2 - number3)
print("대칭차집합 : ", number2 ^ number3)
text1 = set("asdfasdf")
print(text1)
numbers = {2,4,1,5,2}
#numbers에 1 원소가 들어있을 때
if 1 in numbers:
    #1빼기
    numbers -= {1}
print(numbers)
numbers = sorted(set([string.ascii_lowercase[randint(0,25)] for i in range(10)]))
for num in numbers:
    print(num, end=' ')
print()
numbers = sorted(set([randint(1,10) for i in range(10)]))
for num in numbers:
    print(num, end=' ')
print()
numbers = set([i for i in range(1,11)])
numbers.add(100)
print(numbers)

numbers.remove(1)
print(numbers)