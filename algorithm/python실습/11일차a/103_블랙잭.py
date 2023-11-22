import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 카드의 개수 n,m
card = list(map(int, input().split()))  # 카드에 쓰여 있는 수
total = 0

for i in range(n):  # n만큼 반복
    # 인덱스 0, 1, 2
    for j in range(i + 1, n):
        # 인덱스 1, 2, 3
        for k in range(j + 1, n):
            # 인덱스 2, 3, 4
            if card[i] + card[j] + card[k] > m:
                continue

            else:
                total = max(total, card[i] + card[j] + card[k])
print(total)
