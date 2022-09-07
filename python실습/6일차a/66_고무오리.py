stack = [] #고무오리 리스트

while True : #while문을 반복문
    du = input() #고무오리 디버깅 데이터 입력

    if du == '문제': #만약 '문제'가 들어오면
        stack.append('O') # 맞다는 표시 추가

    elif du =='고무오리': #고무오리인데
        if not stack: #리스트에 없다면
            stack.append('문제') # 두문제 추가
            stack.append('문제')
        else: #고무오리가 리스트에 있다면
            stack.pop() # 그 값 지우기
    elif du == '고무오리 디버깅 끝': #이 나오면 break
        break

if not stack: #모든 문제가 해결되면(값이 없으면)
    print('고무오리야 사랑해')
else: # 해결되지 않으면 (값이 없다면)
    print('힝구')

