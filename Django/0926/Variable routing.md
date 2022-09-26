### Variable routing

> 필요성 => 템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상화에서 비슷한 URL과 템플릿을 계속해서 만들어야 할까?

- URL 주소를 변수로 사용하는 것 의미

- URL 일부를 변수로 지정하여 view 함수의 인자로 넘기기 가능

- 변수 값에 따라 하나의 path()에 여러 페이지 연결 가능



### 작성

- 변수는 "<>"에 정의하며 view 함수의 인자로 할당
- 기본 타입 string => str, int, slug, uuid, path 타입이 있음



```html
{% extends 'base.html'%}

{% block content %}
{% endblock %}

```



### 템플릿 상속에 관련된 태그

`{% extends ' ' %}`

**반드시 템플릿 최상단에 작성**

`{% block content %}` `{% endblock content %}`



## Sending and Retrieving form data

> 데이터를 보내고 가져오기

HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기



- 웹은 가장 기본적으로 클라이언트-서버 아키텍처 사용
- 클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 사용자는 HTTP 요청에서 전달할 정보 제공 가능



## Sending form data(Client)

HTML <form> element

- 데이터가 전송되는 방법 정의
- 웹에서 사용자 정보를 입력하는 여러 방식(text, button,) 등을 제공하고,  사용자로부터 할당된 데이터를 서버로 전송하는 역할 담당
- 데이터를 어디(action)로 어떤 방식(method) 보낼지



### HTML form's attributes

1. action
   - 입력 데이터가 전송될 URL 지정
   - 데이터를 어디로 보낼 것인지 지정, 이 값은 반드시 유효한 URL
   - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
2. method
   - 데이터를 어떻게 보낼 것인지 정의
   - 입력 데이터의 HTTP request methods를 지정
   - HTML form 데이터는 오직 2가지 방법으로만 전송 가능 => GET 방식과 POST 방식



### GET 

- ㅇ서버로부터 정보 조회하는 데 사용
- 데이터를 가져올 때만 사용
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송

form 정의

주소(누구에게) => https://search.naver.com

주문서(무엇을) => /search.naver?query=아이유



http://search.naver.com/search.naver? 

=> form의 action에 정의한 내용

query=아이유

=> input으로 정의한 데이터

