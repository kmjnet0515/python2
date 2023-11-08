'''
작성일 : 2023년 11월 8일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : lab 8-3
'''
partyA = set(['Park', 'Kim', 'Lee'])
partyB = set(['Park', 'Choi'])
print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA.intersection(partyB))
print("partyA와 partyB에 참석한 사람들은 :", partyA.union(partyB))
print("1개의 파티에만 참석한 사람은 :", partyA.symmetric_difference(partyB))
print("파티 A에만 참석한 사람은 :", partyA.difference(partyB))