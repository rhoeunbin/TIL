#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

#while문 이용
n = 5
a = 1
result = 1
while(a< (n+1)):
    result *= a
    a += 1
print(result)

#for문 이용
n=5    
result=1
for a in range(1,n+1):
    result *= a
print(result)