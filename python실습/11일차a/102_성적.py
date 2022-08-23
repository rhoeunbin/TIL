import sys

input = sys.stdin.readline

for i in range(int(input())):
    score = list(map(int, input().split()))
    gap = []
    score.pop(0)  # 맨 앞은 학생 수로 제외

    for j in range(len(score) - 1):
        score.sort()
        g = score[j + 1] - score[j]
        gap.append(g)

    print(f"Class {i+1}")
    print(f"Max {max(score)}, Min {min(score)}, Largest gap {max(gap)}")
