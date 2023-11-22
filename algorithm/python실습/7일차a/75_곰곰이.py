n = int(input()) # 사람 수 input 받기

cnt = 0 #곰곰티콘이 사용된 횟수
enter = {} # 들어간 횟수를 넣을 딕셔너리

for i in range(n):
    person = input() #사람 이름 input 받기

    if person == "ENTER": #ENTER 들어오면
        for k,v in enter.items(): # key, value값 불러오기
            if v == 1: #value가 1이면
                cnt += 1 #count +1
        enter={} # 초기화
    else:
        if person not in enter: #딕셔너리에 없다면
            enter[person] = 1

for k,v in enter.items(): 
    if v == 1:
        cnt += 1

print(cnt)
