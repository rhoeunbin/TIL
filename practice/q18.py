#18
word = 'banana'
dic={}

for i in word :
    dic[i] = 0  #초기값
    for j in word :
        if j == i:   # 같은 알파벳이면 +1
            dic[i] += 1
for key, value in dic.items():
    print(key,value)