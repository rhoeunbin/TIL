import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    cnt = 0

    for i in range(n, m + 1):
        cnt += str(i).count("0")  # 숫자를 문자열로 바꾸어 count하면 됨
    print(cnt)
