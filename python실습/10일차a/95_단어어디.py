t = int(input())

for tc in range(t):
    n, k = map(int,input().split()) #단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 
    matrix = [list(map(int,input().split())) for _ in range(n)] # n의 길이만큼의 이차원 리스트

    res = 0 # 들어갈 수 있는 단어의 개수 count

    for x in range(n): # 가로
        cnt = 0 # 들어갈 수 있는 자리 = 0
        for y in range(n):
            if matrix[x][y] == 0: # 자리가 0 일 때
                if k == cnt: #단어의 길이 = cnt
                    res += 1 # 들어갈 수 있는 단어의 개수 +1
                cnt = 0 # k가 0이 아닐 때는 cnt = 0
            else : 
                cnt += 1 # 자리가 1일 때
        if k == cnt: 
            res += 1 

    for y in range(n): # 세로
        cnt = 0 
        for x in range(n):
            if matrix[x][y] == 0:
                if k == cnt:
                    res += 1
                cnt = 0
            else : 
                cnt += 1
        if k == cnt:
            res += 1

    print(f'#{tc+1}', res)

                