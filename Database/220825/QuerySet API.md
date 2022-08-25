## QuerySet API



#### gt (greater than)

```sql
Entry.objects.filter(id__gt=4)
			# ↑ 메서드 호출
SELECT ... WHERE id > 4
```



#### gte(greater than equal)

```sql
Entry.objects.filter(id__gte=4)
			# ↑ 메서드 호출
SELECT ... WHERE id >= 4
```



*lt(less than) : 미만, lte : 이하*

```sql
Entry.objects.filter(id__lt=4)
Entry.objects.filter(id__lte=4)

SELECT ... WHERE id >= 4
SELECT ... WHERE id >= 4
```



#### in

```sql
Entry.objects.filter(id__in = [1, 3, 4]) #id라는 필드 안에 있다면  
Entry.objects.filter(headline__in = 'abc')

SELECT ... WHERE id IN (1, 3, 4):
SELECT ... WHERE headline IN ('a','b','c'):
```



#### startswith

```sql
Entry.objects.filter(headline__startswith = 'Lennon')

SELECT ... WHERE headline LIKE 'Lennon%'
```



#### istartswith

> 대소문자 구분 안 함

```sql
Entry.objects.filter(headline__istartswith = 'Lennon')

SELECT ... WHERE headline ILIKE 'Lennon%'
```



#### endswith

```sql
Entry.objects.filter(headline__endswith = 'Lennon')
Entry.objects.filter(headline__iendswith = 'Lennon')

SELECT ... WHERE headline LIKE '%Lennon'
SELECT ... WHERE headline ILIKE '%Lennon'
```



#### contains 

> 포함(앞 뒤로 %)

```sql
Entry.objects.get(headline__containsh = 'Lennon')
Entry.objects.filter(headline__istartswith = 'Lennon')

SELECT ... WHERE headline LIKE '%Lennon%'
SELECT ... WHERE headline ILIKE '%Lennon%'
```





#### range 

```python
import datetime
start_date = datetime. date(2005,1,1)
end_date = datetime. date(2007,1,1)
Entry.objects.filter(pub_date__range = (start_date, end_date))
```



```sql
SELECT ... WHERE pub_date
BETWEEN '2005_01_01' and '2007_01_01'
```



#### 복합 활용

```sql
inner_qs = Blog.objects.filter(name__contains='Cheddar')
entries = Entry.objects.filter(blog__in = inner_qs)

SELECT ... 
WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%)'
```



#### 활용

```sql
Entry.objects.all()[0]

SELECT ... LIMIT 1;

# 만약 n:m이라면
LIMIT OFFSET 


Entry.objects.order_by('id')

SELECT ... ORDER BY id;

# 내림차순
Entry.objects.order_by('-id')
SELECT ... ORDER BY id DESC;
```



```bash
# venv 가상환경에서

# 장르의 모든 값
Genre.objects.all().query

print(Genre.objects.all().query)

print(Genre.objects.order by('-id').query)

print(Genre.objects.get(id=1).query)
# 쿼리 출력 안 됨 이유? 개별 인스턴스이기 때문

print(Genre.objects.order by('-id')[2:5].query)
```





### ORM 확장(1:N)

```python
class Genre(models.Model):
    name = models.CharField(mas_langth=30)
    
class Artist(models.Model):
    name = models.CharField(mas_langth=30)
    debut = models.DateField()
    
class Artist(models.Model):
    name = models.CharField(mas_langth=30)
    genre = models.ForeignKey('Genre',
on_delete = models.CASCADE)
# 데이터베이스에는 genre_id => genre_id라고 쓸 필요 없고 genre만 쓰면 됨 fk를 쓰면 자동으로 id 생성
    artist = models.ForeignKey('Arist'
on_delete = models.CASCADE)
```



### models.ForeignKey 필드

- 2개의 필수 위치 인자
  - Model Class : 참조하는 모델
  - on_delete : 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식
    - CASCADE: 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제 (ex :  글이 사라지면 댓글도 삭제)
    - PROTECT : 삭제되지 안음
    - SET_NULL : NULL 설정
    - SET_DEFAULT : 기본 값 설정



### Foreign Key(외래키)

- 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
  - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
- 외래 키의 값이 반드시 부모 테이블의 기본키일 필요는 없지만 유일한 값이어야 함

```python
genre = models.ForeignKey('Genre',
on_delete = models.CASCADE)
# 데이터베이스에는 genre_id 라고 표시됨 
#genre_id라고 쓸 필요 없고 genre만 쓰면 됨 => fk를 쓰면 자동으로 id 생성
```



```python
# 앨범에 장르 추가

album = Album()
album.name = '꽃'
#album.genre = Genre
#album.genre = 1
# error 

genre = Genre.objects.get(id = 1)
album.genre = genre
album.artist = Artist.objects.get(id = 1)
album.save()

#값
#테이블에 실제 필드는 _id가 붙어있기 때문
album = Album()
album.genre_id = 1
album.artist_id = 1
album.name = '미아'
album.save()

#앨범의 id가 1인 것의
album = Album.objects.get(id = 1)
album.name
#장르의 이름은?
album.genre #장르 객체
album.genre.name

#1-> N (역참조)
# 클래스이름_set
#id가 1인 장르의 모든 앨범은?
g1 = Genre.objects.get(id = 1)
g1.album_Set_all()

```



```python
#1 참조
#앨범 입장에서 장르는 직접 참조
album = Album.objects.get(1)
album.artist
album.genre

#2 역참조
genre = Genre.objects.get(1)
genre.album_set.all() #별도의 설정이 없다면 역참조는 _set 필요
#앨범의 인스턴스 값이 담긴 쿼리셋
```



#### Create

```python
artist = Artists.object.get(1)
genre = Genre.objects.get(1)

album = Album()
album.name = '앨범'
album.artist = artist # 객체의 저장
album.genre = genre
album.save()
```

