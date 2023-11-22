N = int(input()) #입력 받기

han = 0 #한수 지정
for i in range(1, N+1) :
    if i <= 99: #99까지는 한수이니깐 +1
        han += 1 
    else : #99 이후
        a = list(map(int, str(i))) #99이후의 숫자 넣기
        if a[0] - a[1] == a[1] - a[2] : # 백의 자리- 십의자리 = 십의 자리 - 일의 자리
            han += 1 #수가 같다면 한수 +1
print(han)