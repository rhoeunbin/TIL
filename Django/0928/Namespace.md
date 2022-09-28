## Namespace

- 개체를 구분할 수 있는 범위를 나타내는namespace에 대한 이해

URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 가능

app_name attribute를 사용해 지정 가능



url 태그의 변화

 {% url 'index' %} => {% url 'articles:index' %}



Template namespace



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



