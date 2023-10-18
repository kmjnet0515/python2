'''
작성일 : 2023년 10월 18일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 리스트의 객체 생성과 참조
'''

fruits1 = ['딸기', '수박', '바나나']

fruits2 = fruits1
print("fruits1 : {}, fruits2 : {}".format(fruits1, fruits2))


fruits2[1] = '망고' #fruits2의 [1]번지 과일을 망고로 바꾸면
print("fruits1 : {}, fruits2 : {}".format(fruits1, fruits2))

# 주소 확인 => 메모리 위치 정보 알아보기 id()함수
print("fruits1의 id : {}, fruits2의 id : {}".format(id(fruits1), id(fruits2)))
fruits2 = fruits1.copy()
print("fruits1의 id : {}, fruits3의 id : {}".format(id(fruits1), id(fruits2)))

fruits2 = list(fruits1)
print("fruits1의 id : {}, fruits3의 id : {}".format(id(fruits1), id(fruits2)))
fruits2 = fruits1[:]
print("fruits1의 id : {}, fruits3의 id : {}".format(id(fruits1), id(fruits2)))
