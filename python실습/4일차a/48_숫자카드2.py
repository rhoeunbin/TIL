n = int(input())
card=list(map(int,input().split()))
m = int(input())
find =list(map(int,input().split()))

count_ = []
cnt = 0

for i in range(n):
    for j in range(m):
        if card[i] == find[j]:
            cnt += 1
        else :
            cnt = 0
        count_.append(cnt)
print(count_)



# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10


    

