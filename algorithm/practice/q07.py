#주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.

numbers = [-10, -100, -30]
min = numbers[0]
for n in numbers:
    if n > min:
        min = n
print(min)