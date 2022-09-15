import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip() #오른쪽 공백 제거
    stack = [] #스택

    if sen == '.': #'.'이 나오면 break
        break
    
    for i in sen: #문장 받기
        if i == '(': # (가 나오면 
            stack.append(i) #스택에 ( 추가
        elif i == ')': # )가 나오면
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print('no')
    else:
        print('yes')


    