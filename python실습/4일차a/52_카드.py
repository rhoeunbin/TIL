import sys 
input = sys.stdin.readline

n = int(input()) # 카드의 개수
num = {} #카드가 들어갈 딕셔너리

for i in range(n):
    c = int(input()) #카드값
    if c in num: #카드값이 이미 딕셔너리에 있으면 
        num[c] += 1 #개수에 1 더하기
    else : #없으면
        num[c] = 1 #개수 세기

num = sorted(num.items(), key = lambda x :(-x[1], x[0])) 
# items를 이용해 키-값 뽑기, sorted를 사용해 리스트로 돌려주기, 반대로 정렬
#print(num) [(1, 3), (2, 2)]
print(num[0][0]) #리스트 첫번재 인덱스의 첫번째 값




