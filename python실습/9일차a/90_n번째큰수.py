t = int(input())

for i in range(t):
    num = list(map(int,input().split()))
    num.sort()
    print(num[-3])