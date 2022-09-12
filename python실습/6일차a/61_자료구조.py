import sys
input = sys.stdin.readline

n, m = map(int,input().split()) #첫째 줄에 교과서의 수 : n 교과서 더미의 수 : m
order = True # 정렬이 가능한지

for _ in range(m):
    num = int(input()) #책 교과서 수 input 받기
    book = list(map(int,input().split())) # 책 번호 리스트로 input 받기

    for i in range(num-1): 
        if book[i] < book[i+1]: #리스트의 인덱스 비교, i 인덱스 값이 i+1 보다 작다면
            order = False #정렬 불가능
            break 
    if not order: break # 정렬이 불가능하면 break

if order:
    print('Yes') #정렬 가능하면 Yes
else:
    print('No') # 아니라면 No
# print('Yes' if order else 'No')
