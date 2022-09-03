import sys
sys.stdin = open('소득불균형.txt')

#테스트 케이스를 받아서 평균 이하의 소득을 가진 사람들의 수를 출력


T = int(input()) #전체 테스트 케이스

for i in range(T): #전체 테스트 케이스만큼 반복
    t = int(input()) #T에 대한 테스트 케이스
    n = list(map(int,input().split())) #숫자 리스트를 받는다
    avg = sum(n)/ len(n) #평균 = 합/길이
    cnt = 0 #0부터 count 해준다

    for j in range(len(n)): #숫자 리스트의 길이만큼
        if avg >= n[j]: #해당 인덱스보다 평균이 크다면
            cnt += 1 # +1

    print(f'#{i+1} {cnt}') #f스트링으로 표현


#전에 썼던 코드 => 오히려 잘 씀,,, 구글링 했나봄

t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    sum_= sum(lst)
    total = len(lst)
    avg = sum_/total
    lst2 = []
    for j in range(len(lst)):
        if avg >= lst[j]:
            lst2.append(j)
    print(f'#{i+1} {len(lst2)}')


