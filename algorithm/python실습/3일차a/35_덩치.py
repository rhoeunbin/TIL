t = int(input())  #데스트케이스 
wandh = []  # 학생들의 몸무게, 키 넣을 빈 리스트 생성

for _ in range(t):  #t만큼 반복
    x, y = map(int, input().split())
    wandh.append((x, y))  #리스트에 x,y 추가

for i in wandh :
    rank = 1  #1등부터
    for j in wandh :
        if i[0]< j[0] and i[1] < j[1]:   #리스트 각각의 값을 비교
            rank += 1  #등수를 더함  1등-> 2등->,,,
    print(rank, end=" ")