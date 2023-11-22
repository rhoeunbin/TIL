result = [] # 점수가 들어갈 리스트

for i in range(5): # 5명만큼 반복
    score = list(map(int,input().split())) #점수를 score 리스트에 넣기
    result.append(sum(score))  #result 리스트에 더한 합계인 score 추가

print(result.index(max(result))+1, max(result))
#max(result)+1 => 인덱스 값이 0부터 시작이므로 참가자 번호는 +1 해야함