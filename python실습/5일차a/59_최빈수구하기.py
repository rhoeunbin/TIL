import sys
sys.stdin = open('최빈수.txt')

t = int(input())

for i in range(1,t+1):
    n = int(input())
    num = list(map(int,input().split()))

    max_num = 0
    max_idx = 0

    counts = [0] * 101  #0점 ~ 100점까지 사람 수

    for j in range(1000):  #1000명의 학생
        counts[num[j]] += 1
    # print(counts)

    for j in range(101):  
        if counts[j] >= max_num:  #0점부터 반복하면서 최빈수 찾기
            max_num = counts[j] #최빈수가 여러개이면 더 큰 값 출력
            max_idx = j
    print(f'#{i+1} {max_idx}')