for i in range(int(input())): #test case만큼 반복
    a,b= map(int,input().split()) #순위
    p = 0 # 상금
    if a == 0:
        pass
    elif a == 1: #1명 
        p += 5000000 #500만원
    elif a <= 3: #3명 이상(2등)
        p+=3000000 # 300만원
    elif a <= 6:
        p += 2000000
    elif a <= 10:
        p += 500000
    elif a <= 15:
        p += 300000
    elif a <= 21:
        p += 100000
    else: # 아니라면 pass
        pass
    
    if b == 0: #b=0이면 pass
        pass
    elif b == 1: #1명이면 
        p += 5120000 #512만원
    elif b <= 3: #3명 이상이면
        p += 2560000 #256만원
    elif b <= 7:
        p += 1280000
    elif b <= 15:
        p += 640000
    elif b <= 31:
        p += 320000
    else:
        pass
    print(p)   