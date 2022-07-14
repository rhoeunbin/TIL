#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
#apple→pple로

word='apple'
#반복!for
result = '' 
for char in 'apple' :
    #만약 a 일 때
    if char == 'a':
        continue
    else :
        result += char
print(result)         
        #반복문에서 아무것도 안 하고 넘어가는 것? continue
        
word='apple'
result = '' 
for char in 'apple' :
    if char != 'a' : #(continue 모를 때) a가 아닐 때
        result = result + char
print(result)    