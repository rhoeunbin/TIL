import sys 
input = sys.stdin.readline

hear = [] #듣도 못한 사람 리스트
see = [] #보도 못한 사람 리스트

n, m = map(int,input().split())
#n은 듣도 못한 사람,m은 보도 못한 사람
for i in range(n):
    hear.append(input().strip()) #개행 제거하고 값 추가
for j in range(m):
    see.append(input().strip())

# print(hear, see)
#중복이 없으면 set

li = sorted(list(set(hear) & set(see))) # &을 사용하면 교집합, 정렬하기

print(len(li), *li, sep='\n')
