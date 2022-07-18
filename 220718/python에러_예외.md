### 📃딕셔너리 해설

```python
word='banana'
result={}   #딕셔너리 초기화
#문자열을 반복하면서 알파벳 하나씩이 char
for char in word :     #char = b,a,b,a,n,a
    #만약에 기존의 키가 없으면 , 1으로 초기화를 하고 
    # 오류 if char in result:
    if char not in result : 
        result[char]=1
    #키가 있으면 ,기존 값에 더하기
    else : 
        result[char] =result [char]+1 
print(result)
    # 키-값의 쌍 추가
#result['a']=0
#print(result)
```

```python
word='banana'
result={}
for char in word :
    result[char]=result.get(char,0)+1
    #result[char] : 없으면 KeyError
    #result.get(char,0) : 없으면 None, 기본값을 주면 0
```



## 에러/예외 처리

branches - 모든 조건이 원하는대로 동작하는지

for loops - 반복문에 진입하는지, 원하는 횟수만큼 실행되는지

while loops - for loops와 동일, 종료 조건이 제대로 동작하는지

function - 함수 호출 시, 함수 파라미터, 함수 결과



#### 에러 확인 방법

- print 함수 활용
- 개발 환경 등에서 제공하는 기능 활용
- Python tutor 활용
- 뇌컴파일 ,눈디버깅 



### Syntax Error - 문법 에러

```python
print('hello   #EOL(End of Line)
print(         #EOF(End of File) 
while          #Invalid syntax
5 = 3          #assign to literal : 소스코드의 고정된 값을 대표하는 용어
              #(숫자나 문자를 Literal 이라고 함)
```



## 예외(문법 오류 X)

```python
10/0 # ZeroDivisionError : 0으로 나눌 수 없다

NameError # namaspace 상에 이름이 없을 때(변수 선언 x)
```

### TypeError

```python
1+'1' #'int' and 'str' - 숫자랑 문자 더할 수 없음
      #a+b에서 오류나면 값을 보기!
    
round('3.5') #문자열 X, round(number)

divmod()  # 함수를 호출 -> 두 숫자를 받아서 나눈 결과를 하나의 튜플로 반환해주는 함수 => 두 개의 argument 주기 
import random
random.sample() # 두 개의 필수적인 위치 인자 안 줌

divmod(1,2,3) # 개수 초과
import random
random.sample(range(3),1,2)  # 개수 초과

import random
random.sample(1,2)  # 첫번째 값은 숫자X ,딕셔너리라면 리스트라도 넣어야 함
```



### ValueError - 타입O, 값X or 적절하지 않은 경우

```python
int('3.5')  #10진수만 가능
range(3).index(6)  #range 범위에 없음

empty_list = []
empty_list[2]  #넘어서는 인덱스를 주었을 때
```



### KeyError

```python
song = {'iu':'좋은날'}  #키가 없어서 발생하는 에러
song['BTS']
```



### ModuelNotFounError

> 존재하지 않는 모듈 inport 할 때



#### ImportError 

> Module은 있으나 존재하지 않는 클래스/함수 가져오는 경우

```python
from random 
```



#### IndentationError - 잘못된 스페이스

```python
for i in range(3):
print
```



#### KeyboardInterrupt - 임의로 프로그램을 종료

```python
while True :
    continue
```



### 예외 처리

- try 문
  - 오류 발생 가능성이 있는 코드를 실행
  - 예외가 발생 안 하면, except 없이 종료
- except문
  - 예외가 발생하면

*원하는 형태를 직접 관리 가능*

```python
try :
    print() 
except ValueError :
    print()
except exception :
    #exception 가장 높은 단계의 예외
#복수의 예외   
try:
num = input('100으로 나눌 값을 입력: ')
100/int(num)
except (ValueError, ZeroDivisionError):
print('제대로 입력')
```



### 예외 발생 시키기

#### Raise -강제로 예외 발생

- 내가 실수하는 부분들을 도와줌

- 처리 가능한 부분을 의도상으로 넣어줌

```python
except ValueError as err :  #에러메세지 볼 수 있음
```



