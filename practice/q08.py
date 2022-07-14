#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.

numbers = [0, 20, 100, 40]
max_num = numbers[0]
second_num = numbers[0]

#1. 전체 숫자를 반복
for n in numbers :
    #만약에, n이 최대보다 크다면
    if max_num < n:
        #최대값이었던 것을 두번째로 큰 수로 넘기고
        second_num = max_num
        max_num = n
   # elif second_num < n < max_num
   # elif second_num < n and n < max_num
   # second_num =n 
print(second_num)