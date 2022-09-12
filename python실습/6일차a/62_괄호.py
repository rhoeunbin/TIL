import sys
sys.stdin.readline = input()

t = int(input()) #test case

for i in range(t):
    stack = [] #stack 
    gwal = input() #괄호들 input 받기

    for j in gwal:
        if j == '(': 
            stack.append(j) 
        elif j == ')': 
            if stack :
                stack.pop()
            else :
                print('NO') 
                break 

    else: 
        if not stack:  
            print('YES') 
        else :
            print('NO') 
