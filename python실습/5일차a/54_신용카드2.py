import sys
sys.stdin = open('신용카드2.txt')

t = int(input())

for i in range(t):
    n = input()
    num = n.replace('-','')

    if num[0] == '3' or num[0] == '4' or num[0] == '5' or num[0] == '6' or num[0] == '9':
        if len(num) == 16:
            print(f'#{i+1} 1')
        else:
            print(f'#{i+1} 0')
    else:
        print(f'#{i+1} 0')