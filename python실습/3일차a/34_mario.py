mush = [] #버섯리스트
score = 0

for i in range(10): #10개의 점수만큼 반복
    mush.append(int(input()))

for j in mush :
    score += j
    if score >= 100: #점수가 100보다 크면 
        if score - 100 > 100 - (score - j):  #두 값의 절대값 비교
            score -= j
        break
print(score)