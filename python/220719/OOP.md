### OOP

>  객체 지향 프로그래밍(Object Oriented Program)

- 파이썬은 모든 것이 객체(Object)

- 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법
- 현실 세계를 프로그램 설계에 반영(추상화)



**특징**

- 타입 : 어떤 연산자(operator)와 조작(method)이 가능한가(각자 다름)

- 속성(attribute) : 어떤 상태(데이터)를 가지는가

- 조작법(method) : 어떤 행위(함수)를 할 수 있는가



**객체는 특정 타입(클래스)의 인스턴스(사례)**

<class>'list'

✨클래스 - 사람 - 리스트-str

✨인스턴스 -  iu -  [1,2,3]-'123'



*클래스 내부의 정의된 함수=>메소드(method)*



✍*객체 지향이 되면 데이터가 주가 되고*

*for문 등으로 input을 하면 데이터가 주가 아닌 흘러다님*



*sum은 함수*

*[].sort()는 메서드(리스트가 쓸 수 있는 것이기 때문)*

```python
name = '홍길동'
#name은 str 클래스의 instance(값)인 '홍길동'을 담는 변수일 뿐이다
```



```python
my_list = [1,2,3]
#리스트.sort()
#리스트의 데이터를 직접 정렬
my_list.sort()

my_list = [1,2,3]
#리스트는 sorted 함수의 인자로 전달될 뿐,
sorted(my_list)
```



```python
#클래스 정의
Class MyClass:   #CamelCase : 클래스 / snake_case: 변수나 함수
    pass
#인스턴스 생성
my_instance = MyClass()
#메서드 호출
my_instance.my_method()
#속성
my_instance.my_attribute
```

책 : 개발자로 먹고 사는 법



**모든 클래스는 type, 모든 인스턴스는 클래스**

**파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스**

- 클래스 : 객체들의 분류(class)
- 인스턴스 : 하나하나의 실체/예(instance)
- 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 샅애/데이터를 의미
- 메소드 :  특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수) - 클래스 내부에 정의된 함수



#### 객체 비교하기

- == : 객체가 동등한 경우 True
- is : 동인한 객체를 가리키는 경우 True

```python
a = [1,2,3]  #값은 같은데 주소는 다름
b = [1,2,3]

print(a == b, a is b)
#True False

a = [1,2,3] #주소 자체가 들어감
b = a
print(a == b, a is b)
#True True 실제로는 같은 객체이기 때문에
```

```python
a = [1,2,3]
b = a
b[0] = 'hi'

print(a)  #1,2,3
print(b)  #hi,2,3

#둘 다 hi,2,3  => 변수는 메모리 주소값으로 되어 있다!!!(값이 저장된 게 아님)
```



- 인스턴스 변수 : 인스턴스가 가지고 있는 속성
- 인스턴스 메소드 : 인스턴스 조작을 위한 메서드
  - 호출 시,첫번쨰 인자로 인스턴스 자기자신(self) 이 전달됨



#### self

- 인스턴스 자기자신

- 매개변수 이름으로 self를 첫번째 인자로 정의(암묵적 규칙)



##### 생성자 매소드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
- 이름을 바꿀 수 없음

```python
class Person :
    #생성자! 인스턴스가 생성될 때 어떠한 작업
    def __init__(self,name): #__init__ : 자동 호출
        #그 인스턴스의 이름을 name으로 해달라는 코드 필요
        self.name=name  #그 이름의 속성 만들어줌
        
#Person 클래스의 인스턴스인 iu 생성
iu = Person('아이유')
print(iu.name)
jimin = Person('지민')
print(jimin.name)
```

```python
class Person :
    
#Person 클래스의 인스턴스 iu
iu = Person()
#iu의 인스턴스 변수 할당
iu.name = '아이유'
iu.age = 28
iu.gender = 'F'
#인스턴스 변수 접근
print(iu.name)
```

##### 소멸자 메소드 (del)

- 인스턴스 객체과 소멸되기 전에 호출되는 메소드
