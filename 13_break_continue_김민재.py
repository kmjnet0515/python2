'''
작성일 : 2023년 10월 4일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 반복문을 제어하는 break, continue
      교재 137페이지
      
      Test word : programming
      
'''
#단어를 입력받기
word = input("단어를 입력하세요. : ")
#모음을 변수에 저장하기
vowel = 'aeiou'
#단어 하나씩 반복하면서
for i in word:
    #i가 모음 변수에 있다면
    if i in vowel:
        #반복문 나가기
        break
    #아니면
    else:
        #i 출력하기
        print(i, end="")
'''
for i in word:
    #i가 모음 변수에 있다면
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        #반복문 나가기
        break
    #아니면
    else:
        #i 출력하기
        print(i, end="")
'''        
print()
print(":: continue ::")
vowel = 'aeiouAEIOU'
for i in word:
    #i가 모음 변수에 있다면
    if i in vowel:
        #처음으로 돌아가기
        continue
    #i 출력하기
    print(i, end="")