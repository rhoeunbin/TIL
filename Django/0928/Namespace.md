## Namespace

> 개체를 구분할 수 있는 범위를 나타내는namespace에 대한 이해

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 가능

- **app_name** attribute를 작성해 URL namespace 설정



```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
...,
]
```

 ↓

```python
# pages/urls.py
app_name = 'pages'
urlpatterns = [
...,
]
```



### url 태그의 변화

```django
 {% url 'index' %} => {% url 'articles:index' %}
```



- `:` 연산자를 사용하여 지정 
  -  app_name이 articles이고 URL name이 index인 주소 참조는 articles:index가 됨



### Naming URL patterns

```python
urlpatterns = [
path('index/', views.index, name='index'),
path('greeting/', views.greeting, name='greeting'),
path('dinner/', views.dinner, name='dinner'),
path('throw/', views.throw, name='throw'),
]
```



### Built-in tag - "url"

```django
{% url '' %}
```

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
- 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력하는 방법



### DRY 원칙 

> **Don't Repeat Yourself**의 약어
>
> => 소스 코드에서 동일한 코드를 반복하지 말자



Django의 설계 철학

1. 표현과 로직(view)을 분리
2. 중복 배제



framework의 성격

- 독선적
- 관용적



MTV Design Pattern

> 여러번 짓다보니 자주 사용되는 구조가 있다는 것을 알게 되었고 이를 일반화해서 하나의 공법으로 만들어 둔 것

- Model-View-Controller
- 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴

목적 => 관심사 분리(더 나은 업무와 향상된 관리 제공)



ㅡModel

- MVC 패턴에서 Model의 역할에 해당
- 데이터와 관련된 로직 관리
- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록 관리



Template

- 레이아웃과 화면 처리



View

- 모델&템플릿과 관련한 로직을 처리해서 응답 반환
- 클라이언트의 요청에 대해 처리를 분기하는 역할
- MVC 패턴에서 Controller의 역할에 해당



database의 구조

1. schema
   - 뼈대
   - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
2. table
   - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
   - 관계(REalation)
     1. 필드(속성, Column:열)
     2. 레코드(튜플, Row:행)

PK(Primary Key) => id



CharField







CRUD



