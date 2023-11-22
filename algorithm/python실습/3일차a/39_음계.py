num = list(map(int,input().split())) #숫자들을 리스트로 input

if num == sorted(num): #num리스트와 정렬한 값이 같으면
    print('ascending') #오름차순
elif num == sorted(num,reverse=True): #num리스트와 역으로 정렬한 값이 같으면
    print('descending') #내림차순
else: # 둘 다 아니면
    print('mixed') #섞여있음