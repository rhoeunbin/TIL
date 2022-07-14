#주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

count=0
for a in numbers :
    if a == 5 :
        count += 1
print(count)