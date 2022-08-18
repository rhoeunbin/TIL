n = int(input())

for i in range(n):
    ox = list(map(str,input())) #OX 값을 리스트로 받음
    # print(ox)
    cnt = 0 #'O'의 개수
    result = 0 # 점수 결과

    for j in ox:
        if j == 'O': # 만약 j가 O라면
            cnt += 1 #'O'의 개수 추가
            result += cnt # 결과에 cnt 값 더하기
        else : #j가 O가 아닐 때
            cnt = 0

    print(result)
