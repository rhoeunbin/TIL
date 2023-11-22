mush = [] #버섯 점수 리스트
score = 0 #점수

for i in range(10): #10개의 점수만큼 반복
    mush.append(int(input())) #10개의 점수를 버섯 리스트에 넣기

for j in mush : #버섯 점수 리스트에 있다면
    score += j # 점수에 추가
    if score >= 100: #점수가 100보다 크면 
        if score - 100 > 100 - (score - j):  #두 값의 절대값 비교해서
            score -= j #그 값 빼기
        break
print(score)