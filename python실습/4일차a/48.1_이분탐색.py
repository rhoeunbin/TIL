n = int(input())
card = list(map(int,input().split()))
card.sort()

m = int(input())
find = list(map(int,input().split()))

def b_s(left, right, target):
    left = 0
    right = n -1
    # start = 0
    # end = len(a)-1

    while left <= right:
        mid = (left + right) // 2
        if target == card[mid]:
            return 1
        elif target < card[mid]:
            right = mid - 1
        else: 
            left = mid + 1
    return 0 
# for i in range(m):
#     if b_s(find[i]):
#         print(1)
#     else:
#         print(0)
for i in range(m):
    print(b_s())