📝**어제 복습**

|          | 구문   | 예시                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| C(reate) | INSERT | INSERT INTO 테이블 이름 (칼럼 1, 칼럼 2,...) VALUES (값 1, 값 2); |
| R(ead)   | SELECT | SELECT * FROM 테이블 이름 WHERE 조건;                        |
| U(pdate) | UPDATE | UPDATE 테이블 이름 SET 칼럼 1=값 1, 칼럼 2 = 값 2 WHERE 조건; |
| D(elete) | DELETE | DELETE FROM 테이블 이름 WHERE 조건;                          |



## WHERE

```sql
--테이블생성
CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL,
);

-- 데이터를 추가
.mode CSV
--
.import users.csv users

--쿼리

--users table에서 age가 30이상인 유저의 모든 컬럼 정보 조회
SELECT * FROM users WHERE age >= 30;

--30세 이상인 사람들의 이름 3명만
SELECT first_name FROM users WHERE age >= 30 LIMIT 3;

--age가 30 이상 성이 '김'인 사람의 나이와 성만 조회
SELECT age, first_name FROM users WHERE age >= 30 AND last_name = '김';
```



#### WHERE절에서 사용할 수 있는 연산자

- 비교 연산자
  - =, >, >=, <, <= 
- 논리 연산자
  - AND - 앞, 뒤 조건이 모두 참
  - OR - 앞이나 뒤 조건이 참
  - NOT - 뒤 조건 결과 반대로



```sql
--1. 키가 175이거나, 키가 183이면서 몸무게가 80인 사람
WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80

--2. 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80
```



### SQL 사용 가능 연산자

- BETWEEN 값 1 AND 값 2 
  - 값 1과 값 2 사이 비교 (값 1 <= 비교 값 <= 값 2)
- IN (값 1, 값 2, ...)
  - 목록 중에 값이 하나라도 일치하면 성공
- LIKE 
  - 비교 문자열과 형태 일치
- IS NULL / IS NOT NULL
  - NULL 여부를 확인할 떄 항상 IS 사용( = 사용 X)
- 부정 연산자
  - 같지 않다 ( !=, ^=, <>)
  - ~와 같지 않다 (NOT 칼럼명 = )
  - ~보다 크지 않다 (NOT 칼럼명 > )



- 연산자 우선 순위
  - 1 순위 : 괄호()
  - 2 순위 : NOT
  - 3 순위 : 비교 연산자, SQL
  - 4 순위 : AND
  - 5 순위 : OR



### SQLite Aggregate Functions

- Aggregate Functions (집계 함수)
  - 값 집합에 대한 계산을 수행하고 단일 값 반환

- COUNT
- AVG
- MAX
- MIN
- SUM



```sql
--users table에서 age가 30이상인 유저의 모든 컬럼 정보 조회
SELECT COUNT(*) FROM users WHERE age >= 30;

--전체 중에 가장 작은 나이
SELECT MIN(age) FROM users;

--이씨 중 가장 작은 나이
SELECT MIN(age),first_name FROM users WHERE last_name = '이';

--이씨 중에 가장 적은 나이를 가진 사람의 이름과 계좌잔고
SELECT MIN(age),first_name,balance FROM users WHERE last_name = '이';

--30 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30:

--계좌 잔액이 가장 높은 사람과 그 액수 조회
SELECT MAX(balance),first_name FROM users;

--30 이상인 사람들의 평균 계좌 잔액
SELECT AVG(balance) FROM users WHERE age >= 30:
```



### LIKE

> 패턴 일치를 기반으로 데이터 조회

- % => 0개 이상의 문자
  - 문자열이 있을 수도, 없을 수도 있음
-  _ => 임의의 단일 문자
  - 반드시 한 개의 문자 존재



SELECT * FROM 테이블 이름 WHERE 컬럼 LIKE '패턴';

|                    |                                              |
| ------------------ | -------------------------------------------- |
| 2%                 | 2로 시작하는 값                              |
| %2                 | 2로 끝나는 값                                |
| %2%                | 2가 들어가는 값                              |
| _2%                | 아무 값이 하나 있고 두번째가 2로 시작하는 값 |
| 1_ _ _             | 1000 이상의 숫자                             |
| 2 _ % _ % / 2_ _ % | 2로 시작하고 적어도 3자리인 값               |





```sql
--지역 번호가 02인 사람만 조회
SELECT * FROM users WHERE phone LIKE'02-%';'

--이름이 '준'으로 끝나는 사람만 조회
SELECT * FROM users WHERE first_name LIKE '%준'

--중간 번호가 5114인 사람만 조회
SELECT * FROM users WHERE phone LIKE'%-5114-%';'
```





### ORDER BY

- ASC - 오름차순
- DESC - 내림차순

```sql
SELECT * FROM 테이블이름 ORDER BY 칼럼 ASC;
SELECT * FROM 테이블이름 ORDER BY 칼럼 DESC;
```



```sql
--나이 순으로 오름차순 정렬 상위 10개만 조회
SELECT * FROM users ORDER BY age ASC LIMIT 10;

--나이, 성 순으로 오름차순
SELECT * FROM users ORDER BY age, last_name LIMIT 10;

--계좌 잔액 순 내림차순
SELECT last_name,first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

--계좌 잔액 순 내림차순, 성은 오름차순
SELECT last_name,first_name, balance FROM users ORDER BY balance DESC,last_name ASC LIMIT 10;
```

