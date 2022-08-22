## JOIN

> 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능

- 데이터 베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라 여러 테이블로 나눠 저장하게 됨 => 여러 테이블을 결합(join)하여 출력하여 활용

- **기본키(PK - 고유한 값 )**나 **외래키(FK - 다른 테이블의 고유한 값) **값의 관계에 의해 결합

```sql
SELECT * FROM table WHERE 작성자 = "홍길동";
```



- 변경될 때마다 고유한 값인지 알 수 없고, 변경할 값이 너무 많을 수도 있다 => 관리가 어려움 

→ user 테이블을 만듦 → user가 별도의 관계형 데이터베이스로 분류됨

→ 외래키(PK)로 바뀐다 → user 에 있는 pk가 fk

= > **레코드를 다 바꿀 필요 없음**



💡**두 개의 테이블로 결과를 만들고 싶을 때 사용하는 게 join**

📢*여러 테이블들이 나눠서 관리되고 있고 우리가 조합해서 만들 수 있다!*



### INNER JOIN 

> 조건에 일치하는 (동일한 값이 있는) 행만 반환

```sql
SELECT *
FROM 테이블1 [INNER] JOIN 테이블2
	ON 테이블1.칼럼 = 테이블2.칼럼;
-- INNER 생략 가능
```



```sql
-- INNER JOIN
-- A와 B 테이블에서 값이 일치하는 것들만
SELECT *
FROM users [INNER] JOIN role
	ON users.role_id = role.id;
	
	
-- 원하는 컬럼만 지정할 시
SELECT
	users.name,
	role.title
FROM users [INNER] JOIN role
	ON users.role_id = role.id;
```



```sql
-- 스태프(2)만 출력
SELECT * 
FROM users INNER JOIN role
	ON users.role_id = role.id
WHERE role.id=2;

-- 이름을 내림차순으로 출력
SELECT * 
FROM users INNER JOIN role
	ON users.role_id = role.id
ORDER BY users.name DESC;
```





### OUTER JOIN

> 동일한 값이 없는 데이터도 반환할 때 사용



```sql
SELECT *
FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
	ON 테이블1.칼럼 = 테이블2.칼럼;
```



```sql
-- LEFT OUTER JOIN
-- LEFT 테이블에 오른쪽에 해당하는 테이블을 붙임
SELECT * 
FROM articles LEFT OUTER JOIN users
	ON articles.user_id = users.id;
	
-- NULL인 부분 제외
SELECT * 
FROM articles LEFT OUTER JOIN users
	ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;

-- FULL OUTER JOIN
-- LEFT 테이블에 오른쪽에 해당하는 테이블을 붙임, 오른쪽 테이블에 또 왼쪽 테이블을 다시 붙이고 중복된 것을 날림
SELECT * 
FROM articles FULL OUTER JOIN users
	ON articles.user_id = users.id;
	-- 이영희의 값이 생김 , 중복된 것은 날림 => 집합처럼 보임
	
```



### CROSS JOIN

> 모든 가능한 경우의 수 조회

```sql
SELECT *
FROM 테이블1 CROSS JOIN 테이블2;
```



```sql
SELECT *
FROM users CROSS JOIN role;
```



```sql
SELECT *
FROM albums JOIN artists
	ON albums.AritstId = artist.ArtistId;

SELECT *
FROM albums LEFT JOIN artists
	ON albums.AritstId = artist.ArtistId 
LIMIT 5;
```

