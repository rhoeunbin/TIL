### CASE

> 특정 상황에서 데이터를 변환하여 활용

**ELSE 생략 시 NULL 값 지정됨**

```sql
CASE
	WHEN 조건식 THEN 식
	WHEN 조건식 THEN 식
	ELSE 식
END
```



```sql
SELECT id, gender FROM healthcare;
-- gender 대신에 case

-- 성별 1(남자), 2(여자)
SELECT 
	id,
	CASE
    	WHEN gender = 1 THEN '남자'
    	WHEN gender = 2 THEN '여자'
    	-- ELSE 없으면 NULL 값 생성
	END AS 성별
FROM healthcare
LIMIT 5;
	-- 파이썬의 if문과 비슷
	
```



```sql
-- 흡연(smoking) 값 조회
SELECT DISTINCT smoking
FROM healthcare;

smoking
-------
1
3
2

SELECT
	id,
	smoking,
	CASE
		WHEN smoking = 1 THEN '비흡연자'
		WHEN smoking = 2 THEN '흡연자'
		WHEN smoking = 3 THEN '헤비스모커'
		ELSE '무응답'
	END
FROM healthcare
LIMIT 50;
```



```sql
-- 나이에 따라서 구분
-- 청소년(~18), 청년(~40), 중장년(~90)

SELECT 
	first_name,
	last_name,
	CASE
		WHEN age <= 18 THEN '청소년'
		WHEN age <= 40 THEN '청년'
		WHEN age <= 90 THEN '중장년'
		ELSE '노년'
	END
FROM users
LIMIT 10;
```



### 서브 쿼리

> 특정한 값을 메인 쿼리에 반환하여 활용

*소괄호로 감싸고, 메인 쿼리의 칼럼 모두 사용 O, 메인 쿼리는 섭 쿼리의 칼럼 이용 X*

```sql
SELECT * 
FROM 테이블
WHERE 컬럼1 = (
	SELECT 컬럼1
	FROM 테이블
);
```



- 단일행 서브쿼리
  - 검색의 결과가 0 또는 1
  - 단일행 비교 연산자와 같이 사용 ( <, >, =, <>, <=, >= )
- 다중행 서브쿼리
  - 서브쿼리 결과가 2개 이상
  - IN, EXISTS 사용
- 다중컬럼 서브쿼리



```sql
-- users에서 가장 나이가 작은 사람의 수?
-- 1
SELECT age,COUNT(*) FROM users GROUP BY age ORDER BY age LIMIT 1;

-- 2
SELECT MIN(Age)
FROM users;
-- 서브쿼리

SELECT COUNT(*) FROM users 
WHEN age = 15;

-- 3 서브쿼리 활용
SELECT COUNT(*) FROM users 
WHERE age = (SELECT MIN(age) FROM users);
```



```sql
-- users에서 평균 계좌 잔고가 높은 사람의 수?

SELECT AVG(balance) FROM users;
-- 서브쿼리

SELECT COUNT(*) FROM users
WHERE balance > (SELECT AVG(balance) FROM users);
```



```sql
-- 단일행 서브쿼리 - WHERE에서의 활용
-- users에서 유은정과 같은 지역에 사는 사람의 수?

-- 서브쿼리
SELECT 
	country
FROM users
WHERE last_name = '유' AND fist_name = '은정'

SELECT 
	COUNT(*) 
FROM users
WHERE country = (WHERE last_name = '유' AND fist_name = '은정');
```



```sql
-- 단일행 서브쿼리 - SELECT에서 활용
-- 전체 인원과 평균 연봉, 평균 나이

SELECT COUNT(*), AVG(balance), AVG(age) FROM users;

SELECT
	(SELECT COUNT(*) FROM users) AS 총인원,
	(SELECT AVG(balance) FROM users) AS 평균연봉;
```



```sql
-- 단일행 서브쿼리 - UPDATE에서의 활용
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);
```



#### 다중행 서브쿼리

> 모든 결과를 합쳐서 반영할 때

```sql
-- 다중행 서브쿼리
-- 이은정과 같은 장소에 있는 사람 수 
SELECT country 
FROM users
WHERE last_name = '이' AND fist_name = '은정';
-- 전라북도, 경상북도에 있음

SELECT 
	country, COuNT(*)
FROM users
GROUP BY country;
-- 전라북도와 경상북도에 사는 모든 사람이 나오진 않음을 확인

SELECT 
	COuNT(*)
FROM users
WHERE country IN (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
```



```sql
-- 특정 성씨에서 가장 어린 사람들의 이름과 나이

-- 특정 성씨별로 가장 적은 나이
SELECT 
	last_name,
	MIN(age) 
FROM users
GROUP BY last_name;

SELECT 
	first_name, 
	last_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT 
          last_name,
          MIN(age) 
          FROM users 
          GROUP BY last_name) 
ORDER BY last_name;
```



```sql
-- AC/DC의 모든 앨범
-- AC/DC(Artists)
-- 앨범(albums)

-- 앨범 검색 -> 아티스트는 id로 저장되어 있음
-- AC/DC는 아는데 ID를 모를 때

-- id 조회
SELECT ArtisId
FROM artists
WHERE Name = 'AC/DC';

-- 서브쿼리
SELECT *
FROM albums 
WHERE ArtistsId = (SELECT AristId
FROM artists
WHERE Name = 'Queen')
```

