a, b = input().split()  #map 굳이 쓸 필요 X

a = a[::-1] #역순으로
b = b[::-1]

print(max(a,b))  # a와 b 중 큰 값