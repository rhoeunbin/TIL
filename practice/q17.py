#17
#word = 'banana'

word=input()
up = ''   #up에 대문자가 쌓임
for i in word : 
    up += chr(ord(i)-32)
print(up, end='')

#강사님 답
word = 'banana'
result = ''
for char in word:
    # 1. 알파벳을 숫자로 바꾸고
    number = ord(char)
    # 2. 그 숫자를 -32를 하고
    number = number-32
    # 3. 다시 숫자를 알파벳으로 바꾼다.
    result += chr(number)
print(result)


for char in word:
    print(chr(ord(char)-32), end='')