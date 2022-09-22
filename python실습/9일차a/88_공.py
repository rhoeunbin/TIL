import sys
input = sys.stdin.readline

M = int(input())

cup = [0, 1, 2, 3]  #0이 없으면 IndexError: list index out of range
for _ in range(M):
    a, b = map(int,input().split())
    cup[a], cup[b] = cup[b], cup[a]  

print(cup.index(1))