n = int(input())

for i in range(1, n+1): #1부터 n+1까지(i값을 곱해야 하므로)
    print(' '*(n-i) + '*'*i) 
    # 공백 - 4 3 2 1 0
    # *    - 1 2 3 4 5