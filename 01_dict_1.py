'''
작성일 : 2023년 11월 1일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 8.1키와 값을 가지는 딕셔너리
        
    튜플 = (), 리스트 = [], 딕셔너리 = {}
'''
#빈 딕셔너리 생성
phone_book1 = {}

#딕셔너리에 값 저장. 1. key, value         [key] = value
phone_book1['김민재'] = '01011112222'

print('phone_book1 :', phone_book1)
#딕셔너리에 값 저장. 2. key, value
phone_book2 = {'홍길동' : '01011112234', '김민재' : '01011112222'}
print('phone_book2 :', phone_book2)

phone_book3 = {}
phone_book3['김민재'] = '01011112222'
phone_book3['홍길동'] = '01033334444'
phone_book3['정근우'] = '01055556666'
phone_book3['이대호'] = '01077778888'
phone_book3['신재영'] = '01099990000'

print('phone_book3 :', phone_book3)
print(":: 전화번호 phone_book3 출력 ::")
#모든 key 출력
print(phone_book3.keys())
for key in phone_book3.keys():
    print(key, ":", phone_book3[key])
#모든 value 출력
print(phone_book3.values())
for i in phone_book3.values():
    print(i)
#모든 key, value 출력
print(phone_book3.items())
for name, phone in phone_book3.items():
    print(name, ",", phone)

print()

print("딕셔너리 작성 시 : (콜론)을 기준으로 key:value 작성")
person_dict = {'name' : '김민재', 'age' : '20', 'class' : '1학년'}

print('name :', person_dict['name'])
print('age :', person_dict['age'])
print()

print(":: 정렬 ::")
# phone_book3를 정렬
# 딕셔너리를 키를 기준으로 정렬하여 리스트로 반환.
print(sorted(phone_book3))
print(":: 키를 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])
print(sort_phone_book3)

sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])
print(sort_phone_book3)

print(':: 항목 삭제 ::')
del phone_book3['김민재']
print(phone_book3)

print(":: 전체 삭제 ::")
phone_book3.clear()
print(phone_book3)