import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(str,input().split())) for _ in range(n)]

row = 0 # 가로
col = 0 # 세로

for y in range(n):
    cnt = 0
    for x in range(n):
        if matrix[y][x] == '.':
            cnt += 1
        elif matrix[y][x] == 'X':
            if cnt >= 2:
                row += 1
            cnt = 0
    if cnt >= 2:
        row += 1
    cnt = 0

for x in range(n):
    cnt = 0
    for y in range(n):
        if matrix[y][x] == '.':
            cnt += 1
        elif matrix[y][x] == 'X':
            if cnt >= 2:
                col += 1
            cnt = 0
    if cnt >= 2:
        col += 1
    cnt = 0

print(row, col)


