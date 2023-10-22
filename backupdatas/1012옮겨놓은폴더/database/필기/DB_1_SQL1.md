# DB
## 1. SQL1

## 목차
1. Database
2. Relational Database
3. SQL
4. Single Table Queries
- Querying data
- Sorting data
- Filtering data
- Grouping data

## 1. Database
### 데이터베이스
데이터 베이스 : 체계적인 데이터 모음
- 데이터 : 저장이나 처리에 효율적인 형태로 변환된 정보
#### 기존 데이터 저장 방식
1. 파일(File) 이용
- 장점 : 어디서나 쉽게 사용 가능
- 단점 : 데이터를 구조적으로 관리하기 어려움
2. 스프레드 시트(Spreadsheet) 이용
- 장점 : 테이블의 열과 행을 사용해 데이터를 구조적으로 관리 가능
- 단점 : 크기(약 100만 행까지만 저장 가능), 보안(파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공), 정확성의 한계
#### 데이터베이스의 역할
데이터 베이스의 역할 : 데이터를 저장(구조적 저장)하고 조작(CRUD)

## 2. Relational Database
### 관계형 데이터베이스
관계형 데이터베이스 : 데이터 간의 관계가 있는 데이터 항목들의 모음
- 테이블, 행, 열의 정보를 구조화
- 서로 관련된 데이터 포인터를 저장하고, 이에 대한 엑세스 제공
- 관계(여러 테이블 간의 논리적인 연결)을 통해 데이터를 다양한 형식으로 조회 가능
#### Relational Database 키워드
1. Table(Relation) : 데이터를 기록하는 곳
2. Field(Column, Attribute) : 고유한 데이터 타입이 지정되는 위치
3. Record(Row, Tuple) : 구체적인 데이터 값이 저장되는 위치
4. Database(Schema) : 테이블의 집합
5. Primary Key(기본 키) : 각 레코드의 고유 값
- 관계형 DB에서 레코드의 식별자로 PK 사용
6. Foreign Key(외래 키) : 테이블의 필드 중, 다른 테이블의 레코드를 식별할 수 있는 키
- 다른 테이블의 기본 키를 참조하여 외래 키로 저장
- 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용
### RDBMS
#### DBMS
DBMS(Database Management System) : 데이터베이스를 관리하는 소프트웨어 프로그램
- 데이터 저장 및 관리에 용이한 시스템
- 데이터베이스와 사용자 간의 인터페이스 역할
- 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움
#### RDBMS
RDBMS(Relational Databse Management System) : 관계형 데이터베이스를 관리하는 소프트웨어 프로그램
- SQLite : 경량의 오픈 소스 데이터베이스 관리 시스템
    - 컴퓨터나 모바일 기기에 내장되어 간단하고 효율적인 데이터 저장 및 관리를 제공
- MySQL
- PostgreSQL
- Oracle Database ...
## 3. SQL
### SQL
SQL(Structure Query Language) : 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
- 테이블의 형태로 구조화(Structure)된 관계형 DB에게 요청(Query)
#### SQL Syntax
SELECT column_name FROM table_name;
- SQL 키워드는 대소문자 구분 X(명시적 구분을 위해 키워드를 대문자로 작성)
- 각 SQL 문장의 끝에는 세미콜론(;) 필요
#### SQL Statements
SQL Statements : SQL을 구성하는 가장 기본적인 코드 블록
### 수행 목적에 따른 4가지 유형의 SQL Statements
1. DDL(Data Definition Language) : 데이터 정의를 위한 SQL Statement
- DDL의 역할 : 데이터의 기본 구조 및 형식 변경
- SQL 키워드 : CREATE, DROP, ALTER
2. DQL(Data Query Language) : 
- DQL의 역할 : 데이터 검색
- SQL 키워드 : SELECT
3. DML(Data Manipulation Language) : 데이터 조작
- DQL의 역할 : 데이터 조작(추가, 수정, 삭제)
- SQL 키워드 : INSERT, UPDATE, DELETE
4. DCL(Data Control Language) 
- DCL의 역할 : 데이터 및 작업에 대한 사용자 권한 제어
- SQL 키워드 : COMMIT, ROLLBACK, GRANT, REVOKE
## 4. Single Table Queries(DQL)
### Querying data
#### SELECT
SELECT : 테이블에서 데이터 조회
```sql
SELECT
    -- 데이터를 선택하려는 필드 하나 이상 지정
    -- AS를 사용하여 출력시 원하는 필드명으로 변경하여 출력 가능
    -- 실제 DB에서 필드명 변경 X(출력시에만)
    -- asterisk(*) 사용시, 해당 테이블의 모든 필드 데이터 조회 
    select_list1,
    select_list2, 
    select_list3 AS WTC
FROM
    -- 데이터를 선택하려는 테이블 이름 지정
    table_name;
```
### Sorting data
#### ORDER BY
ORDER BY : 하나 이상의 컬럼을 기준으로 결과 정렬
- 오름차순 : 기본 값(ASC)
- 내림차순 : (DESC)
- FROM clause(테이블 선정) 뒤에 위치
- 만약, 오름차순 정렬하는 필드의 데이터 중, NULL 값이 있을 경우 가장 위에 출력(NULL이 제일 우선적으로 오름차순 정렬)
```sql
SELECT
    select_list
FROM
    table_name
ORDER BY
    column1 DESC,
    column2 ASC;
```

### Filtering data
#### DISTINT
DISTINCT : 조회 결과에서 중복 레코드 제거
- SELECT 키워드 바로 뒤에 작성(SELECT DISTINCT)
- SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드 지정
- '데이터에 포함되어있는 모든 나라 출력' 등 SET이 필요할 경우 사용
```sql
SELECT DISTINCT
    select_list
FROM 
    table_name;
```
#### WHERE
WHERE : 특정 검색 조건을 지정하여 조회
- FROM clause 뒤에 위치
- 연산자를 뒤에 붙여서 작성
    - 비교 연산자 : =, >=, <=, !=, IS (NOT) NULL, LIKE '%str'('___단일문자'), (NOT) IN (), BETWEEN A AND B
    - 논리 연산자 : AND, OR, NOT
```sql
SELECT
    select_list
FROM
    table_name
WHERE
    -- AND혹은 OR 논리연산자를 통해 여러 조건 부여 가능
    -- 비교 연산자 : =, !=
    -- NULL값 비교 : IS NULL / IS NOT NULL
    search_condition1
    AND/OR serach_contidion2;
```
#### LIMIT
LIMIT : 조회하는 레코드 수 제한
- 하나 또는 두 개의 인자 사용(0 또는 양의 정수)
- 조회하는 최대 레코드 수 지정
```sql
SELECT
    select_list
FROM
    table_name
LIMIT
    -- 해당 테이블의 필드 값 중, offset 이후로 row_count개 만큼 조회
    offset row_count;
```
### Grouping data
#### GROUP BY
GROUP BY : 레코드를 그룹화하여 요약본 생성
- SELECT 키워드에서 집계 함수(Aggregation Functions)와 함께 사용 가능
    - 값에 대한 계산을 수행하고, 단일 값 반환
    - SUM(합), AVG(평균), MAX(최대), MIN(최소), COUNT(개수)
- WHERE 혹은 FROM 절 뒤에 배치
    - WHERE 주의 사항 : GROUP BY 할 항목에 관한 aggregation function에 조건을 부여해야 할 경우, WHERE에 조건 작성 X
    - GROUP BY clause 뒤에 HAVING clause 사용
- GROUPBY 키워드 뒤에 그룹화할 필드 목록 작성
- HAVING : 집계 항목에 대한 세부 조건 지정
    - 주로 GROUP BY와 함께 사용(GROUP BY가 없을 경우, WHERE처럼 사용)
```sql
SELECT
    field_name, agg_func(arg) as AggFunc
FROM
    table_name
-- 그룹화 할 항목과 관련 없는 요소(AggFunc이 아닌 것)에 조건 부여 시
WHERE
    conditon
GROUP BY
    field_lists;
-- 그룹화 할 항목에 대한 세부조건 필요 시
HAVING
    AggFunc condition
```


```sql
-- 조회할 내용
SELECT
    -- Composer 필드 조회
    Composer,
    -- 그룹화 할 항목에 대해 조회할 내용 : Milliseconds를 60000으로 나누어 분 단위로 변경 후, 평균 값 조회
    -- 이름은 avgOfMinute으로 -> 이루 밑의 clauses에서 사용 시 해당 이름으로 사용
    AVG(Milliseconds/60000) AS avgOfMinute
-- 조회할 필드 값들을 가지고 있는 테이블
FROM
    tracks
-- WHERE clause에는 GROUP BY 하여 조회할 내용에 대한 조건 부여 X
-- 따라서, 에러 발생
-- WHERE 
--     avgOfMinute < 10
GROUP BY
    -- 그룹화할 항목 : Composer필드
    Composer
-- 그룹화 하여 조회 할 집계함수(aggregation functions)에 대한 조건 부여
-- HAVING 사용
HAVING
    avgOfMinute < 10;
```

#### SELECT 실행 순서
FWGHSOL 순으로 실행(작성 순서랑 다름!!)
1. FROM : 어떤 테이블에서 가져올까?
2. WHERE : 가져올 데이터들의 조건은 무엇일까?
3. GROUP BY : 어떤 항목들로 그룹화할까?
4. HAVING 그룹화 한 항목의 집계 항목들에 대해서는 어떤 세부조건을 부여할까?
5. FROM : 해당 테이블의 어떤 필드 값을 가져올까?
6. ORDER BY : 어떤 순서로 정렬할까?
7. LIMIT : 몇 번째 항목부터(offset이후) 몇 개를 가져올까? 
