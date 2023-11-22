#짝수랑 홀수일 때 따로 
n = int(input())

for i in range(1, n+1):
    if i % 2 ==0 : # 짝수일 때
        print(' *' * n)
    else: # 홀수일 때
        print('* ' * n)
