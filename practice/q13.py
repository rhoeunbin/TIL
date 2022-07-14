#주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

#1. 내가 푼 방법
#word = 'apple'
word = input()
print(word[::-1])

#2
word='apple'
result = ''
for char in word :
     result = result + char
print(result)   #apple  

for char in word :
     result = char +result   # 거꾸로 출력
print(result)   #elppa


#3 index
#익숙해질수록 나중에 알고리즘 코드 풀기 좋다
word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i-1], end='')