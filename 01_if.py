'''
작성일 : 2023년 9월 20일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 선택문 if
        성적을 입력 받아 60점 이상이면 "합격입니다."를 출력
'''
#1. 성적을 입력받는다. -> 입력 받아(문자) 정수로 변환하여 변수에 저장
score = int(input("점수를 입력하세요. : "))
#2. 60점 이상이면 '합격'출력.
if score >= 60:
    print("합격입니다.")
'''
자동차의 속도를 입력받아 속도를 출력하고(현재속도 : 00km/h), 30km/h이상이면 '과속입니다. 속도를 줄이세요.'를 출력하고, 속도와 상관없이 '안전운전하세요'를 출력
'''
#1. 자동차의 속도를 입력받아 정수로 변환하여 변수에 저장
speed = int(input("자동차의 속도를 입력하세요. : "))
print("현재 속도 : {}km/h".format(speed))
#2. 속도가 30 이상이라면
if speed >= 30:
    #2.1 '과속입니다. 속도를 줄이세요.'출력
    print("과속입니다. 속도를 줄이세요.")
#3. '안전운전하세요'출력
print("안전운전하세요.")