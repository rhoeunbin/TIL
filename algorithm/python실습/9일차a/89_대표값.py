num = []

for i in range(10):
    num.append(int(input()))
    
print(sum(num)//10, max(num, key = num.count), sep='\n') #max 함수 key값 이용   


from collections import Counter

for i in range(10):
    num.append(int(input()))
    
cnt = Counter(num)
mode = cnt.most_common(1)
print(mode[0][0])