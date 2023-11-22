for num in range(int(input())): #test case를 한 번에 input 받기
    A, B = map(int,input().split()) #정수 A와 B input 받기
    print(f'Case #{num+1}: {A} + {B} = {A+B}')