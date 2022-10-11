# Django Auth

> Django authentication system(인증 시스템)은 인증과 권한 부여를 함께 제공(처리)

- user
- 권한 및 그룹
- 암호 해시 시스템
- Form 및 View 도구
- 기타 적용 가능한 시스템



*필수 구성은 settings.py의 INSTALLED_APPS에서 확인 가능*



Authentication(인증)

- 신원 확인
- 사용자가 자신이 누군지

Authorization(권한)

- 권한 부여
- 인증된 사용자가 수행할 수 있는 작업 결정



### 사전 설정

```bash
$ python manage.py startapp accounts
```



````python
# settings.py

INSTALLED_APPS= [
    'articles',
    'accounts',
    ...
]
````





urls.py에서 path('accounts/', include('accounts.urls')) 만들기



```python
#accounts/urls.py에서 

from django.urls import path
from . import views

appname = "accounts"
urlpatterns = [
    
]
```



```python
# accounts/modles.py 에서

from django.db import models


```

**auth_user(앱이름_모델이름)에서 확인 가능**

=> 모델을 가져와서 쓰겠다 => 클래스 상속 (공식 문서에서 확인 가능)



## django User Model

- Django 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 강력하게 권장
- 커스텀 모델은 기본 user  모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정 가능
  - 단, User 모델 대체 작업은 프로젝트의 모든 migration 혹은 첫 migrate를 실행하기 전에 이 작업 마쳐야 함



### 모델 설정

```python
# settings.py 맨 밑에 user model 설정
AUTH_USER_MODEL = 'accounts.User'
```



```python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```



```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



=> 설정하고 db 한 번 날리고 migrations와 migrate 하기

- migrations 파일 삭제 
  - migrations 폴더 및 __init__.py는 삭제하지 않음 
  - 번호가 붙은 파일만 삭제 
-  db.sqlite3 삭제 
-  migrations 진행
  -  makemigrations 
  - migrate



AbstractUser => username이 설정되어 있음

상속을 구조화한 것



### user 객체 활용

```python
Articles.objects.create(title='제목', content='내용')

User.objects.create(username='eunbin',password='dmsdms22!!')
```



- 회원은 가입시 일반적으로 암호 저장이 필수적이며, 별도의 처리 필요

- Django에서는 기본으로 PBKDF2를 사용하여 저장
  - 단방향 해시함수 : 1234 ->로 암호화 a1b2 but, a1b2 -> 1234 는 안 된다



```python
# user 생성
User.objects.create_user('dms0', 'dmsqls.gmail.com', '1234')

# user 비밀번호 변경
user = User.objects.get(pk=2)
User.set_password(‘new password’)
User.save()

# user 인증(비밀번호 확인)
from django.contrib.auth import authenticate
user = authenticate(username='dms0', password='secret')

# 비밀번호 자동 암호화해서 저장된다

from django.contrib.auth import authenticate

authenticate(username='rho', password='1234')

# 틀리면 정보 안 나옴
```



# 회원가입

```python
#accounts/urls.py에서 
from django.urls import path
from . import views

appname = "accounts"

urlpatterns = [
	path('signup/', views.signup, name='signup')    
]

```



```python
# accounts/views.py

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationform

def signup(request):
    form = UserCreationForm()
    context = {
        'form': form, 
    }
    return render(request, 'accounts/signup.html', context)
```



```html
# signup.html에서

{% extends 'base.html'%}

<h1>
    회원가입
</h1>
{{ form.as_p }}
```





```html
# signup.html에서

{% extends 'base.html'%}
{% load django_bootstrap5 %}

{% blockbody %}
<h1>
    회원가입
</h1>

<form action='' method='POST'>
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" content="OK" %}
</form>

{% endblockbody %}
```



```python
# accounts/views.py => POST 요청

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationform

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    else :
        form = UserCreationForm()
    context = {
        'form': form, 
    }
    return render(request, 'accounts/signup.html', context)
```



UserCreationForm() => auth 안에 있던 user // 상속 받아야 함



```python
# forms.py 생성

from django.contrib.auth.form import USerCreationForm
from .models form User

class CustomerUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('username')
```





```python
# accounts/views.py => POST 요청

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationform
from .forms from CustomerUserCreationForm 

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    else :
        form = UserCreationForm()
    context = {
        'form': form, 
    }
    return render(request, 'accounts/signup.html', context)
```



### usermodel 설정하기

> user -> get_user_model로 바꾸기(직접 참조 X)

```python
# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(get_user_model(), UserAdmin)
```


    
```python
# forms.py 생성

from django.contrib.auth.form import USerCreationForm
from django.contrib.auth import get_user_model
# 직접 참고 하지 않아도 된다

class CustomerUserCreationForm(UserCreationForm):
class Meta:
    model = get_user_model
    fields = ('username',)
```



### 프로필 페이지 만들기

URL :  /accounts/2/

view : detail

Template 반환 : 사용자 정보 (username)



```python
#accounts/urls.py에서 

from django.urls import path
from . import views

appname = "accounts"

urlpatterns = [
	path('signup/', views.signup, name='signup')    
    path('<int:pk>', views.detail, name='detail')
]
```



```python
# accounts/views.py

from django.shortcuts import render
from .forms from CustomerUserCreationForm 
from django.contrib.auth import get_user_model

def detail(request,pk):
    User = get_user_model().objects.get(pk=pk)
    context = {
        'user' : user,
    }
	return render(request, 'accounts/detail.html', context)
```



```html
detail.html


```

