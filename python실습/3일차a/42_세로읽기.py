board = [] # 칠판에 적힌 문자열을 받을 리스트
len_list = [] # 줄마다 길이를 저장해놓을 변수

for i in range(5): # 가로 5줄 
    board.append(list(input())) # 문자열을 받고 list로 더해준다.
    len_list.append(len(board[i])) # 입력받은 문자열의 길이도 같이 저장한다.
max_len = max(len_list) # 제일 큰 문자열의 길이를 찾아놓는다.

for j in range(max_len): # 세로 우선 순회를 max_len 만큼 한다.
    for i in range(5): # 5줄의 문자열을
        if j < len(board[i]): # 해당 문자열의 길이 이하의 범위일때
            print(board[i][j], end='') # 공백없이 이어서 출력한다.