t = int(input()) #test case

for j in range(t) : #test case만큼 반복
    n, k = map(int, input().split()) 
    do_h = list(map(int, input().split())) # 과제 제출한 사람 리스트
    not_h = []   # 과제 제출 안 한 사람 리스트 

    for i in range(1, n+1) :
        if i not in do_h :
            not_h.append(i)
    
    print(f'#{j+1}', *not_h)