word = input().upper()   #대문자로 입력 받기
many = list(set(word))   #중복된 값들 지우기

cnt = []   #빈 리스트 만들기

for i in many: #many 리스트에서
    c = word.count(i)  #입력받은 word 개수 세기
    cnt.append(c)   #빈 리스트에 개수 추가

if cnt.count(max(cnt)) >= 2 : #중복된 값이 2개 이상이라면
    print('?') 
else :
    max_index = cnt.index(max(cnt))  # count 숫자 최대값 인덱스(=위치)
    print(many[max_index])   # count 숫자 최대값 인덱스 print