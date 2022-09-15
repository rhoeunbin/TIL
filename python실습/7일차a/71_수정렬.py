import sys
input = sys.stdin.readline

num = [] #숫자리스트

for i in range(int(input())): #숫자 input만큼 반복
    num.append(int(input())) #input 받은 숫자 list에 넣기
    num = sorted(num) # 숫자 정렬

print(*num, sep='\n') #리스트에서 값만 한 줄씩 출력하기 위해서