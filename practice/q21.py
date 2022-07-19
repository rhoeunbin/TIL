#주어진 숫자를 뒤집은 결과를 출력하시오. 
# 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
# number = 1234

#!
n=int(input())
b=(n//1000)+(((n%1000)//100)*10)+(((n%100)//10)*100)+((n%10)*1000)
print(b)

#2
n=int(input())
while n !=0:
    result = n%10
    n = n//10
    print(result, end="")

#3
number = int(input())

while number > 0:
    print(number%10, end='')
    number //= 10