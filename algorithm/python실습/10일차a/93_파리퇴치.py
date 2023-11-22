t = int(input()) #테스트 케이스 수

for tc in range(t):
    n, m = map(int,input().split()) # 주어지는 n과 m 5 2

    matrix = [list(map(int,input().split())) for _ in range(n)] #이차원 리스트 만들기

    paris = [] #죽일 파리 수가 들어갈 리스트

    for x in range(n-m+1): #가로로 )파리채 휘두를 곳 탐색하기 (n-m+1)*(n-m+1) 범위의 인덱스를 돌기 => 크기가 커지면 탐색할 수 있는 배열 공간이 줄어들어서 조절 
        for y in range(n-m+1): # 세로로 한 칸씩
            cnt = 0 # 잡을 수 있는 파리 수

            for i in range(m): # m X m 범위 내 합 저장(해당 칸에서 파리채 크기만큼)
                for j in range(m):
                    cnt += matrix[x+i][y+j]
            paris.append(cnt)

    print(f'#{tc+1}', max(paris)) #최대값 출력


#
def hap(lst):
    f = 0
    for i in lst:
        f += sum(i)
    return f
for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            ans = max(ans, hap([maps[i + x][j:j + m] for x in range(m)]))
    print(f"#{test_case} {ans}")