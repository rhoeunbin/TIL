while True : #반복해서 계속 문장 수행
    A , B = map(int,input().split())
    
    if A + B == 0: #A+B=0일 때 값이 안 나오기 때문에
        break #while문 빠져나가기 
    else:
        print(A+B)
