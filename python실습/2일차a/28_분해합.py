N = int(input()) #N은 정수

for M in range(1, N + 1):
    list_ = list(map(int, str(M)))  #M은 N의 생성자
    # str(M) - M인 숫자를 문자열로 만들어줌
    # map(int, str(M)) - 문자열로 되어있는 각 자릿수를 정수로 변경
    # ex) 234->2,3,4로 바꿈
    result = M + sum(list_)  #i와 리스트의 합은 결과
    if N == result :  #input 받은 값이랑 result 가 같으면 
        print(M) # 그 값을 출력
        break 
else : #생성자가 없는 경우
    print('0')