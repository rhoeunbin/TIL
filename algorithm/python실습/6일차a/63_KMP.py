name = list(map(str,input().split('-'))) #이름을 받을 리스트를 '-'를 기준으로 input 받음

for i in name: #name 리스트의 모든 값들 중에서
    print(i[0], end='') #인덱스 0 자리의 알파벳 출력