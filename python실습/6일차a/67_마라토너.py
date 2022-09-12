import sys
input = sys.stdin.readline

n = int(input()) #참가자 수
names = {}

for _ in range((2*n-1)):
    name = input()
    if name not in names: #딕셔너리에 name이 없다면
        names[name] = 1
    else: # name이 있다면 +1
        names[name] += 1 #횟수가 2가 되도록
    
for key, value in names.items(): #key와 value를 쌍으로 묶은 튜플 중에서
    if value % 2 == 1: #두 번 불리지 않은 사람의
        print(key) #이름 출력