t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    in_matrix = list(map(list,zip(*matrix)))

    cnt_0 = []

    for i in in_matrix:
        for j in range(n):
            if i[j] ==1:
                cnt_0.append(i[j:].count(0))
    print(sum(cnt_0))


    T = int(input())
for test_case in range(T):
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for i in range(m)]

    cnt = 0
    for i in range(n):
        floor = m - 1
        for j in range(m-1, -1, -1):
            if box[j][i] == 1:
                cnt += floor - j
                floor -= 1
    print(cnt)