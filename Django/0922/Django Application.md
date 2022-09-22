#### firstpjt 파일 안

- ` __init__.py `
  -  Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시 
  -  별도로 추가 코드를 작성 x
- `asgi.py` 
  -  Asynchronous Server Gateway Interface 
  -  Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움 
  -  추후 배포 시에 사용하며 지금은 수정하지 않음

- `settings.py `
  - Django 프로젝트 설정을 관리
- `urls.py` 
  - 사이트의 url과 적절한 views의 연결을 지정

- `wsgi.py` 
  -  Web Server Gateway Interface 
  -  Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움 
  -  추후 배포 시에 사용하며 지금은 수정하지 않음
- `manage.py `
  -  Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티 `python manage.py <command> [options]`





## Django Application (기능 만들기)

> *가상환경 상태에서 해야함*



### 어플리케이션 생성

- `python manage.py startapp articles(기능)`

  *일반적으로 어플리케이션 이름은 '복수형'으로 작성*

​		=> `articles` 가 생김



### 어플리케이션 구조

- admin.py
  - 관리자용 페이지 설정
- apps.py
  - 설정들
- models.py
- tests.py
- **view.py**



**프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 반드시 추가해야 함(settings.py에 있음)**

- INSTALLED_APPS 
  - Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록
  - 앱을 추가할 때는 최상단에 하나씩 추가 (`articles` 넣기) **이름 반드시 동일**



*반대로 삭제할 때는?*

1. INSTALLED_APPS에서 articles 지우기

2. articles 디렉토리 지우기



#### Project&Application

- Project
  - 'collection of apps'
  - 프로젝트는 앱의 집합
  - 프로젝트에는 여러 앱 포함 가능
  - 앱은 여러 프로젝트에 있을 수 있음
- Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할 담담
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것 권장



## 요청과 응답

> url 로 요청하고 문서(HTML)로 응답 받기



client (나&크롬)  시세정보가 담긴 것(url)요청 server(네이버)



- URL -> VIEW -> TEMPLATE 순의 작성 순서로 코드 작성, 데이터 흐름 이해



1. 주문서 만들기 (url, urls.py)
2. 로직 구현(views.py)
3. HTML 페이지 구현(template, index.html)



### urls.py

```python
# urls.py
# 위의 링크 눌러서 설명 보기 가능

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #함수 호출 
   #path('주문서/', 어떤 view파일의 어떤 함수에서 핸들링 할 것인지)
    path('index/', views.index),
]
```



### views.py

- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- Template에게 HTTP 응답 서식을 맡김

```python
#articles -> views.py

from django.shortcuts import render

# Create your views here.
# () 안에 핸들링할 인자 써야함 index(요청 정보)
def index(request):
    #환영하는 메인 페이지를 보여줌
    return render(request,'index.html') #만들면서 끝난다
```



#### render()

- 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수
  - request
    - 응답 생성하는 데 사용되는 요청 객체
  - template_name
    - 템플릿의 전체 이름 또는 템플릿 이름의 경로
  - context
    - 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)

```python
render(request, template_name, context)
```



### Template

- 실제 내용을 보여주는데 사용되는 파일

- 파일의 구조나 레이아웃 정의

- Template 파일의 기본 경로

  - app 폴더 안의 templates 폴더

    `app_name/templates`



변수 활용 이유 => 변수 변경 시 한 번에 적용하기 위해서