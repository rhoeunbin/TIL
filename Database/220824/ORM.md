#### 📢파이썬 복습

객체 - 모든 것

=> 속성 & 메서드 (값 & 함수)

=> 클래스 / 인스턴스 (틀 / 사례)



## ORM

> Object - Relational - Mapping

> 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술

- 파이썬에서는 SQLAlchemy, peewee 등의 라이브러리 있음
- Django 프레임워크에서는 내장 Jjango ORM 활용



#### 객체로 DB를 조작한다

```python
# python
Genre.objects.all()
```



```sql
-- sql
SELECT * FROM Genre;
```



### 모델 설계 및 반영

1. 클래스를 생성하여 내가 원하는 DB의 구조를 만든다



```python
# python
from django.db import models

Class Genre(models.Model):
    name = models.CharField(max_length=30)
    #Text일 때는 TextField 사용
```



```sql
-- sql
CREATE TABLE Genre(
	id Primary Key
	name);
```



2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일 **자동** 생성

```
$ python manage.py makemigrations
```



3. DB에 migrate한다

```
$ python manage.py migrate
```



### Migration

> Model에 생긴 변화를 DB에 반영하기 위한 방법
>
> migration 파일을 만들어 DB schema를 반영

- 명령어
  - makemigrations : migration 파일 생성
  - migrate : migration을 DB에 반영

=> class 생성 → 테이블 생성 → 필드 변경(수정,삭제,추가) → class 수정( ALTER 명령어 필요 없이 자동으로 바꿈)



```sql
-- 트랜잭션
BEGIN;
--
-- Create model Genre
--
CREATE TABLE "db_genre" (
	"id" integer NOT NULL PRIAMRY KEY AUTOINCREMENT,
	"name" varchar(30) NOT NULL
);
COMMIT;
```



- 데이터 베이스 조작(Database API)

```bash
Genre.objects.all()

class name
```



## ORM 기본 조작

### Create

```python
#1. create 메서드 활용
Genre.objects.create(name='트로트')
genre = Genre()
genre.name = '락'
genre.save()

# 저장된 것 조회
genre.objects.all() 
# <QuerSet>[] => 일종의 리스트
# SELECT * FROM genres; 랑 비슷하다고 생각하기

genre.objects.all()[0]
# <genre:objects.all()(1)>
genre.objects.all()[0].name
# '인디밴드'

genres = Genre.objects.all() 
for genre in genres:
    print(genre.name)
    '''인디밴드
  		트로트
  		락'''

```

### READ(조회)

``` python
genres = Genre.objects.all()

Genre.objects.get(id=1)
# 반드시 하나 => 단일쿼리 (없거나 많으면 오류) => pk 바탕으로 찾을 때

Genre.objects.filter(id=1)
#무조건 결과가 QuerySet(일종의 리스트)=> 개수 상관 없이 =>이외의 모든 값을 꺼낼 때
```





### Update 수정

```python
# genre 객체 활용
genre = Genre.objects.get(id=1)
genre.name
# '인디밴드'

genre.name = '인디음악'
genre.save()

## 
a = 1
a
# 1
a = 5

person = ['홍길동', '김철수']
# 다 출력하려면 반복문
person = '홍길동'
```



### Delete 삭제

```python
# genre 객체 활용
genre = Genre.objects.get(id = 2)
genre
#<Genre:Genre object (2)>
genre.name
# '트로트'

#genre 객체 삭제
genre.delete()
#(1, {})

genre = Genre.objects.get(id = 2).delete()
# 도 가능
```



### Artist 모델 생성

```python
class Artist(models.Model):
	name = model.CharField(mas_length=30)
    debut = models.DateField()
    
python manage.py makemigrations
python manage.py migrate
```



```python
# Artist 생성
artist = Artist()
artist.name = '아이브'
#2021년 12월 1일
artist.debut = datetime.date(2021,12,1)
artist.save()

ive = Artist.objects.get(id=1)
ive.debut
#datetime.date(2021,12,1)

#1 Artist 생성
artist = Artist()
artist.name = '아이유'
artist.debut = '2019-12-26' #문자열도 가능
artist.save()

iu = Artist.objects.get(id=1)
iu.debut
#datetime.date(2019,12,26)
```

