t = int(input()) #test case

for _ in range(t):
    a, b = map(int,input().split(',')) #,로 구분할 때 ',' 사용
    print(a+b)