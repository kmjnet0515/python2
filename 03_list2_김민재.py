'''
작성일 : 2023년 10월 18일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 리스트에서 사용가능한 함수
'''

num_list = [i for i in range(1,10)]
print("num_list1 : ", num_list)
print("num_list1 길이 : ", len(num_list))
print("num_list1 최댓값 : ", max(num_list))
print("num_list1 최솟값 : ", min(num_list))
print("num_list1 항목의 합계 : ", sum(num_list))
print("num_list1 항목의 평균: ", sum(num_list)/len(num_list))
print("num_list1 항목 중 0이 아닌 원소가 있는가? : ", any(num_list))


