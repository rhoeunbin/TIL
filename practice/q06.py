#주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.

numbers = [0, 20, 100]
#처음값을 미리 넣어놓고 시작
max = numbers[0]
#반복
for n in numbers :
#만약, max 값이 n보다 작으면 바꾼다
    if max< n :
       max = n
print(max)