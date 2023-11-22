n = int(input())
card = list(map(int,input().split()))
m = int(input())
find =list(map(int,input().split()))

count_ = {} # 카드 숫자와 개수 넣을 딕셔너리

for i in card: #card의 숫자 세기
    if i in count_: #있었던 숫자면 +1
        count_[i] += 1 
    else : # 아니면 1
        count_[i] = 1
# print(count_)

for i in find: #find 리스트에서
    if i in count_ : #해당하는 숫자 있으면 해당 인덱스 딕셔너리에서 출력
        print(count_[i], end = ' ')
    else: #해당하는 숫자 없으면 0출력
        print(0, end = ' ')



    

