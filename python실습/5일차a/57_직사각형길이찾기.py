t = int(input())

for i in range(t):
    rec = list(map(int,input().split()))
    rec.sort()

    if rec[0] == rec[1]:
        print(f'#{i+1} {rec[2]}')
    elif rec[1] == rec[2]:
        print(f'#{i+1} {rec[0]}')
    else:
        print(f'#{i+1} {rec[0]}')
