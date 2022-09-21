# Django 개발 환경 설정 가이드

> window 기준



### Django?

- 서버를 구현하는 웹, 파이썬 프레임워크

📝프레임 워크? => Frame + Work : 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것



명령어

- `~` : 내pc > 사용자 디렉토리로 감 => home으로 이동
- `cd` : 원하는 디렉토리로 이동
- `pwd` : 현재 자신의 디렉토리 경로 확인
- `ls` : 현재 터미널 위치의 디렉토리 경로 확인





## 1. 기본 설정

> 바탕화면에서 git bash를 활용했다



1. `cd~` 

   git bash 화면에서 명령어를 통해 home 디렉토리로 가기

2. `pwd` 

   명령어를 통해 현재의 위치 확인

3. `mkdir server` 

   명령어로 'server' 라는 이름의 문서 만들기

4. `pip list` 

   명령어를 통해 다운받은 파일들 리스트 확인

5. `python --version` 

   명령어로 파이썬 버전 확인



## 2. 가상환경 설정



#### 가상환경이란?

> 자신이 원하는 python 환경을 만들기 위해 필요한 모듈만 넣어 놓은 곳



1. `python -m venv server-venv[가상환경이름]` 

​		명령어로 파이썬 가상환경 모드 만들기

2. `ls -a`

​		명령어로 `~/server`에 `server-venv`가 있는지 확인

3. `cd server-venv`

​        명령어로 `server-venv` 디렉토리로 이동

4. `source server-venv/Scripts/activate`

   `~/server`디렉토리 위치에서 가상환경 활성화

5. `deativate`

   명령어를 통해 가상환경 끄기



## 3. Django 설치



*상위 디렉토리에서*

1. `source server-venv/Scripts/activate`

   `~/server`디렉토리 위치에서 가상환경 활성화

2. `pip install django==3.2.13`

   명령어로 django 설치 

📝3.2.13 버전 설치 이유?

=> 최신 버전을 사용하면 오류가 날 수 있기도 하고 기존의 버전에서 크게 달라지지 않았으며 기존 버전이 더 상용화 되었기 때문!!



3. `pip list`

   명령어를 통해 다운받아져 있는 파일에 Django가 버전에 맞게 설치되었는지 확인

4. `django-admin startproject firstpjt .`

   `django-admin startproject [프로젝트이름] [설치 경로]`	

   장고를 관리하는 명령어 사용

5. `code .`

   파일들을 연다

6. `python manage.py runserver`

   명령어를 통해 서버 실행할 준비를 하고 Chrome으로 가서 `localhost:8000`주소 입력하면 설치 완료



## 프로젝트 구조



#### firstpjt 파일 안

- ` __init__.py `
  -  Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시 
  - 별도로 추가 코드를 작성 x
- `asgi.py` 
  -  Asynchronous Server Gateway Interface 
  - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움 
  -  추후 배포 시에 사용하며 지금은 수정하지 않음

- `settings.py `
  - Django 프로젝트 설정을 관리
- `urls.py` 
  - 사이트의 url과 적절한 views의 연결을 지정

- `wsgi.py` 
  -  Web Server Gateway Interface 
  - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움 
  -  추후 배포 시에 사용하며 지금은 수정하지 않음
- `manage.py `
  -  Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티