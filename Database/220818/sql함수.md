### 문자열 함수

- SUBSTR(문자열, start, length) : 문자열 자르기
  - 시작 인덱스 : 1, 마지막 인덱스 : -1
- TRIM(문자열), LTRIM, RTRIM : 문자열 공백 제거 => (파이썬에서 strip과 같은 기능)
- LENGTH(문자열) :문자열 길이
- REPLACE(문자열, 패턴, 변경값) : 패턴에 일치하는 부분 변경
- UPPER(문자열) , LOWER : 대소문자 변경
- || : 문자열 합치기 ( Enter 키 위에)



```sql
SELECT * FROM users LIMIT 1 :

-- 문자열 합치기
-- (성+이름) 출력, 5명만
SELECT 
	last_name || first_name 이름,
	age,
	country,
	phone,
	balance
FROM users
LIMIT 5;
```



```sql
-- 문자열 길이

SELECT
	LENGTH(first_name)
	first_name
FROM users
LIMIT 5;
```



```sql
-- 문자열 변경

SELECT 
	first_name,
	REPLACE(phone,'-','')
FROM users
LIMIT 5;
```



### 숫자 함수

- ABS(숫자) : 절대값
- SIGN : 부호(양수 1, 음수 -1, 0 0)
- MOD(숫자1, 숫자2) : 숫자1을 숫자2로 나머지
- CEIL, FLOOR, ROUND : 올림, 내림, 반올림
- POWER(숫자1, 숫자2)  : 숫자1의 숫자2 제곱
- SQRT : 제곱근



*CEIL : ceiling*

```sql
-- 숫자 활용

SELECT NOD(5,2)
FROM users
LIMIT 1;

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;

-- 9의 제곱근
SELECT SQLT(9)
FROM users
LIMIT 1;

-- 9^2
SELECT POWER(9,2)
FROM users
LIMIT 1;

```



- 산술 연산자
  - +, - , *, %



### GROUP BY

> 선택된 행 그룹을 하나 이상의 열 값으로 요약 행 만듦

- 집계 함수와 같이 활용했을 때 의미 있음
- 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐

```sql
SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2
```

```sql
SELECT * FROM users GROUP BY last_name;
-- 로 사용X => 반드시 집계함수 사용

-- 평균 나이
SELECT AVG(age) FROM users;

-- 성에 따른 평균 나이
SELECT AVG(age) FROM users GROUP BY 성;
```



```sql
-- users에서 각 성(last_name)씨가 몇 명씩 있는지?

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

-- GROUP BY 사용시 활용하는 컬럼 제외하고는 집계 함수를 써야함

SELECT last_name, AVG(age), COUNT(*) FROM users GROUP BY last_name;

```



```sql
SELECT last_name, COUNT(*) 
FROM users 
GROUP BY last_name
LIMIT 5;

last_name  COUNT(*)
---------  --------
강          23
고          10
곽          4
구          2
권          17

-- GROUP BY는 결과 정렬 X, 기존 순서와 바뀜
-- 원칙적으로 정렬해서 보고 싶으면 ORDER BY 써야함

SELECT last_name, COUNT(*) 
FROM users 
GROUP BY last_name
ORDER BY last_name
LIMIT 5;

last_name  COUNT(*)
---------  --------
강          23
고          10
곽          4
구          2
권          17
```





```sql
-- GROUp BY WHERE을 쓰고 싶다
-- 100번 이상 등장한 성만 출력하고 싶다

SELECT last_name, COUNT(last_name) 
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;

-- 오류 Parse error: misuse of aggregate: COUNT()


-- 조건에 따른 GROUP 하려면 HAVING 사용

SELECT last_name, COUNT(last_name) 
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
```



### SELECT 문장 실행 순서

FROM →WHERE → GROUP BY → HAVING → SELECT → ORDER BY

📝순서 => 

`FROM` 테이블을 대상으로 

`WHERE` 제약조건에 맞춰 뽑아서 

`GROUP BY` 그룹화한다 

`HAVING` 그룹 중에 조건과 맞는 것 만을 

`SELECT` 조회하여 

`ORDER BY` 정렬하고 

`LIMIT` 특정 위치의 값 가져옴



### ALTER TABLE

> 칼럼을 추가하거나 삭제하고 싶을 때
>
> ex) 주소를 추가, 이름 제거 등

1. 테이블 이름 변경
2. 새로운 column 추가
3. column 이름 수정 
4. column 삭제



```sql
-- 1. 테이블 이름 변경
ALTER TABLE table_name
RENAME TO new_name;

-- 2. 새로운 column 추가
ALTER TABLE table_name
ADD COLUMN column_definition;

-- 3. column 이름 수정 
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;

-- 4. column 삭제
ALTER TABLE table_name
DROP COLUMN current_name;
```



💡기사를 쓴 시간 추가 => X

```sql
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;

-- Error : Cannot add TABLE news ADD COLUMN created_at TEXT NOT NULL
```

💡*테이블에 있던 기존 레코드들에는 새로 추가할 필드에 대한 정보가 없다. 따라서 NOT NULL 형태의 컬럼 추가 불가능*



🤭*해결방법*

1. NOT NULL 설정 없이 추가
2. 기본값 (DEFAULT) 설정

