dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] #다이얼 위치 리스트
d = input() #단어 input 받기
cnt = 0 #필요한 최소 시간 

for i in range(len(d)): # 단어 길이만큼 #0 1
    for j in dial: # j = WXYZ
        if d[i] in j: #만약 WXYZ에 W가 있다면 (예사)
            cnt += dial.index(j)+3 #숫자 1은 2초, 한 칸 옆으로 갈 때마다 1초씩 걸림
    
print(cnt)

