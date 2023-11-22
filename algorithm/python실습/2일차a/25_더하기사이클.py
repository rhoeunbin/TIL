N = int(input())
# print(N)
new = N #input과 나와야 하는 결과 설정
cycle = 0 #cycle한 횟수 세기

while True :
    f = new // 10 #십의 자리- 몫을 반환
    s = new % 10 #일의 자리 - 나머지 반환
    num = (f + s) % 10
    new = (s * 10) + num # 새로운 숫자 
    cycle += 1 
    if (new == N): #두 숫자가 같아질 때
        break #끝내기
print(cycle)


