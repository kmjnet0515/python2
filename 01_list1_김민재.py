'''
작성일 : 2023년 10월 18일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 리스트 만들기
'''
#과일 리스트 만들기
fruits = ['딸기', '사과', '바나나']
print("과일목록 : ", fruits)
#수박 추가(append)
fruits.append('수박')
#끄집어내기(pop)
fruits.pop(-1)
#특정 위치에 추가(insert)
fruits.insert(1,'수박')
fruits.append('망고')
fruits = fruits + ['포도']
fruits
print("과일목록 : ", fruits)
num = [1,2,3] + [4,5,6]
print("숫자 리스트 덧셈 결과: ", num) # [1,2,3,4,5,6]
num = [1,2,3] * 3
print("숫자 리스트 * 3 : ", num) # [1,2,3,4,5,6]
#in 연산자 -> 포함되는가?
print("과일 목록에 망고가 있나요? ", '망고' in fruits)
'''
    인덱스를 사용하여 리스트의 항목에 접근하기
'''
#과일 리스트 중 제일 첫 번째 과일은?
print("과일 중 제일 좋아하는 과일은? : ",fruits[0])
#과일 리스트 중 제일 마지막 과일은?
print("과일 중 제일 마지막 과일은? : ", fruits[-1])
#과일의 최대와 최소
print("과일 중 가장 큰 과일은? : ", max(fruits))
print("과일 중 가장 작은 과일은? : ", min(fruits))
#과일 정렬
fruits.sort()
print("과일을 사전 순서대로 정렬 ", fruits)
fruits.sort(reverse=True)
print("과일을 사전 순서대로 정렬 ", fruits)
'''
    리스트를 원하는 모양으로 자르는 슬라이싱
'''
print("과일 목록 : ", fruits)
print("과일 리스트 중 2,3,4번 과일은? : ", fruits[1:4])
print("과일 리스트 중 1~3번 과일은? : ", fruits[:3])
print("과일 리스트 중 3번 과일부터 끝까지 과일은? :", fruits[2:])
print("과일 리스트 중 홀수번째 과일을? : ",fruits[::2])
print("과일 리스트 중 짝수번째 과일은? : ",fruits[1::2])
print("과일을 거꾸로 출력 : ",fruits[::-1])
fruits.reverse()
print("과일을 거꾸로 출력 : ",fruits)

'''
    리스트의 원소 값을 자유롭게 조작해보자.
'''

print()
print("과일목록", fruits)
#원하는 위치에 '두리안'추가 -> insert()
fruits.insert(3, '두리안')
print(fruits)

#위치 찾기 -> index()
print("사과의 위치는? ",fruits.index('사과'))

#사과를 마지막에 추가
fruits.append('사과')
print("과일 목록(마지막에 사과 추가) : ",fruits)

#사과의 개수 -> count() 메소드
print("사과의 개수는? :", fruits.count('사과'))

'''
    리스트의 항목 삭제
'''
print()
#사과 삭제 -> remove() 메소드
fruits.remove('사과')
print("사과 삭제 후 : ", fruits)
#특정 위치의 값 삭제 -> pop() 메소드
fruits.pop(1)
print("1번 요소를 끄집어낸 후 :", fruits)

# del()키워드
del(fruits[0])
print(fruits)

