import sys
input = sys.stdin.readline

matrix = [list(map(str,input())) for _ in range(8)]

result = 0  #결과값 초기화

for x in range(8): #행
    for y in range(8): #열
        if (x + y) % 2 == 0:
            if matrix[x][y] == 'F' : #하얀 칸에 'F'가 있다면
                result += 1  #+1을 해준다

print(result)

        