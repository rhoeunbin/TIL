x, y = map(str,input().split()) 
#x와 y를 각각 map 함수를 이용해 input 받는다
#[::-1]을 쓰기 위해 str 문자형으로 input 받기

rev_x = x[::-1] #입력받은 x와 y를 뒤집는다
rev_y = y[::-1] #생각해보니 사실 그냥 아래식에 넣어도 됨,,,

rev = str((int(rev_x) + int(rev_y)))
#뒤집은 수를 각각 int형으로 바꾸어 더해준 후 또다시 뒤집기 위해 str로 바꾼다

print(int(rev[::-1])) #뒤집은 숫자를 int형으로 출력한다