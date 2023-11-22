color = {'black': 0,'brown': 1,'red':2 ,'orange' :3,'yellow' :4,'green': 5,'blue': 6,'violet': 7,'grey': 8,'white' :9}
# 각 색에 해당하는 딕셔너리 만들기
a = input() # 각각의 색들 input 받기
b = input()
c = input()

print((color[a] * 10 + color[b]) * (10 ** color[c])) # 인덱스를 사용해 저항값 구하기