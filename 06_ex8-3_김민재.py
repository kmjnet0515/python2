'''
작성일 : 2023년 11월 8일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 심화문제 8-3
학번, 이름, 전화번호의 3쌍의 요소를 가지는 student_tuple 튜플이 존재한다.

이 튜플을 수정하여 {학번 : [이름, 전화번호]}의 쌍으로 이루어진 딕셔너리를 만들어 출력하시오.

이 정보를 이용하여 학생의 학번을 입력 받아 이름과 전화번호를 출력하는 학사정보 프로그램을 작성

student_tuple의 마지막 항목으로 학점을 추가한다
이 정보를 바탕으로 딕셔너리를 만들어 출력하시오.

학생의 학점 평균을 출력하시오.
'''
print("\'\'  \"a\" \'\\\'를 사용해서 출력함")
student_tup = (('211101','조성훈', '010-1234-4500'),('211102', '김은지', '010-2230-6548'),('211103', '윤소정', '010-3232-7788'))

dict1 = {}
for school_num, name, tel in student_tup:
    dict1[school_num] = [name, tel]
print("학생의 정보 목록")
for key, value in dict1.items():
    print("{"+"\'{}\' : {}".format(key,value)+"}")

input_school_num = input("학번을 입력하세요. : ")
print("이름 : ", dict1[input_school_num][0])
print("연락처 : ", dict1[input_school_num][1])
num = sum = 0
'''
student_tup = list(student_tup)

for i in student_tup:
    student_tup[num] = list(i)
    num += 1
for i in student_tup:
    i.append(float(input("{}학번 학생의 학점을 입력하세요. : ".format(i[0]))))
    sum += i[3]'''
for i in dict1.values():
    i.append(float(input("{}학번 학생의 학점을 입력하세요. : ".format(i[0]))))
    sum += i[2]
print("학생의 정보 목록")
for key, value in dict1.items():
    print("{"+"\'{}\' : {}".format(key,value)+"}")
print("학생의 평균학점은 : {:.2f}".format(sum/len(student_tup)))