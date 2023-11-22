a, b, c = map(int,input().split()) #a,b,c 를 정수형으로 input 받기

if a == b == c: # 세 개의 숫자가 같을 때
    print(10000 + (a * 1000))
elif a == b or b == c: # 셋 중 두 개의 숫자가 같을 때
    print(1000 + (b * 100)) # 같은 수 하나를 b로 설정
elif a == c: # 셋 중 두 개의 숫자가 같을 때 
    print(1000 + (a * 100)) # 같은 수 하나를 a로 설정
else : # 세 개 다 다를 때
    print(max(a, b, c) * 100)