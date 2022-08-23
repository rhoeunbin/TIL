import sys
input = sys.stdin.readline

N = int(input()) #방의 크기

room = [list(map(str,input())) for _ in range(N)] 

cnt_row, cnt_col = 0,0
row,col = 0,0  #가로, 세로자리

for i in range(N):   
    cnt_row = 0 # 누울 자리 count
    for j in range(N):
        if room[i][j]== '.':
            cnt_row += 1 # . 이 있으면 +1
        else : # .이 아니라면
            cnt_row = 0 
        if cnt_row == 2: # .이 두 개면
            row += 1 # 가로 +1
            

for i in range(N):
    cnt_col = 0
    for j in range(N):
        if room[j][i] =='.':
            cnt_col += 1
        else :
            cnt_col = 0
        if cnt_col == 2:
            col += 1    
            
print(row ,col)   


