import matplotlib as plt

'''
작성일 : 2023년 11월 15일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : LAB 9-2 : 트위터 메시지 처리의 단어 추출 띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라..
'''
text = "There's a reason some people are working to make it harder to vote, especially for people of color. It’s because when we show up, things change."
# 띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라. len() => 개수
print(len(text.split()))

text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'
text = text.lower() #소문자로 변환
cName = ['kt', 'samsung', 'lg', 'skt'] #회사명 리스트생성

text2 = [i for i in text.split() if i in cName] #text에 회사명이 있는 것만 저장
cLenSort = [[0],[]]
for i in range(0,len(text2)):
    j = text2[i]
    num = 0
    for k in range(0,len(cLenSort[0])):
        k1 = cLenSort[0][k]
        if k1 <= len(j):
            cLenSort[0].insert(num, len(j))
            cLenSort[1].insert(num, j)
            break
        num += 1

print(cLenSort)
for i in cLenSort[1]:#반복하면서
    text = text.replace(i, '*')#바꾸기
print(text)


for word in cName:
    text = text.replace(word, "**")
print(text)
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'
t = ""
for i in text.lower().split():
    if i in cName: t += '*'
    else: t += i
    t += " "
print(t)


