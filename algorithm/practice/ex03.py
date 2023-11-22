numbers = input().split()
print(sum(numbers)) 
#오류 이유 : TyperError로 int 삽입

numbers = map(int,input().split())
print(sum(numbers)) 
