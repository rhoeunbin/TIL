t = int(input())

for i in range(t):
    bdpq = list(input())
    reverse = ''

    for j in range(len(bdpq)):

        if bdpq[j] == 'b':
            reverse += 'd'
        elif bdpq[j] == 'd': 
            reverse += 'b'
        elif bdpq[j] == 'p': 
            reverse += 'q'
        elif bdpq[j] == 'q': 
            reverse += 'p'

    print(f'#{i+1} {(reverse[::-1])}')
