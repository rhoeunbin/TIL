n = int(input())

boom = [list(input()) for _ in range(n)]
board = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

for x in range(n):
    for y in range(n):
        if boom[x][y] == '.' and board == 'X':
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

            if 
