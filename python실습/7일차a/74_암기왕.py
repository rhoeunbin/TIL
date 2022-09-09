import sys
input = sys.stdin.readline

for _ in range(int(input())): #test case만큼 input 받기
    n = int(input()) #‘수첩 1’에 적어 놓은 정수의 개수
    num1 = set(map(int,input().split())) #list로 했다가 시간초과가 나서 set으로 바꿈
    m = int(input()) #‘수첩 2’에 적어 놓은 정수의 개수 M
    num2 = list(map(int,input().split())) #‘수첩 2’에 적어 놓은 정수들

    for i in num2: #수첩2에서
        if i in num1: #i가 수첩1에도 있으면
            print(1) 
        else:
            print(0)