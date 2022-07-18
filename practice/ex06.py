N = 10
answer = ()
#오류 이유 : ()로 이루어진 튜플은 값 수정이나 삭제, 추가 불가능
# append()함수는 []로 리스트를 만들어야 함
for number in range(N + 1):
    answer.append(number * 2)
print(answer)

#수정  
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)
print(answer)