# DB
## 2. SQL2

## 목차
1. Managing Tables
- Create a table
- Modifying table fields
- Delete a table
2. Modifying Data
- Insert data
- Update data
- Delete data
3. Multi table queries
- Join
- Joining tables

## 1. Managing Tables(DDL)
### Create a table
#### CREATE TABLE
CREATE TABLE : 테이블 생성
- 각 필드에 적용할 데이터 타입 작성
    - NULL : 아무런 값도 포함 X
    - INTEGER : 정수
    - REAL : 부동 소수점
    - TEXT : 문자열
    - BLOB : 이미지, 동영상, 문서 등의 바이너리 데이터
- 테이블 필드에 대한 제약조건 작성
    - 데이터의 무결성을 유지
    - 데이터베이스의 일관성 보장
    - PRIMARY KEY : 해당 필드를 기본 키로 지정(INTEGER 타입에만 적용 가능, INT, BIGINT 등의 다른 정수 유형에는 적용 X)
    - NOT NULL : 해당 필드에 NULL 값 허용 X
    - FOREIGN KEY : 다른 테이블간의 외래 키 관계 정의
```sql
-- examples 테이블 생성 및 확인
CREATE TABLE examples(
    -- 필드명 필드의데이터타입 필드제약조건

    -- AUTOINCREMENT 키워드 : PRIMARY KEY 제약조건을 받은 필드에 작성(항상 새로운 레코드에 대해 이전의 최대 값보다 큰 값 할당 즉, 삭제된 값은 재사용 불가)
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);

-- 생성 후, 테이블 스키마 확인
-- PRAGMA : 테이블 구조 확인
PRAGMA table_info('examples');
```
### Modifying table fields
#### ALTER TABLE
ALTER TABLE : 테이블 및 필드 조작
- 필드 추가 : ADD COLUMN 
- 필드명 변경 : RENAME COLUMN A TO B
- 필드 삭제 : DROP COLUMN
- 테이블명 변경 : RENAME TO new_table_name 
```sql
-- 필드 추가
ALTER TABLE
    table_name
ADD COLUMN
    field_name DATATYPE CONSTRAINT;
-- 잘못된 필드 추가 : 여러 개의 필드를 추가하고 싶은 경우
-- 한 번의 ADD COLUMN으로 여러 필드 추가 불가능
-- 따라서, ALTER TABLE - ADD COLUMN을 원하는필드마다 작성
ALTER TABLE
    table_name
ADD COLUMN
    new_field_1 DATATYPE1 CONSTRAINT1;

ALTER TABLE 
    table_name
ADD COLUMN
    new_field_2 DATATYPE2 CONSTRAINT2;

-- 필드 이름 변경
ALTER TABLE
    table_name
RENAME COLUMN
    current_name TO new_name

-- 필드 삭제
-- 삭제하는 필드가 다른 부분에서 참조하지 않고(다른 필드의 외래 키로 사용 X), PRIMARY KEY가 아니며, UNIQUE 제약 조건이 없는 경우에만 작동
ALTER TABLE
    table_name
DROP COLUMN
    to_drop_field_name;

-- 테이블 명 변경
ALTER TABLE
    table_name
RENAME TO
    new_table_name;
```

### Delete a table
#### DROP TABLE
DROP TABLE : 테이블 삭제
```sql
-- 테이블 삭제
DROP TABLE
    to_drop_table_name;
```


## 2. Modifying Data(DML)
### Insert data
#### INSERT 
INSERT : 테이블 레코드 삽입
- INSERT INTO 절 뒤, 테이블 이름 및 괄호 안에 필드 목록들 작성
- 위에서 지정한 필드 목록 순서에 맞게 VALUES 키워드 다음 괄호 안에 데이터 목록 작성
- 추가내용 : DATA()
    - DATE() 함수를 통해, DATA TYPE이 DATE인 필드 값에 DATE()를 넣어주면, 레코드를 INSERT했을 때의 시각이 자동으로 입력됨
```sql
-- INSERT
INSERT INTO
    table_name (field1, field2, ...)
VALUES
    (data1, data2, ...)
-- INSERT의 경우, 여러 레코드를 한 번에 추가 가능(앞에서 ADD COLUMN은 다 따로 했어야 하는데,,,)
INSERT INTO
    table_name (field1, field2, ...)
VALUES
    (data1-1, data1-2, ... ),
    (data2-1, data2-2, ... ),
    (data3-1, data3-2, ... );
```
### Update data
#### UPDATE
UPDATE : 테이블 레코드 수정
- SET 절 다음에 수정할 필드와 새 값 지정
- WHERE 절이 존재할 경우, 수정할 레코드 지정
- WHERE 절이 존재하지 않을 경우, 모든 레코드 수정
```sql
-- UPDATE

-- 수정할 레코드가 포함된 테이블 지정
UPDATE
    table_name
-- 수정할 필드값(여러 필드값을 한 번에 수정 가능)
SET 
    field_name1 = expression1,
    field_name2 = expression2
-- 수정할 레코드 지정
WHERE
    condition
```
### Delete data
#### DELETE
DELETE : 테이블 레코드 삭제
- DELETE FROM 절 다음 테이블 이름 작성
- WHERE 절이 존재할 경우, 삭제할 레코트 지정
- WHERE 절이 존재하지 않을 경우, 모든 레코드 삭제
```sql
DELETE FROM
    table_name
WHERE
    condition;
```
## 3. Multi table queries
### Join
관계의 필요성 : 동명이인, 특정 데이터 수정 시 레코드 조회에 문제 발생
- 테이블을 여러 개로 나누어서 분류(게시글 작성 테이블, 가입 유저테이블, 유저 별 역할 테이블 등)
- 여러 개의 테이블들을 연결해 줄 수 있는 값 필요 : ForeignKey를 부여하여 참조 시 사용
- 출력 시에 문제를 발생시키지 않기 위해, 테이블 간의 결합을 통해 출력

### Joining tables
#### JOIN
JOIN : 둘 이상의 테이블에서 데이터 검색
- INNER JOIN
- OUTER JOIN
#### INNER JOIN
INNER JOIN : 두 테이블에서 값이 일치하는 레코드에 대해서만 결과 반환
- FROM 절 이후 메인 테이블 지정
- INNER JOIN 절 이후 메인 테이블과 조인할 테이블 지정
- ON 키워드 이후 JOIN할 조건 작성(두 테이블 간 레코드를 일치시키는 규칙)
```sql
SELECT 
    select_list
FROM
    table_main
INNER JOIN table_side
    ON table_main.pk = table_side.fk;
-- 뒤에 WHERE로 조건부여 가능
```

#### LEFT JOIN
LEFT JOIN : 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
- FROM 절 이후 왼쪽 테이블 지정
- LEFT JOIN 절 이후 오른쪽 테이블 지정
- ON 키워드 이후 JOIN할 조건 작성(왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴)
- 즉, 왼쪽 테이블의 레코드 중, 오른쪽 테이블의 레코드와 일치하지 않는 레코드는 조회 가능
- 반대로, 오른쪽 테이블의 레코드 중, 왼쪽 테이블의 레코드와 일치하지 않는 레코드는 조회 불가

