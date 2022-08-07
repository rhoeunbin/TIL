### 제어문

- 파이썬은 위에서부터 아래로 순차적으로 명령 수행
- 특정 상황에 따라 코드를 선택적으로 실행하거나 계속하여 실행(반복)하는 제어가 필요
- 제어문은 순서도(flow chart)로 표현 가능



### 조건문

>  참/거짓을 판단할 수 있는 조건식과 함께 사용

- expression에는 참/거짓에 대한 조건식

```python
if < expression > :
    #Run this Code block(참)
else: #선택적
    #Run this Code block(거짓)
```

```python
a = -10
if a >= 0 ;
    print('양수')
else:
    print('음수')
pirnt(a)    #'음수 -10' 출력
```



```python
#홀수인지 확인하는 코드?
#2를 나눈 나머지가 1이냐?

num = int(input())
if num % 2 == 1:
    print('홀수')
else:
    pirnt('짝수')
    
*TypeError가 뜰 때 확인해보기 Print(num, type(num))
```



### 복수 조건문

> elif (else lf의 줄임말)

**else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건 불가능**

**조건문에서 else는 생략 가능**

```python
dust = 100
if dust > 150 :
    print('매우 나쁨') 
elif dust >= 80 :
    print('나쁨')
elif dust > 30 :
    print('보통')
else :
    print('좋음')
    
#굳이 범위를 정할 필요는 없다(위에서부터 아래로 실행하기 때문)
```



### 중첩 조건문

> 들여쓰기를 유의하면 중첩 가능

```python
if <expression> : 
    print()
    if <expression> :
        print()
else :
    print()
```



#### 조건 표현식

```python
num = -10

#1. 양수면 그대로
if num >= 0:
    valie = num
else:
    value = -num
print (num, value)

# 조건 표현식 코드
value = num if num >= 0 else -nums
```

![화면 캡처 2022-07-12 102722](C:\Users\shgus\OneDrive\Desktop\화면 캡처 2022-07-12 102722.png)

```python
num = 2
if num % 2:
    result = '홀'
else:
    result = '짝'
print(result)

#위와 동일한 조건 표현식
num = 2
result = '홀' if num % 2 else '짝'
print(result)
```



---

### 반복문

> 특정 조건을 도달할 때까지, 계속 반복



#### While문

- 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야함
- true일 때는 무한히, False일 때는 0번

```python
a = 0
while a < 5:
    print(a)
    a += 1     #종료 조건
print('끝')    #5번
```

**참고 사이트*[pythontutor](https://pythontutor.com/)

**합을 구하는 result의 초기값 : 0**

**곱을 구하는 result의 초기값 : 1**

```python
#1부터 사용자가 입력한 양의 정수까지의 총합
#처음 시작 값
n = 0
#0부터 더하기 위해서
result = 0
#user_input 값 (사용자가 입력한 양의 정수)
user_input = int(input())

while n < user_input :  #n이 만약 2라면
    n += 1   #n은 1씩 증가  n이 3이 되고
    result += n  #result에 n을 더하기  3에서 계속 더하게 됨
print(result)
# 둘의 차이? 실행되는 것에 따라 다르다! 어려우면 하나씩 출력해보기
while n <= user_input :  #n이 2라면
    result += n  #2부터 더하게 됨
    n += 1
print(result)
```



#### for 문

- 시퀀스(string, tuple, list, range)를 포함한 반복가능한 객체를 모두 순화하면 종료(별도의 종료조건이 필요없다)

```python
for <변수명> in <iterable> :
    #코드블럭
```

```python
#사용자가 입력한 문자를 한 글자씩 세로로 출력
chars = input()   #hi

for char in chars:
    print(char)
    #h
    #i
```

```python
#range를 활용하여 한 글자씩 출력
chars = input()
#index[0]
#index[1]...

for idx in range(len(chars)) # 0부터 원하는 숫자까지(idx = index)
    print(chars[idx])   # index를 기준으로 순회를 한다
    #h
    #i
```



#### 딕셔너리 순회

- 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grades = {'john':80, 'eric' : 90}
for name in grades: 
    print(name)        #키 데이터만 나옴 john eric
    
    print(name, grades[name])  #john 80 eric 90
    #1 print('john',grades[john])
    #2 print('eric',grades[eric])
    
```



### 반복문 제어

- break
  - 반복문 종료

```python
n = 0
while True : 
    if n == 3:
        break
    print(n)
    n += 1
#0
#1
#2

for i in range(10):
    if i > 1:
        print('0과 1만 필요')
        break
    print(i)
#0
#1
#0과 1만 필요
```

  

- continue
  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

```python
fo i in range(6):
    if i % 2 == 0:
        continue
    print(i)
#1
#3
#5 짝수일 때는 실행 안 되고 넘어감
```



- for- else
  - 끝까지 반복문을 실행한 이후에 else 실행
    - break를 통해 중간에 종료되는 경우 else는 실행 

```python
for char in 'apple':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없음')       
    #b가 없음
```

