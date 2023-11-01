'''
작성일 : 2023년 11월 1일
작성자 : 컴퓨터공학과 202395006 김민재
설명 : 한 번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''
#튜플 생성
t_colors = (
    "Red", "Orange", "Yellow", "Green", "Blue",
    "Purple", "Pink", "Brown", "Gray", "Black",
    "White", "Lime", "Cyan", "Magenta", "Terracotta",
    "Silver", "Gold", "Lawn Green", "Turquoise", "Fruit Punch",
    "Sky Blue", "Royal Blue", "Lavender", "Raspberry",
    "Blackberry", "Coffee", "Beige", "Khaki", "Burgundy",
    "Coral", "Indigo", "Orange", "Mocha", "Peppermint",
    "Cream", "Jasmine", "Butterscotch", "Walnut", "Lilac",
    "Pink", "Purple", "Violet", "Vermilion", "Charcoal",
    "Tungsten", "Mahogany", "Ivory", "Apricot", "Apple Green"
)
#리스트 생성
l_colors = list(t_colors)
print("\n\n\nlist : {}\n\n\ntuple : {}".format(l_colors, t_colors))
#tuple개체에 'append'속성이 없음 -> 튜플은 추가 삭제가 안 됨.
#color.append('aaa')
print('튜플 중 2,3,4번은 :', t_colors[2:5])

print(t_colors[1:5] * 2)
print(t_colors[1:2] + t_colors[2:5])

