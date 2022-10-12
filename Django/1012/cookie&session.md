## HTTP 특징

- 비연결지향(connectionless)
  - 서버에 요청에 대한 응답을 보낸 후 연결을 끊음
    - 예를 들어 우리가 네이버 메인 페이지를 보고 있을 때 우리는 네이버 서버와 연결되어 있는 것은 아님
    - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것
- 무상태(stateless)
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
  - 클라이언트와 서버가 주고받는 메세지들은 서로 완전히 독립적



어떻게 로그인 상태를 유지할까?

> 서버와 클라이언트 간 지속적인 상태 유지를 위해 "쿠키와 세션"



## 쿠키(Cookie)

> 서버가 사용자의 웹 브라우저(클라이언트)에 전송하는 작은 데이터 조각

- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  - 브라우저는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  - 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
- 쿠키는 서로 다른 요청이 동일한 브라우저로부터 발생한 것인지 판단할 때 주로 사용
  - 상태가 없는 HTTP에서 상태 정보를 관리, 사용자는 로그인 상태를 유지할 수 없다



### 쿠키 사용 목적

- 세션 관리(Sessinon management)
  - 로그인, 아이디 자동완성, 공지 하루 안 보기. 팝업 체크, 장바구니 등의 정보 관리
- 개인화(Personalization)
  - 사용자 선호, 테마 등의 설정
- 트래킹(Tracking)
  - 사용자 행동을 기록 및 분석



### 쿠키 수명(lifetime)

- Session cookie
  - 현재 세션이 종료되면 삭제
  - 브라우저의 종료와 함께 세션 삭제
- Persistent cookie
  - Expires 속성에 지정된 날짜 혹은 Max-Age속성에 지정된 기간이 지나면 삭제



## 세션(Session)

> 사이트와 특정 브라우저 사이의 state(상태)를 유지시키는 것

- 클라이언트가 서버에 전속하면 서버가 특정 session id를 발급, 클라이언트는 session id를 쿠키에 저장
  - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
  - 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직 처리
- session id는 세션을 구별하기 위해 필요, 쿠키에는 session id 만 저장



*로그인이 되어있다=> 세션에 저장되어 있다*



### Session in Django

```python
#settings.py에서

INSTALLED_APPS = [
    'django.contrib.sessions',
]
# 세션 저장
```



## login()

- login(request, user, backend=None)
- 인증된 사용자를 로그인
  - 유저의 ID를 세션에 저장하여 세션을 기록
- HttpRequest 객체와 User 객체가 필요
  - 유저 정보는 반드시 인증된 유저 정보여야 함
    - authenticate()함수를 활용한 인증
    - AuthenticationForm을 활용한 is_valid



### 로그인 로직 작성

- 일반적인 ModelForm 기반의 Create 로직과 동일하지만
  - ModelForm이 아닌 Form으로 필수 인자 구성이 다름
  - DB에 저장하는 것 대신 세션에 유저를 기록하는 함수 호출
    - View 함수와 이름이 동일하여 변경해 호출
    - 로그인 url이 'accounts/login/'에서 변경되는 경우 settings.py LOGIN_URL을 변경해야함



### get_user()

- AuthenticationFrom의 인스턴스 메서드
- 유효성 검사를 통과했을 경우 로그인한 사용자 객체 반환



### 세션 데이터 확인하기 

- 로그인 후 개발자 도구와 DB에서 django로부터 발급받은 세션 확인(로그인은 관리자 계정을 만든 후 진행)
- django_session 테이블에서 확인



### Authentication with User

```html
<!-- base.html -->
<body>
<div class="container">
<h3>Hello, {{ user }}</h3>
<a href="{% url 'accounts:login' %}">Login</a>
<hr>
{% block content %}
{% endblock content %}
</div>
...
</body>
</html>
```



## logout()

- logout(request)
- 요청 유저에 대한 세션 정보를 삭제
  - DB에서 session data 삭제
  - 클라이언트의 쿠키에서 sessionid 삭제
- HttpRequest 객체를 인자로 받고 반환 값이 없음
- 사용자가 로그인하지 않은 경우 오류 발생 X



```html
<!-- base.html -->
<body>
<div class="container">
    
<h3>Hello, {{ user }}</h3>
<a href="{% url 'accounts:login' %}">Login</a>
<form action="{% url 'accounts:logout' %}" method="POST">
{% csrf_token %}
<input type="submit" value="Logout">
</form>
```

