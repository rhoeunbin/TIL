### python 함수(function)

> input을 주면 output이 나오는 것

```python
word = 'happy!'
count=0
for char in word:
    count = count+1     #len(happy!)
```

```python
numbers = [3, 10 ,20]
result = 0
for number in numbers :
    result += number        #sum([3, 10, 20])
```



```python
#3, 10, 20이라는 요소로 구성된 리스트를 numbers라는 변수에 할당
numbers = [3, 10, 20]
#값 초기화
result = 0
a=0
#반복
for num in numbers:
    result += num   #result= result+num  ,합
    a += 1
avg = result /a    
print(avg)

#= print(sum(numbers)/len(numbers))
```

- 함수
  - 특정한 기능을 하는 코드의 조각
  - 특정 명령을 수행하면서 

*파이썬 자습서 활용*

[python내장함수](https://docs.python.org/ko/3/library/functions.html?highlight=%EB%82%B4%EC%9E%A5)

- 사용자 함수

```python
def function_name
    #code block
    return returnin_value
```

*코드 중복 방지, 재사용 용이*

#### 선언 및 호출

- 함수의 선언은 def 키워드 활용

- 들여쓰기를 통해 Function body 작성

- 함수는 parameter를 넘겨줄 수 있음

- 동작 후에 return 사용해 결과값 전달



```python
def foo() :        foo() #호출(소괄호)
    return True
#정의
#1. def
#2. 함수 이름 :add
#3. Input :  a,b
def add(a, b) :
    #4. return : 값을 반환
    return a+b

def minus(a, b) :
    return a-b
#호출
print(add(5, 10))  #a=5,b=10이 들어가고 코드 종료되고 minus 코드 실행
print(minus(10, 5))
```

```python
#내장 함수 호출
print(sum([1,2,3]))
```

```python
n1= 0
n2= 1

def func1(a,b): #3 func1(a,5) 대입
    return a+b  
def func2(a,b): #4 func(5,b)대입
    return a-b
def func3(a,b): #2. func3으로 와서 계산
    return func1(a,5) + func2(5,b)

result = func3(num1,num2) #1. n1과 nu2 적용
print(result)    #5. 결과값 9
```



### 함수의 결과값(output)

#### return

- 함수는 반드시 1개만 return

- 함수는 return과 동시에 실행 종료

```python
def minus_and_add(x,y):
    return x-y
    return x+y    #실행X
#Tuple(튜플)로 묶어서 반환 
```

*print(result, type(result)) 해보기*

**print 함수는 NoneType**

```python
a = print('hi')
print(a, type(a))  
#None <class 'Nonetype'>
#출력만 해주고, return 값은 없다 
```

---

### 함수의 입력(Input)

- parameter : 함수를 실행할 떄 ,함수 내부에서 사용되는 식별자
- argument : 함수를 호출 할 때 함수의 parameter를 통해 전달되는 값, 넣어주는 값

```python
def func(apple) : #parameter : apple
    return apple

func('fruit')   #argument: 'fruit'
```



##### func_name(argument)

- 필수 argument : 반드시 전달되어야 하는 argument

- 선택 argument : 값이 전달하지 않아도 되는 경우, 기본 값이 전달



#### positional argument 

>  위치에 따라   (위치는 기본)

```python
def add(a,b):    add(3,4)
    return a+b
```



#### keyword argument : 

>  직접 변수의 이름으로 특정 argument 전달 가능

​        **keyword 다음에 positional 활용 불가능**

```python
def add(a,b):        add(a=3,b=5)  -> add(a=3,5)는 불가능 키워드가 먼저 나올 수는 없음
    return a+b       add(3, b=5)
```



#### default arguments values  

> 기본값을 지정하여 함수 호출시 argument 값을 설정 안 해도 됨

```python
def add(a, b=0) :  #b=0(기본값 지정) //  add(2)  #2
    return a+b                        add(2,5)   #7
```



```python
# sep는 기본값이 ''(공백)으로 정의되어 있음
print ('hi', 'hello')  
#키워드로 sep를 바꿔서 호출 가능
print ('hi', 'hello', sep='-')  
#hi-hello
```



#### 정해지지 않은 개수의 arguments

> 몇 개의 arguments를 받을지 모를때

```python
#정해지지 않은 개수의 positional argus
def my_add(*numbers) :             #*args
    #내부적으로 numbers가 tuple
    return numbers
result=my_add(1,2,3)
print(result, type(result))  #튜플 : 값을 변경할 수 없다

#정해지지 않은 개수의 keyword argus
def my_func(**kwargs):
    return kwargs
result=my_func(name='길동', age='100', gender='M')
print(result, type(result))  #딕셔너리

```

---

### 함수의 범위(scope)

> 함수는 코드 내부의 local , scope으로 구성되고 그 외의 공간인 global scope로 구성

*함수는 독립적인 scope를 가지고 있음*

```python
def foo():
    a=1
    
foo()   #글로벌영역에 정의된 함수 밖에 없으므로 오류가 난다
print(a)
```

- built-in scope : 원래 있던 함수들 ex) print, sum, len,,

- global scope : 직접 정의된 건, 인터프리터가 끝날때까지 ex) a=3

- local scope : 함수가 호출될 때 생성되고, 종료될 때 사라짐 ex)def



#### 이름 검색 규칙

```python
sum= 5
print(sum[1,2,3])
#bulit-in scope에 sum 함수가 있었음
#global scope에 sum이름의 변수를 만들었음
#찾을때 L→E→G→B Rule 순서로 이름 찾아냄
```

local →enclosed→ global→ built-in 



#### map(function,iterable)

> 특정한 함수를 반복적으로 적용하고 싶을 때

```python
numbers=['1','2','3']
#숫자를 바꿔서 쓰고 싶다?
#리스트를 숫자로 형 변환은 불가능
#다만, 숫자 형태의 문자로 변환 가능
#n=int(numbers) X

#가능! 그런데 100개, 1000개는?
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
new_numbers = [a,b,c]

#반복문
new_numbers=[]
for number in numbers :
    new_numbers.append(int(number))
print(new_numbers)

#map 사용!!!!!
numbers=['1','2','3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2)  # <map object at 0x15515155> : 이미 함수가 모두
print(lise(new_numbers))   #리스트로 형변환해서보면 바뀌어 있다.(보기 위해서 바꾼 것일뿐 반드시 list로 바꿔야 하는 것은 아님)
```

```python
#직사각형의 넓이를 구해라, 세로 n 가로 m
#input예시 10 20

n, m = map(int, input().split()) 
#input() 타입- 항상 string(문자열)
#문자열split() 내가 구분값을 기준으로 쪼개갰다. 반환 결과는 항상 리스트
# int(함수)=> 문자열로 받은 것은 각각 공백을 기준으로 리스트로 쪼갰다  리스트[10,20]
# map => 어떤 함수를 반복가능한 것들의 요소에 모두 적용시킨 결과
#(int 함수를 input().split()리스트의 모든 요소에 적용한 결과)

#=> n,m = [10,20]
print(n*m)   #200
```

```python
#내장함수를 10을 다 더해주는 함수가 있다
def plus10(n):
    return n+10

numbers = [10,20,30]
new_numbers = list(map(plus10), numbers)
#list를 안 하고 print(map(plus10), numbers)로 출력시 map object 어쩌구로 나옴
print(new_numbers)   #[20, 30, 40]
```



#### 오늘 배운 것 한눈에 정리

![](https://github.com/rhoeunbin/TIL/blob/master/220713/python%20%ED%95%A8%EC%88%98.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-07-07%20175335.png)

