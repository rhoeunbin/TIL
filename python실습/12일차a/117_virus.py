import sys
input = sys.stdin.readline
from collections import deque

com = int(input()) # 컴퓨터 수(정점) 
n= int(input()) # 컴퓨터 쌍의 수(간선)

graph = [[] for _ in range(com+1)] # 컴퓨터 수만큼의 그래프
visited = [False]*(com+1) #노드가 방문된 정보

for _ in range(n): # 컴퓨터 쌍의 수만큼 반복
    a, b = map(int,input().split()) # 컴퓨터 쌍 input
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
def bfs(graph, start, visited):
    queue = deque([start]) #현재 노드 방문 처리
    visited[start] = True
    cnt = 0
    while queue: 
        v = queue.popleft() # 큐에서 값 하나씩 봅아서

        for i in graph[v]:
            if not visited[i]: #변수가 방문하지 않았다면
                # print(i)
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

#     # 1번 컴퓨터 제외
# bfs(graph, 1, visited) #정의된 함수 호출
# print(visited)
# print(len(visited)-1) # 1번 컴퓨터 빼고
print(bfs(graph, 1, visited))
    