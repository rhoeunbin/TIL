## Database

>  체계화된 데이터의 모임, 정보의 집합, 몇 개의 자료 파일을 조직적으로



#### 데이터 베이스의 장점

- 데이터 중복 최소화
- 데이터 무결성
- 데이터 일관성(정확한 정보 보장)
- 데이터 독립성(물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지



### 관계형 데이터베이스(RDB)

> 키와 값들의 관계를 표 형태로 저장되어 있음



### 스키마(schema)

> 자료의 구조, 표현 방법이나 관계 등 명세 기술

id => INT

name => TEXT

address => TEXT

age => INT



### 테이블

> 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합 => 스키마를 기준으로 작성

|  id  |  name  | address | age  |
| :--: | :----: | :-----: | :--: |
|  1   | 홍길동 |  제주   |  20  |
|  2   | 노은빈 |  인천   |  25  |
|  3   |  동이  |  서울   |  30  |



#### 열(column)

> 각 열에 고유한 데이터 형식 지정



#### 행(row)

> 실제 데이터가 저장되는 형태



#### 기본키(Primary Key)

> 각 행(레코드)의 고유 값 => id

*반드시 설정, 데이터베이스 관리 및 관계 설정 시 주요하게 활용*

ex) 중복X => ID, 주민 번호, 학번 등 (이름 X => 동명이인)



## RDBMS

> 관계형 데이터베이스 관리 시스템

=> **SQLite** 파일 형식, 비교적 가벼운 데이터베이스



#### DATA Type

`INTEGER`

`TEXT`

`NULL`



### SQL(Structured Query Language)

> 데이터 관리를 위해 특수 목적으로 설계된 프로그래밍 언어

- **DDL**(Data Definition Language) - 데이터 정의 언어 (테이블, 스키마 정의) - `CREATE`, `DROP`, `ALTER`
- **DML**(Manipulation) - 데이터 조작 언어 (데이터 저장,조회,수정,삭제) - `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- **DCL**(Control) - 데이터 제어 언어 (사용자의 권한 제어) - `GRANT`, `REVOKE`, `COMMIT`, `ROLLBACK`



```sql
$ sqlite3 tutorial.sqlite3
-- sqlite 실행됨

sqlite> .databse
-- tutorial.sqlite3 생성

sqlite> .import hellodb.csv examples
sqlite> SELECT * FROM examples;
-- 테이블 모든 정보 조회
```

CSV(Comma Seperated Valiables) => comma로 구분된 값들

csv에 있는 값들을 조회하기 가능



```sql
-- classmates 테이블 생성
CREATE TABLE classmates(
    id INTEGER PRIMARY KEY,
    name TXT  
);
-- 테이블 목록 조회
.tables

-- 특정 테이블 스키마 조회
.schema classmates

-- 값 추가
INSERT INTO classmates VALUES (1, '조세호');

id name
-- ----
1  조세호

-- 테이블 조회
SELECT * FROM classmates;
INSERT INTO classmates VALUES (2, '이동희');

id name
-- ----
1  조세호
2  이동희

-- 테이블 삭제
DROP TABLE classmates
```

```sql
CREATE TABLE classmates(
    name TEXT, 
    age INT,
    address TEXT
);
```



#### 필드 제약 조건

- NOT NULL : NULL 값 입력 금지
- UNIQUE : 중복 값 입력 금지 (NULL은 중복 가능)
- PRIMARY KEY : 테이블에서 반드시 하나, NOT NULL + UNIQUE
- FOREIGN KEY : 외래키
- CHECK : 조건으로 설정된 값만 입력 허용
- DEFAULT :  기본 설정 값



```sql
CREATE TABLE students(
    id(필드이름) INTEGER PRIMARY KEY, 
    name TXT NOT NULL,
    age INTEGER(타입) DEFAULT(제약조건) 1 CHECK (0 < age)
);

INSERT INTO students (id, name) VALUES (5, '홍길동');
-- 5 홍길동 1 생김
INSERT INTO students (id) VALUES (6);
-- error : NOT NULL conastraint failed:students.name
```



## CRUD(Create Read Update Delete)

### Insert

- 테이블에 단일 행 삽입
- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력



```sqlite
-- 테이블에 단일 행 삽입
INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

-- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력
INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);

INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23,'서울');
-- 데이터 조회
SELECT * FROM classmates;

-- 아래도 가능
INSERT INTO classmates VALUES ('홍길동', 23,'서울');
```



```sqlite
-- rowid 사용 = > 자동으로 증가하는 숫자를 id로 추가
SELECT rowid, * FROM classmates;

SELECT name FROM classmates;
```



```sql
INSERT INTO classmates VALUES
('홍길동', 23,'서울')
('김길동', 33,'인천')
('송길동', 27,'경기');
-- 여러번 할 필요X
```



### READ

- `SELECT`
- `LIMIT`
- `WHERE`
- `SELECT DISTINCT` (중복 행을 제거) - SELECT 바로 뒤에 작성



#### LIMIT

```sqlite
-- classmates 테이블에서 id, name 컬럼만 조회

SELECT id, name FROM classmates;

-- classmates 테이블에서 id, name 컬럼 값 하나만 조회

SELECT id, name FROM classmates LIMIT 1;
-- 홍길동만 나옴 
-- LIMIT 2 => 홍길동, 김철수 
```



#### OFFSET  

> 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

```sql
-- classmates 테이블에서 id, name 컬럼 값 세번째에 있는 하나만 조회

SELECT id, name FROM classmates LIMIT 1 OFFSET 2;
-- 두 칸 띄우고 
```



```sqlite
-- classmates 테이블에서 id, name 컬럽 값 중에 주소가 서울인 경우의 데이터 조회
SELECT id, name FROM classmates WHERE address = '서울';

SELECT * FROM classmates WHERE address = '서울';
-- *: 모든 , 전부
```



#### SELECT DISTINCT

```sqlite
SELECT DISTINCT 컬럼 FROM 테이블이름:

-- classmates 테이블에서 age 값 전체 중복없이 조회
SELECT DISTINCT age FROM classmates:
```



### DELETE

```sqlite
-- 삭제
DELETE FROM members WHERE rowid=5;
INSERT INTO members (name) VALUES ('노은빈');
SELECT * FROM members;
```



### UPDATE(수정)

```sqlite
UPDATE classmates SET address='서울' WHERE rowid=5;
SELECT rowid * FROM classmates;
```

