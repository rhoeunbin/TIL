import sys
import heapq
input = sys.stdin.readline

n =int(input())  #연산의 개수
heap = []        #heap 생성

for i in range(n):    #n만큼
    x = int(input()) #x = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]
    if x != 0:       
        heapq.heappush(heap, (abs(x), x))  # heappush 값을 넣을 때
    else :
        if heap:   
            print(heapq.heappop(heap)[1]) # heappop 값을 뺄 때
        else:
            print(0)