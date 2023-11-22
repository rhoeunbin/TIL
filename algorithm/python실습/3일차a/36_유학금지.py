cam = ['C','A','M','B','R','I','D','G','E'] #CAMBRIDGE를 리스트에 넣기

word = list(input()) #리스트로 단어 input 받기

# print(word)
for i in range(len(word)): #word 리스트의 길이만큼 반복
    if word[i] not in cam: #cam리스트에 없다면
        print(word[i], end='') #없는 알파벳만 공백으로 출력        

