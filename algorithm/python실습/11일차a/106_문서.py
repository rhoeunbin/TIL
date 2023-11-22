import sys

input = sys.stdin.readline

w = input()
s = input()

while s in w:
    print()

w = input()
s = input()
cnt = 0
n = 0
while n <= len(w) - len(s):
    if w[n : n + len(s)] == s:
        cnt += 1
        n += len(s)
    else:
        n += 1
print(cnt)
