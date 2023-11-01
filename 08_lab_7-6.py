'''
작성일 : 2023년 11월 1일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 도시의 이름과 인구를 튜플로 묶어보자
'''
#도시 정보
city_info = [('서울' , 9675), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]
#변수 선언 초기화
#기준
max_pop = 0
#기준
min_pop = 999999999999999
total_pop = 0

max_city = None
min_city = None
#city_info속 tuple을 하나씩 반복하면서
for city in city_info:
    #총인구에 튜플의 2번째 요소(인구)를 더함
    total_pop += city[1]
    # 인구가 최대보다 크면
    if city[1] > max_pop :
        #최대값에 인구 저장
        max_pop = city[1]
        #최대 도시에 도시 이름 저장
        max_city = city[0]
    # 인구가 최소보다 작으면
    if city[1] < min_pop :
        #최소값에 인구 저장
        min_pop = city[1]
        #최소 도시에 도시 이름 저장
        min_city = city[0]
print('최대인구: {0}, 인구: {1} 천명'.format(max_city, max_pop))
print('최소인구: {0}, 인구: {1} 천명'.format(min_city, min_pop))
print('리스트 도시 평균 인구: {0} 천명 '.format(total_pop / len(city_info)))