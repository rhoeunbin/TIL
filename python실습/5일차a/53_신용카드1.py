import sys
sys.stdin = open('신용카드1.txt')

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))
    even = 0 #짝수
    odd = 0  #홀수

    for j in range(1,16):  #번호가 16자리이기 때문
        if j % 2 !=0:  #홀수이면 *2 한 다음 더하기
            odd += (num[j-1] * 2)
        else :         #짝수이면 그대로 더하기
            even += (num[j-1])
    
    for k in range(t):
        if (odd + even + k) %10 == 0 :
            print(f"#{i+1} {k}")
  