t = int(input()) #테스트 케이스
tier = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(t) : 
    n, k = map(int, input().split()) #n은 학생수, k는 k번째 학생수
    score = []  #총점 리스트
    
    for j in range(n) : #학생 수만큼
        a, b, c = map(int, input().split())
        sum_ = (a * 0.35) + (b * 0.45) + (c * 0.2) # 총점 계산
        score.append(sum_)

    k_stu = score[k-1]  #k번째 학생의 위치
    score.sort(reverse=True) #점수대로 정렬

    divide = n // 10 #n명의 학생에게 동일하게 학점 주기
    k_score = score.index(k_stu) // divide  #학점에서의 인덱스 구하기

    print(f'#{tc+1} {tier[k_score]}')