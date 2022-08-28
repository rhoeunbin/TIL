import sys #시간초과 나와서 넣음
input = sys.stdin.readline


n = int(input()) #회사 사람 수
ent = dict() #회사 사람 넣을 딕셔너리

for i in range(n): #회사 사람 수만큼 반복
    a, b = map(str,input().split()) #사람이름과 enter,leave input 받기
    if b == 'enter': #만약 enter 라면
        ent[a] = 'enter' #리스트에 enter 넣기
    else : # 아니라면(leave 라면)
        del ent[a] #지우기

res = sorted(ent.keys(), reverse=True) #사람 이름만 출력하기 위해 keys 출력, 정렬
print(*res, sep = '\n') #개행해서 출력
