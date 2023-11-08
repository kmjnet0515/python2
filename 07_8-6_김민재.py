'''
작성일 : 2023년 11월 8일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 심화문제 8-6 
튜플을 요소로 가지는 student_tuple 리스트가 다음과 같이 있다. 이 튜플의 요소가 되는 튜플은(학번, 이름, 전화번호)로 이루어져있다. 
이를 이용하여 (학번 : 이름)의 딕셔너리를 만들어 출력하라.
이를 이용하여 학번으로 조회할 경우 다음과 같이 학번, 이름과 전화번확 출력되도록 하여라.
'''
student_tup = [('211101','강이안', '010-123-1111'),('211102', '박동민', '010-123-2222'),('211103', '김수정', '010-123-3333')]
dict1 = {}
for i in student_tup:
    dict1[i[0]] = i[1]
for key, value in dict1.items():
    print("{} : {}".format(key,value))
input_school_num = input("학번을 입력하세요 : ")
num = 0
for i in student_tup:
    if i[0] == input_school_num:
        
        break
    num += 1
print("{} 학생은 {}이며, 전화번호는 {}입니다.".format(input_school_num, student_tup[num][1], student_tup[num][2]))