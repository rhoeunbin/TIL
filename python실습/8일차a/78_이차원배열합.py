import sys
input = sys.stdin.readline

n, m = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int,input().split())
    cnt = 0

    for r in range(i, x+1):
        for c in range(j, y+1):
            cnt += matrix[r][c]

    print(cnt)



n, m = map(int, input().split()) #배열의 크기 N, M
num = [] # 배열 넣을 리스트
for _ in range(n): #배열에 넣기
    num.append(list(map(int, input().split())))

k = int(input()) #합을 구할 부분의 개수 K
for _ in range(k):
    i, j, x, y = map(int, input().split()) #k개의 줄에 네 개의 정수 주어짐
    cnt = 0 #누적 합
    for r in range(i-1, x): 
        for c in range(j-1, y):
            cnt += num[r][c]
    print(cnt)

#2 3
# 1 2 4         1+2+8+16=27
# 8 16 32
# 3
# 1 1 2 3  i,j,x,y
# 1 2 1 2
# 1 3 2 3