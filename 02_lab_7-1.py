'''
작성일 : 2023년 10월 18일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 입력을 받아 맛있는 과일의 리스트를 만들자.
'''
#과일 리스트 저장하기
fruits = [input("{}번쨰 과일이름을 입력해주세요. ".format(i + 1)) for i in range(5)]
while True:
    #찾을 과일 입력받기
    findFruit = input("찾을 과일을 입력해주세요.")
    print("{}과일은 있습니다.".format(findFruit)) if  findFruit in fruits else print("{}과일은 없습니다.".format(findFruit))
