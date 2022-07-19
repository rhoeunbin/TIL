#정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
number = 135
cnt = 0 
result = 0
while number !=0:
    number =number // 10 #반복마다 10의 정수로 나누기
    cnt += 1
    result += cnt
print(result)
#-> 다른 숫자들은 못 구하고 해당 문제만 가능

#다른 방법 = 형변환하기
number = int(input())
result = 0
for i in str(number):
    result += int(i)
print(result)