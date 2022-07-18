#문제 19. 숫자의 길이 구하기
number = 123

#123=100+20+3 = 1*100+2*10+3
#while 종료 조건 때까지
#for 반복가능한 것이 있을 때 순회를 하겠다

cnt =0
while number !=0:
    number =number // 10
    cnt += 1
print(cnt)

 