#1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

#while문 이용
a=0
n=10	
#초기값
result=0
user_input = int(input())
while a < user_input :
	a += 1  #a는 1씩증가  
	result += a   # result = result + a
print(result)

#for문 이용
n=10	
result=0
for a in range(n+1):
    result += a 
print(result)