🖱헷갈리는 것 정리

ORM 개념 : Object Relational Mapping, 객체-관계 매핑

=> 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 것

MTV 개념 : Model-View-Controller

request 역할

get은 조회, post는 입력

각각의 views.py는 HTTPresponse object 반환

모델폼 없어도 됨 => 유효성 검사를 못할 뿐 => 모델폼을 쓰면 알아서 에러메세지를 띄워준다의 의미



- 요청과 응답
  - url -> view -> templates
- render()
  - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수 
  -  request : 응답을 생성하는 데 사용되는 요청 객체
  -  template_name : 템플릿의 전체 이름 또는 템플릿 이름의 경로
  -  context : 템플릿에서 사용할 데이터 (딕녀너리 타입으로 작성)



## static files

### 웹서버와 정적 파일

- 웹 서버는 특정 위치(URL)에 source을 요청(HTTP request) 받아서 제공(serving)하는 응답(HTTP response)을 처리하는 것을 기본 동작으로 함
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource) 제공





### 정적 파일 활용하기

> 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일(파일 자체가 고정)

설정 확인 = > 이미 settings.py에 되어있음

- django.contrib.staticfiles가 INSTALLED_APPS에 포함되어 있는지 확인
- settings.py에서 STATIC _URL 정의

```python
{% load static %}
<img src=" {% static 'my_App/example.jpg' %}" alt="My image">
```





*templates 폴더 이름 지정 => 하나의 모듈로 관리되기 때문에 분리*



static 폴더에 apparel.jpg 추가하고

{& static ' apparel.jpeg' &} 사용



settings.py에서 STATIC_URL에 이름 지정 가능

static 폴더 안에 해놓고 url 적용하면 전체 적용됨,,,

추가 경로 가능=> `{& static 'images/apparel.jpeg' &}`





## admin 사용하기

1. 가상환경 먼저 실행 후 하기
2. `python manage.py createsuperuser`



```python
#admin.py에서

from django.contrib.import admin
from .models import Article

class ArticleAdmin(admin.ModleAdmin):
	fields = ['title']

admin.site.register(Article, ArticleAdmin)
```

