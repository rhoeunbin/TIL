```
prctices : pingpong 기능(form 데이터 전송)

articles: 방명록

```



### startapp 두 개 생성하기

app 두 개가 떨어져 있지만 같은 폴더로 생각

같은 파일 이름이 있다면 installed app에서 가장 최상위에 있는 파일이 실행됨

=> 장점 : base.html 상속 가능(body만 긁어와도 됨)



templates안에 articles를 넣어 따로 관리

extends의 기준은 templates안의 최상단이므로 base.html은 바깥으로



### BASE_DIR

> 가장 기본이 되는 폴더

- settings.py에서 특정 경로를 절대 경로로 편하게 작성할 수 있도록 Django에서 미리 지정해둔 경로 값

`BASE_DIR = Path(__file__).resolve().parent.parent`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates',], #절대경로가 들어와야함 => templates 문서 이름은 바뀌어도 상관 X
         }
```



### Django URLs

> Dispatcher로서의 URL 이해하기

- 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작



## App URL mapping

> 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법을 이해하기 •

- 두번째 app인 articles를 생성 및 등록 하고 진행 
-  app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고,  app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지 보수에 좋지 않음



1. 각 앱의 view 함수를 다른 이름으로 import 가능

```python
# firstpjt/urls.py
from articles import views as articles_views
from pages import views as pages_views
urlpatterns = [
...,
path('pages-index', pages_views.index),
]
```



2. 하나의 프로젝트의 여러 앱이 존재한다면, 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁할 수 있음

```python
# pages/urls.py
from django.urls import path
urlpatterns = [
]
```





### include()

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수 
-  함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고,  남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

```python
# firstpjt/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('articles/', include('articles.urls')),
path('pages/', include('pages.urls')),
]
```





### Including other URLconfs

- urlpattern은 언제든지 다른 URLconf 모듈을 포함(include) 할 수 있음

```python
# 템플릿 경로 변경

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('practices/', include('practices.urls')),
]
```



