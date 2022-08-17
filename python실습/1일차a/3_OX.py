n = int(input())

for i in range(n):
    ox = list(map(str,input()))
    # print(ox)
    cnt = 0
    result = 0

    for j in ox:
        if j == 'O':
            cnt += 1 
            result += cnt
        else :
            cnt = 0

    print(result)
