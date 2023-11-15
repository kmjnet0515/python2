'''
작성일 : 2023년 11월 15일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 문자열
'''
#문자열 슬라이싱
s = "Happy Day!"
print(s[0])
print(s[0:2])
print(s[:-2])

#문자열 분리 : split()
s = "Welcome to Python"
print(s.split())

s = "2023.11.15"
print(s.split('.')) #분리기준이 없는 경우 공백

s = "Hello, World!"
print(s.split(', '))
s = "Welcome, to, Python, and, bla, bla"
print([x.strip() for x in s.split(',')])

print(list("Hello, World!"))

#문자열 연결 .join()
print(','.join("abcd"))
print(','.join(['apple', 'grape', 'banana']))
#print('-'.join('010.1234.5678'))
print(('-').join('010.1234.5678'.split('.')))
print('010.1234.5678'.replace('.','-'))

s = "Hello, World!"
print(s)
sList = list(s)
print(('').join(sList))

#줄바꿈과 탭이 포함된 문자열 그대로 출력
aString = "Today as well, \n\t Have a Happy Day!"
print((' ').join(aString.split()))

#대소문자 변환과 문자열 삭제
s = "Hello, World!"
print(s.lower())
print(s.upper())
print(s.lower().capitalize())

#공백제거
s = '        Hello, World!         '
print(s.strip())
print(s.rstrip())
print(s.lstrip())
s = '####....#.#.Hello, World!.#.#....####'
print(s.strip('#').strip('.').strip('#').strip('.').strip('#').strip('.'))
print(('').join([i for i in s if i not in '.#']))
s = "www.silla.ac.kr"
print(s.find('.kr'))
print(s.index('.kr'))
print(s.find('.com'))
#print(s.index('.com'))
print(s.count('w'))

