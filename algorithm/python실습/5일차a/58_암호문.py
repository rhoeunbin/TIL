# 0 ~ 999999 사이의 수를 나열하여 만든 암호문이 있다.

# 1. I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
# 위의 규칙에 맞게 작성된 명령어를 나열하여 만든 문자열이 주어졌을 때, 암호문을 수정하고, 수정된 결과의 처음 10개 숫자를 출력하는 프로그램을 작성하여라.


t = 10 #테스트케이스 = 10

for tc in range(1, t+1):
    o_len = int(input()) #원본 암호문 길이
    o_list = list(map(int,input().split())) #원본 암호문
    c_len = int(input()) # 명령어의 개수
    c_list = input().split() #명령어

    i = 0 #I를 기준으로 i를 초기화

    while i <len(c_list): #명령어를 다 돌 때까지 반복
        c = c_list[i] 
        if c == 'I': #명령어에서 I를 기준으로
            x = int(c_list[i+1]) # 0+1
            y = int(c_list[i+2]) # 0+2

            s = c_list[i+3:i+3+y] # 0+3: 0+3+y

            #정방향으로 가면 반대라 s를 역방향[::-1] 아니면 reverse으로 넣고 인덱스 삽입?insert뭐시기,,, 하고 10으로 슬라이싱인데,,
            #원본에서 ?insert(x,숫자)
            for j in s[::-1]:
                o_list.insert(x, int(j))
                
        i += 1 # 0->1, 1->2..
    print(f'#{tc}', *o_list[:10])        
