N, X = map(int,input().split()) #N과 X 정수로 받기
numbers = list(map(int, input().split())) #N개의 정수를 리스트로 input

for num in range(N):
    if numbers[num] < X : # numbers 의 인덱스가 X의 값보다 작을 떄
        print(numbers[num], end = ' ') #해당 인덱스 위치에 해당하는 값 출력, 공백을 두고