import sys
input = sys.stdin.readline

# 직접 푼 것
n = int(input())  #참가자 수

f = [] #첫번째 점수 리스트
s = [] #두번째
t = [] #세번째

for _ in range(n): #n만큼 반복
    a, b, c= map(int,input().split()) #공백을 포함한 값 input
    f.append(a) #첫번째 점수를 f 리스트에 넣기
    s.append(b)
    t.append(c)

for i in range(n): 
    result = 0
    if f.count(f[i]) == 1: #개수가 1개면
        result += f[i] # 점수 더하기
    if s.count(s[i]) == 1:
        result += s[i]
    if t.count(t[i]) == 1:
        result += t[i]
    print(result)


# 강의 보고
n = int(input())
#점수리스트 = [0,0,0,0,0]
col_list = [] #열 리스트
score_list = [0] * n
list_ = []

for _ in range(n):
    list_.append(list(map(int, input().split())))
for x in range(3):
    col = [] #열
    for y in range(n):
        col.append(list_[y][x])
    col_list.append(col)

for x in range(3):
    col = col_list[x] #열 = 열 리스트[x]
    for y in range(n):
        # 친구의 점수
        score = col[y]  #점수 = 열[y]
        # 친구의 점수가 리스트에서 1개일 때
        if col.count(score) == 1:
            # 친구의 점수가 증가
            score_list[y] += score
print(*score_list,sep = '\n')