import sys
input = sys.stdin.readline

for _ in range(int(input())):  # test case
    s = int(input())  # 가격
    n = int(input())  # 서로 다른 옵션의 개수

    for tc in range(n):
        q, p = map(int, input().split())
        # q는 해빈이가 사려고 하는 특정 옵션의 개수이고 p는 해당 옵션의 가격
        s += q * p
    print(s)