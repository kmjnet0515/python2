from random import randint
'''
작성일 : 2023년 11월 8일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 집합의 연산
'''
num1 = {1,2,3}
num2 = {1,2,3}
print("num1 == num2", num1 == num2)
num2 ^= {2,3,5,7}
print("num1 != num2", num1 != num2)

num_set = {1,4,6,3,7,4}
print("num_set : ", num_set)
print("num_set의 길이 :", len(num_set))
print("num_set의 최대 :", max(num_set))
print("num_set의 최소 :", min(num_set))
print("num_set의 합 :", sum(num_set))
num1 = {1,2,3}
num2 = {3,4,5}
#합집합
print("num1 | num2 :", num1 | num2)
print("num1.union(num2) :", num1.union(num2)) #합집합 메소드 union()
#교집합
print("num1 & num2 :", num1 & num2)
print("num1.intersection(num2) :", num1.intersection(num2)) #합집합 메소드 union()
#차집합
print("num1 - num2 :", num1 - num2)
print("num1.difference(num2) :", num1.difference(num2))
#대칭차집합
print("num1 ^ num2 :", num1 ^ num2)
print("num1.symmetric_difference(num2) :", num1.symmetric_difference(num2))