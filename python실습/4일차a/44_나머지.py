num = [] ##나누는 값을 넣을 빈 리스트

for i in range(10): #10개의 숫자
    a = int(input()) #숫자 input 받기
    b = a % 42
    num.append(b) #num 리스트에 나눈 값 넣기
    s = list(set(num)) #중복값 없애기

print(len(s)) #리스트의 길이 구하기
