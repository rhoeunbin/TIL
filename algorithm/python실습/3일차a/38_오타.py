# for i in range(int(input())):
#     p, word = input().split()
#     p = int(p)


t = int(input()) #테스트케이스
for i in range(t): #테스트케이스만큼 반복
    p, words = input().split() #인덱스와 단어 input 받기
    answer = ''

    for idx in range(len(words)): #단어의 길이만큼 반복
        if idx == int(p)-1: #인덱스 위치에서 input 받은 p자리와 같다면
            continue #넘김
        answer += words[idx] # words에 있는 데이터들 그대로 더함
    print(answer)