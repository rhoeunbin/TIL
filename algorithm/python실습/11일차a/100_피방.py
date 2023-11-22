# import sys

# input = sys.stdin.readline

# n = int(input())
# list_ = []
# num = input().split()
# cnt = 0  # 거절당하는 사람 수

# for i in range(n):

#     if num[i] not in list_:
#         list_.append(num[i])
#     else:
#         cnt += 1

# print(cnt)

# #
# n = int(input())
# seat = list(map(int, input().split()))
# s = len(list(set(seat)))
# print(n - s)

#
N = int(input()) 
PC = [0] * 101  # pc방 자리 => 100보다 작거나 같다
seat = list(map(int, input().split()))  
result = 0 # 거절당한 사람 수

for i in seat:  # 변수가 seat 리스트에 있을때 
    if PC[i] != 0:  # 원하는 자리에 사람이 있으면
        result += 1 # 거절 +1
    else:  # 원하는 자리에 사람이 없다면
        PC[i] += 1  # 사람 자리 +1
print(result)

print(int(input()) - len(set(map(int, input().split()))))