n = int(input()) #우유 가게의 수
milk = list(map(int,input().split())) #우유 가게 정보가 우유 거리의 시작부터 끝까지 N개의 정수로
cnt = 0 # 마신 우유 개수

for i in range(n): 
    if milk[i] == cnt % 3 : #0, 1, 2 나오게 
        cnt += 1 #마신 우유의 개수 +1
print(cnt)


    
