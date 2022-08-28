import sys 
input = sys.stdin.readline

book = [] #book 리스트 받아옴

for i in range(int(input())): #책의 개수 input, 책의 개수만큼 반복
    b = input() #책 이름 input
    book.append(b) #책 이름들 리스트에 넣기
# print(book)
book.sort() # 정렬
c = book.count #개수 세기
print(max(book, key = c)) #베스트 셀러 구하기
#key 인자는 list.sort() 에 사용되는 것처럼 단일 인자 순서 함수를 지정