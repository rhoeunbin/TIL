n = int(input()) #숫자 input 받기

queue = list(range(1,n+1)) #input받은 숫자만큼 반복

while len(queue) > 1:
    print(queue.pop(0), end=" ") #제일 위에 있는 카드 버리기
    queue.append(queue.pop(0)) #제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기

print(queue[0]) #제일 위에 있던 카드들 출력