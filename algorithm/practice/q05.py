#주어진 숫자의 평균을 구하는 코드를 작성하시오.

#3, 10, 20이라는 요소로 구성된 리스트를 numbers라는 변수에 할당
numbers = [3, 10, 20]
#값 초기화
result = 0
a=0
#반복
for num in numbers:
    result += num   #result= result+num  ,합
    a += 1
avg = result /a    
print(avg)