number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
#count += 1  #오류 이유 : 들여쓰기 오류
    count += 1

#print(total // count)  #소수를 print하기 위해서 total / count로 바꾸기
print(total / count)


