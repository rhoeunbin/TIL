### πλμλλ¦¬ ν΄μ€

```python
word='banana'
result={}   #λμλλ¦¬ μ΄κΈ°ν
#λ¬Έμμ΄μ λ°λ³΅νλ©΄μ μνλ²³ νλμ©μ΄ char
for char in word :     #char = b,a,b,a,n,a
    #λ§μ½μ κΈ°μ‘΄μ ν€κ° μμΌλ©΄ , 1μΌλ‘ μ΄κΈ°νλ₯Ό νκ³  
    # μ€λ₯ if char in result:
    if char not in result : 
        result[char]=1
    #ν€κ° μμΌλ©΄ ,κΈ°μ‘΄ κ°μ λνκΈ°
    else : 
        result[char] =result [char]+1 
print(result)
    # ν€-κ°μ μ μΆκ°
#result['a']=0
#print(result)
```

```python
word='banana'
result={}
for char in word :
    result[char]=result.get(char,0)+1
    #result[char] : μμΌλ©΄ KeyError
    #result.get(char,0) : μμΌλ©΄ None, κΈ°λ³Έκ°μ μ£Όλ©΄ 0
```



## μλ¬/μμΈ μ²λ¦¬

branches - λͺ¨λ  μ‘°κ±΄μ΄ μνλλλ‘ λμνλμ§

for loops - λ°λ³΅λ¬Έμ μ§μνλμ§, μνλ νμλ§νΌ μ€νλλμ§

while loops - for loopsμ λμΌ, μ’λ£ μ‘°κ±΄μ΄ μ λλ‘ λμνλμ§

function - ν¨μ νΈμΆ μ, ν¨μ νλΌλ―Έν°, ν¨μ κ²°κ³Ό



#### μλ¬ νμΈ λ°©λ²

- print ν¨μ νμ©
- κ°λ° νκ²½ λ±μμ μ κ³΅νλ κΈ°λ₯ νμ©
- Python tutor νμ©
- λμ»΄νμΌ ,λλλ²κΉ 



### Syntax Error - λ¬Έλ² μλ¬

```python
print('hello   #EOL(End of Line)
print(         #EOF(End of File) 
while          #Invalid syntax
5 = 3          #assign to literal : μμ€μ½λμ κ³ μ λ κ°μ λννλ μ©μ΄
              #(μ«μλ λ¬Έμλ₯Ό Literal μ΄λΌκ³  ν¨)
```



## μμΈ(λ¬Έλ² μ€λ₯ X)

```python
10/0 # ZeroDivisionError : 0μΌλ‘ λλ μ μλ€

NameError # namaspace μμ μ΄λ¦μ΄ μμ λ(λ³μ μ μΈ x)
```

### TypeError

```python
1+'1' #'int' and 'str' - μ«μλ λ¬Έμ λν  μ μμ
      #a+bμμ μ€λ₯λλ©΄ κ°μ λ³΄κΈ°!
    
round('3.5') #λ¬Έμμ΄ X, round(number)

divmod()  # ν¨μλ₯Ό νΈμΆ -> λ μ«μλ₯Ό λ°μμ λλ κ²°κ³Όλ₯Ό νλμ ννλ‘ λ°νν΄μ£Όλ ν¨μ => λ κ°μ argument μ£ΌκΈ° 
import random
random.sample() # λ κ°μ νμμ μΈ μμΉ μΈμ μ μ€

divmod(1,2,3) # κ°μ μ΄κ³Ό
import random
random.sample(range(3),1,2)  # κ°μ μ΄κ³Ό

import random
random.sample(1,2)  # μ²«λ²μ§Έ κ°μ μ«μX ,λμλλ¦¬λΌλ©΄ λ¦¬μ€νΈλΌλ λ£μ΄μΌ ν¨
```



### ValueError - νμO, κ°X or μ μ νμ§ μμ κ²½μ°

```python
int('3.5')  #10μ§μλ§ κ°λ₯
range(3).index(6)  #range λ²μμ μμ

empty_list = []
empty_list[2]  #λμ΄μλ μΈλ±μ€λ₯Ό μ£Όμμ λ
```



### KeyError

```python
song = {'iu':'μ’μλ '}  #ν€κ° μμ΄μ λ°μνλ μλ¬
song['BTS']
```



### ModuelNotFounError

> μ‘΄μ¬νμ§ μλ λͺ¨λ inport ν  λ



#### ImportError 

> Moduleμ μμΌλ μ‘΄μ¬νμ§ μλ ν΄λμ€/ν¨μ κ°μ Έμ€λ κ²½μ°

```python
from random 
```



#### IndentationError - μλͺ»λ μ€νμ΄μ€

```python
for i in range(3):
print
```



#### KeyboardInterrupt - μμλ‘ νλ‘κ·Έλ¨μ μ’λ£

```python
while True :
    continue
```



### μμΈ μ²λ¦¬

- try λ¬Έ
  - μ€λ₯ λ°μ κ°λ₯μ±μ΄ μλ μ½λλ₯Ό μ€ν
  - μμΈκ° λ°μ μ νλ©΄, except μμ΄ μ’λ£
- exceptλ¬Έ
  - μμΈκ° λ°μνλ©΄

*μνλ ννλ₯Ό μ§μ  κ΄λ¦¬ κ°λ₯*

```python
try :
    print() 
except ValueError :
    print()
except exception :
    #exception κ°μ₯ λμ λ¨κ³μ μμΈ
#λ³΅μμ μμΈ   
try:
num = input('100μΌλ‘ λλ κ°μ μλ ₯: ')
100/int(num)
except (ValueError, ZeroDivisionError):
print('μ λλ‘ μλ ₯')
```



### μμΈ λ°μ μν€κΈ°

#### Raise -κ°μ λ‘ μμΈ λ°μ

- λ΄κ° μ€μνλ λΆλΆλ€μ λμμ€

- μ²λ¦¬ κ°λ₯ν λΆλΆμ μλμμΌλ‘ λ£μ΄μ€

```python
except ValueError as err :  #μλ¬λ©μΈμ§ λ³Ό μ μμ
```



