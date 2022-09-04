a, b = map(int,input().split()) #구간의 시작과 끝 입력받기
num = [] #숫자 넣을 수열 리스트(1,2,2,3,3,3...)

for n in range(1, b + 1): #1부터 b까지 수열 만들기
    for i in range(n): 
        num.append(n) #리스트에 n의 값 추가

print(sum(num[a - 1 : b])) # 슬라이싱으로 값 구하기(인덱스위치:2~6)






