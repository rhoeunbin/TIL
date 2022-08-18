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



#### 열(row)

> 실제 데이터가 저장되는 형태



#### 기본키(Primary Key)

> 각 행(레코드)의 고유 값

*반드시 설정, 데이터베이스 관리 및 관계 설정 시 주요하게 활용*

ex) 중복X => 주민번호, 학번 등



## RDBMS

> 관계형 데이터베이스 관리 시스템

=> **SQLite** 파일 형식, 비교적 가벼운 데이터베이스



### SQL(Structured Query Language)

- DDL(Data Definition Language) - 데이터 정의 언어(데이블,스키마 정의)
- DML - 데이터 조작 언어(데이터 저장,조회,수정,삭제)
- DCL - 데이터 제어 언어(사용자의 권한 제어)



```sqlite
sqlite>.import hellodb.csv examples
sqlite> SELECT * FROM examples;
```

CSV(Comma Seperated Valiables) => comma로 구분된 값들

csv에 있는 값들을 조회하기 가능



```sqlite
CREATE TABLE classmates(
    id INTEGER PRIMARY KEY,
    name TXT  
);
```테이블 목록 조회
.tables

```특정 테이블 스키마 조회
.schema classmates

#값 추가
INSERT INTO classmates VALUES (1, '조세호');

#테이블 조회
SELECT * FROM classmates;

#테이블 삭제
DROP TABLE classmates
```

```sqlite
CREATE TABLE classmates(
    name TEXT, 
    age INT,
    address TEXT
);
```



필드 제약 조건

- NOT NULL : NULL 값 입력 금지
- UNIQUE : 중복 값 입력 금지 (NULL은 중복 가능)
- PRIMARY KEY : 테이블에서 반드시 하나, NOT NULL + UNIQUE
- FOREIGN KEY : 외래키
- CHECK : 조건으로 설정된 값만 입력 허요
- DEFAULT :  기본 설정 값



```sqlite
CREATE TABLE students(
    id(필드이름) INTEGER PRIMARY KEY, 
    name TXT NOT NULL,
    age INTEGER(타입) DEFAULT(제약조건) 1 CHECK (0<age)
);
```



## CRUD(Create Read Upload Delete)

### Insert

- 테이블에 단일 행 삽입
- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력



```sqlite
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23,'서울');
#아래도 가능
INSERT INTO classmates VALUES ('홍길동', 23,'서울');
```

rowid 사용 = > 자동으로 값 추가



```sqlite
```





### READ

- select
- limit
- where
- select distinct (중복 행을 제거)



```sqlite
#classmates 테이블에서 id, name 컬럼만 조회

SELECT id, name FROM classmates;

#classmates 테이블에서 id, name 컬럼 값 하나만 조회

SELECT id, name FROM classmates LIMIT 1;
-- 홍길동만 나옴 
-- LIMIT 2 => 홍길동, 김철수 

#classmates 테이블에서 id, name 컬럼 값 세번째에 있는 하나만 조회

SELECT id, name FROM classmates LIMIT 1 OFFSET 2;
--두 칸 띄우고 
```



- OFFSET 

```sqlite
SELECT id, name FROM classmates WHERE address = '서울';
SELECT * FROM classmates WHERE address = '서울';
-- *: 모든 , 전부
```



```sqlite
SELECT DISTINCT 컬럼 FROM 테이블이름:

SELECT DISTINCT age FROM classmates:
```



```sqlite
DELETE FROM members WHERE rowid=5;
INSERT INTO members (name) VALUES ('노은빈');
SELECT * FROM members;
```

수정

```sqlite
UPDATE classmates SET address='서울' WHERE rowid=5;
SELECT rowid * FROM classmates;
```

압축파일로 제출