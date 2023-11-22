a, b = input().split() # 문자열로 input 받기 => replace를 쓸 거니깐
#replace(바뀌게 될 문자열, 바꿀 문자열)
min_ = int(a.replace('6', '5')) + int(b.replace('6', '5'))  #6은 5로 (최소)
max_ = int(a.replace('5', '6')) + int(b.replace('5', '6'))  #5는 6으로 (최대)

print(min_, max_) 