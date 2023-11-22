import sys

input = sys.stdin.readline

n = int(input())
num = []

for i in range(n):
    nn = map(int, input().split())
    num.append(nn)

num.sort()
print(num)
