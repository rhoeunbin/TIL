#2단부터 9단까지 반복하여 구구단을 출력하세요.
#* 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

#x의 범위는 2~9, y의 범위는 1~9이다
#반복할 때 단이 끝날때마다 'x단' 출력
for x in range(2,10) :
    print(f' {x}단 ')
    for y in range(1,10) :
        print(f'{x} x {y} = {x*y}')