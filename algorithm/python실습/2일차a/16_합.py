n = int(input()) #n은 정수
cnt = 0 #count 0부터 세기

for i in range(1, n+1): # 1 ~ n+1 까지 반복 
    cnt += i  # 1 + 2 + 3 이므로
print(cnt)