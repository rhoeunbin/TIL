import sys
input = sys.stdin.readline

a, b= map(int,input().split()) # 집합 A의 원소의 개수와 집합 B의 원소의 개수

A = set(map(int,input().split())) #집합 A
B = set(map(int,input().split())) #집합 B

print(len(A-B)+len(B-A)) #대칭 차집합의 원소의 개수