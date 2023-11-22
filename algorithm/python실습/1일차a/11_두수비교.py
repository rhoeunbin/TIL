a, b = map(int, input().split())

if a < b : # a가 b보다 작으면 <
    print('<')
elif a > b : # a가 b보다 크면 >
    print('>')
else :  # a와 b가 같으면 ==
    print('==')