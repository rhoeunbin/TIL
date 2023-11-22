#
n = int(input())
while True:
    if len(str(n)) == str(n).count("4") + str(n).count("7"):
        print(n)
        break
    n -= 1

#
N = int(input())
gold_minsu = ['4', '7']
cnt = 0
find = 0

while find == 0:
    check = 0
    for i in str(N - cnt):
        if i not in gold_minsu:
            cnt += 1
            continue
        else:
            check += 1
            if len(str(N - cnt)) == check:
                find = 1
                print(N - cnt)
                break