'''
작성일 : 2023년 10월 18일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 도시의 인구 자료에 대한 슬라이싱하기.
'''
population = ['Seoul', 9765, 'Busan', 3441, 'Incheon', 2954]
print("서울 인구 :", population[1]) #2번쨰 요소
print("인천 인구 :", population[-1]) # 마지막 요소
print("도시 리스트 :", population[::2]) #홀수번째
print("인구의 합 :", sum(population[1::2])) #짝수번째