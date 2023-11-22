a_list = list(map(int,input().split())) #a 리스트
b_list = list(map(int,input().split())) #b 리스트
winner = 'D' 

a = 0 #a 승점
b = 0 #b 승점
for i in range(10):
    if a_list[i] > b_list[i]:
        a += 3 #a에 승점 추가
        winner = 'A'

    elif a_list[i] < b_list[i]:
        b += 3 #b에 승점 추가
        winner = 'B'

    else : #같으면
        a += 1
        b += 1
print(a,b)

if a > b :
    print('A')

elif b > a:
    print('B')

else:
    print(winner)        
