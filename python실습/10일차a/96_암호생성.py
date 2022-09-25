t = int(input()) #테스트 케이스 수

for tc in range(t):
    n, m = map(int,input().split()) # 주어지는 n과 m

    matrix = [list(map(int,input().split())) for _ in range(n)] #이차원 리스트 만들기

    paris = [] #죽일 파리가 들어갈 리스트

    for x in range(n-m+1): #파리채 휘두를 곳 탐색하기 
        for y in range(n-m+1):
            cnt = 0 # 잡을 수 있는 파리 수

            for i in range(m): # m X m 범위 내 합 저장
                for j in range(m):
                    cnt += matrix[x+i][y+j]
            paris.append(cnt)

    print(f'#{tc+1}', max(paris))
