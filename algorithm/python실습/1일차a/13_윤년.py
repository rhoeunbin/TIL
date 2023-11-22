year = int(input())

#윤년일 때
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('1')
else : # 윤년이 아닐 때
    print('0')