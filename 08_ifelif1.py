'''
작성일 : 2023년 9월 27일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 점수를 입력받아 학점을 출력하시오.
        90~100 : A학점
        80~89 : B학점
        70~79 : C학점
        60~69 : D학점
        00~59 : F학점
알고리즘 : 1. 점수를 입력 받는다.
         2. 판단하여 출력한다.
'''
score = int(input("점수를 입력하세요. : "))
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")
    print("0~100점사이를 입력하세요.\n")
print("::: 두 번째 성적처리 :::\n")
if 90 <= score <= 100:
    print("A학점")
elif score >= 80 and score <= 89 :
    print("B학점")
elif 70 <= score <= 79:
    print("C학점")
elif 60 <= score <= 69:
    print("D학점")
elif 0 <= score <= 59:
    print("F학점")
else:
    print("0~100점사이를 입력하세요.\n")
print("::: 세 번째 성적처리 :::\n")

if score >= 0 and score <= 100:
    if score >= 90:
        print("A학점")
    elif score >= 80:
        print("B학점")
    elif score >= 70:
        print("C학점")
    elif score >= 60:
        print("D학점")
    else:
        print("F학점")
else:
    print("0~100점사이를 입력하세요.\n")