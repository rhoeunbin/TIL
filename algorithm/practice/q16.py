#16
#word = 'apple'

word=input()
list = ['a','e','i','o','u']
y=0  #모음이 있을 때  
n=0  #모음이 없을 때

for i in word :
    if i ==list[y] :
        y += 1
    n += 1
print(y)