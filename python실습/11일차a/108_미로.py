# import sys
# from collections import deque

# input = sys.stdin.readline

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def bfs(x, y):
#     queue = deque
#     queue.append((x, y))
#     visit[x][y] = 1

#     while queue:
#         x, y =queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0 <= nx <n and 0 <= ny < m and not visit[nx][ny]:
#                 if graph[nx][ny] == 1:
#                     visit[nx][ny] = visit[x][y] + 1
#                     queue.append((nx, ny))
#     return visit[n-1][m-1]


# n, m = map(int, input().split())
# graph = [list(input().split() for _ in range(n))]

# # print(*graph, sep = '\n')
# visit = [[0] * m for _ in range(n)]
# print(bfs(0,0))




from collections import deque
# Queue를 사용하기 위한 collection library 사용

N, M = map(int, input().split())
# 행과 열의 개수 받기

graph = [] # 이차원 리스트

for _ in range(N):
    graph.append(list(map(int, input())))

# 너비 우선 탐색 => bfs 선언 (모든 노드를 방문할 때) => x와 y를 받음
def bfs(x, y):
  # 이동할 네 가지 방향
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]

    # deque 생성
    # deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue라이브러리를 이용하는 것보다 더 간단
    queue = deque() #queue 초기화
    queue.append((x, y)) # (x,y) 한 집합을 넣는다

    while queue: # queue가 빈 값이 나올 때까지 반복
        x, y = queue.popleft() # queue에서 하나씩 꺼내기   => deque와 popleft를 하면 O(1)
        
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4): # 4방향
            nx = x + dx[i] # 가로 이동
            ny = y + dy[i] # 세로 이동

            # 위치가 벗어나면 안되기 때문에 조건 추가
            # 칸이 미로의 벽에 닿는지// 칸이 미로의 벽을 넘어가는지
            if nx < 0 or nx >= N or ny < 0 or ny >= M: # 미로 밖으로 이동하는 경우
                continue
            
            # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue
            
            # 벽이 아니므로 이동
            if graph[nx][ny] == 1: # 다음 칸이 1이면 이동 가능
                graph[nx][ny] = graph[x][y] + 1 # 경로를 갱신해줌 =>  nx, ny 칸으로 이동
                queue.append((nx, ny)) # queue에 현재 위치한 nx, ny 값을 전달해 위치 옮겼다고 기록
    
    # while문을 다 돌면 queue가 빈 상태이므로 최종 목적지에 도달
    # 최종 위치에서 최소 거리 반환
    # 마지막 값에서 카운트 값 return(몇번 만에 이 자리에 도착했는지 값이 매겨짐)
    return graph[N-1][M-1] # N-1, M-1 을 하는 이유 => graph = [[0],[0]] 이지만 행과 열을 (1,1)부터 시작해서 세서

print(bfs(0, 0)) # bfs 함수를 사용하기 위해 초기 시작 지점을 넣고 print