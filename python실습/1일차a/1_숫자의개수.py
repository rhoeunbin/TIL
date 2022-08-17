a = int(input())
b = int(input())
c = int(input())

answer = a * b * c
#리스트로 넣어서 count 하기
answer_list = list(str(answer)) #개수를 세기 위해서 str로 형변환
# print(answer_list)

for i in range(10): #0~9까지
    print(answer_list.count(str(i))) #count는 문자열에서만 쓰기 때문에

