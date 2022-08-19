N, X = map(int,input().split())
numbers = list(map(int, input().split()))

for num in range(N):
    if numbers[num] < X :
        print(numbers[num], end = ' ')