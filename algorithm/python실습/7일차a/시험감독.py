import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b, c = map(int,input().split())
answer = 0

for i in range(n):
    if a[i] > b: #인덱스 값보다 총 감독이 감독할 수 있는 응시자 수보다 적을 때
        a[i] -= b
        answer += 1 #총 감독수 
        if a[i] % c == 0: # 나머지 반환
            answer += a[i] // c
        else:
            answer += a[i] // c + 1 # 몫을 반환
    else:
        answer += 1 # 적어도 한 명은 있어서

print(answer)




