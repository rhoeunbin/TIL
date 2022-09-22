import sys
input = sys.stdin.readline

for i in range(int(input())): #input만큼 반복
    sen = list(input().split()) #문장이 들어갈 리스트 input 받기
    res = []
    for s in sen:  #변수 s가 리스트에 있다면
        res.append(s[::-1])  #문자열 뒤집기
    result = ' '.join(res) #리스트를 문자열로 합치기
    print(res)