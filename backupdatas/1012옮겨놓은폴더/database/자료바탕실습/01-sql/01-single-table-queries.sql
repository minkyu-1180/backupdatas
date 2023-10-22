-- 01. Querying data

-- SELECT 활용 1
-- employees 테이블에서 LastName 필드의 모든 데이터 조회
SELECT 
  LastName
FROM
  employees;

-- SELECT 활용 2
-- employees 테이블에서 LastName, FirstName 필드의 모든 데이터 조회
SELECT 
  LastName, FirstName
FROM
  employees;

-- SELECT 활용 3
-- employees 테이블에서 모든 필드 데이터 조회
SELECT 
  *
FROM
  employees;


-- SELECT 활용 4
-- employees 테이블에서 FirstName 필드의 모든 데이터 조회
-- 단, 조회 시 FirstName이 아닌, '이름'으로 필드명이 출력될 수 있도록 변경
SELECT 
  -- FieldName AS WTC : 기존 필드명 그대로 출력하는 것이 아닌, 원하는 대로 필드명 출력
  -- 실제 DB에서 필드명은 변경 X
  FirstName AS '이름'
FROM
  employees;

-- SELECT 활용 5
-- tracks 테이블에서 Name, Milleseconds 필드의 모든 데이터 조회
-- 단, Milliseconds의 데이터는 60000으로 나누어 분 단위 값으로 출력
-- 추가로, Milliseconds를 60000으로 나누어 출력하는 필드명은 '재생시간(분)'으로 변경하여 출력
SELECT
  Name, 
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;

-- 02. Sorting data

-- ORDER BY : 조회 결과의 레코드 정렬
-- FROM clause 뒤에 위치하여 오름차순(ASC, default), 내림차순(DESC) 정렬할 필드 선택

-- ORDER BY 활용 1
-- employees 테이블의 FirstName 필드의 모든 데이터 조회
-- 단, 조회시 출력이 FirstName 필드를 기준으로 오름차순 정렬되어 출력
SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName ASC;

-- ORDER BY 활용 2
-- employees 테이블의 FirstName 필드의 모든 데이터 조회
-- 단, 조회시 출력이 FirstName 필드를 기준으로 내림차순 정렬되어 출력
SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

-- ORDER BY 활용 3
-- customers 테이블에서 Country 필드를 기준으로 내림차순으로 정렬
-- 다음, 같은 Country 필드값을 가진 데이터에 대해서는 Ciry 필드를 기준으로 오름차순 정렬하여 조회
SELECT
  Country, City
FROM
  customers
ORDER BY
  -- 여러 필드에 대한 정렬 기준을 쉼표(,)로 구분
  -- ORDER BY에 작성된 필드순으로 우선 정렬
  Country DESC,
  City ASC;


-- ORDER BY 활용 4
-- tracks 테이블에서 Milliseconds 필드를 기준으로 내림차순으로 정렬하여
-- Name, Milliseconds 필드의 모든 데이터 조회
-- 단, Milliseconds 필드는 60000으로 나누어 분 단위 값으로 출력
-- 추가로, 해당 필드는 출력 시 '재생 시간(분)'이라는 필드명으로 변경하여 조회
SELECT
  Name, 
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;


-- 03. Filtering data

-- DISTINCT : 중복 데이터를 제거하여 필드 조회

-- DISTINCT 활용 1
-- customers 테이블의 Country 필드의 모든 데이터를 오름차순하여 조회
-- 단, 중복 Country 이름은 제거하여 조회
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

-- WHERE : 

-- WHERE 활용 1
-- customers 테이블에서 LastName, FirstName, Country 필드의 데이터 조회
-- 단, City 필드 값이 'Prague'인 데이터만 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  -- 같은 값 -> 비교연산자 =
  -- ==가 아닌, =임을 기억하기!!!
  City = 'Prague';

-- WHERE 활용 2
-- customers 테이블에서 City 필드 값이 'Prague'가 아닌 데이터의 LastName, FirstName, City 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  -- 다른 값 -> 비교연산자 !=
  City != 'Prague';

-- WHERE 활용 3 : 조건1 AND 조건2
-- customers 테이븡에서 Company 필드 값이 NULL이고, Country 필드 값이 USA인 데이터의
-- LastName, FirstName, Company, Country 필드 데이터 출력
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  -- 필드값이 NULL일 경우
  -- 같은 값인지 확인 -> IS NULL
  -- 다른 값인지 확인 -> IS NOT NULL
  Company IS NULL 
  -- 여러 WHERE 조건 부여 -> AND로 연결
  AND Country = 'USA';

-- WHERE 활용 4 : 조건1 OR 조건2
-- customers 테이블에서 Company 필드 값이 NULL이거나 Country필드 값이 USA인 데이터의 
-- LastName, FirstName, Company, Country 조회
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL 
  OR Country = 'USA';

-- WHERE 활용 5 : BETWEEN A AND B
-- tracks 테이블에서 Bytes 필드 값이 10000 ~ 500000 이하인 데이터의 
-- Name, Bytes 조회
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  -- 100000 <= Bytes <= 500000;
  -- 비교 연산자(크기 비교) : Field_name BETWEEN A AND B
  Bytes BETWEEN 100000 AND 500000;

-- WHERE, ORDER BY 활용 6 
-- SELECT -> FROM -> WHERE -> ORDER BY 순으로 작성
-- tracks 테이블에서 Bytes 필드 값이 10000 ~ 500000 이하인 데이터의
-- Name, Bytes를 
-- Bytes 필드를 기준으로 오름차순하여 조회
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

-- WHERE 활용 7 : IN ()
-- customers 테이블에서 Country 필드 값이 Canada 또는 Germany 또는 France인 데이터의
-- LastName, FirstName, Country 조회
SELECT
  LastName, FirstName, Country
FROM 
  customers
WHERE
  -- 한 필드 값을 여러 개의 데이터와 비교 : IN 연산자 사용
  -- Field_Name IN ('데이터1', '데이터2', '데이터3', ... )
  -- OR로 연결한 것과 같은 효과
  Country IN ('Canada', 'Germany', 'France');
  -- Country = 'Canada'
  -- OR Country = 'Germany'
  -- OR Country = 'France';

-- WHERE 활용 8 : NOT IN ()
-- customers 테이블에서 Country의 필드 값이 Canada 또는 Germany 또는 France가 
-- 아닌 데이터의 LastName, FirstName, Country 조회
SELECT
  LastName, FirstName, Country
FROM 
  customers
WHERE
  -- 포함 x인 데이터 조건 조회 -> NOT IN
  -- 여러개의 != 조건과 동일
  Country NOT IN ('Canada', 'Germany', 'France');


-- WHERE 활용 9
-- customers 테이블에서 LastName의 필드 값이 son으로 끝나는 데이터의
-- LastName, FirstName 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  -- Field_Name LIKE '%찾는내용' : 해당 필드의 값이 찾는 내용으로 끝나는 데이터 찾기
  LastName LIKE '%son';

-- WHERE 활용 10
-- customers 테이블에서 FirstName의 필드 값이 4자리이면서 'a'로 끝나는 데이터('___a')의
-- LastName, FirstName 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';

-- LIMIT : 출력하는 레코드의 수 설정

-- LIMIT 활용 1
-- tracks 테이블에서 TrackId, Name, Bytes 필드 데이터를 
-- Bytes 기준으로 내림차순하여 
-- 7개 조회
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
-- LIMIT의 인자가 1개 -> 가장 위 데이터부터 offset 시작
LIMIT 7;

-- LIMIT 활용 2
-- tracks 테이블에서 TrackId, Name, Bytes 필드 데이터를 
-- Bytes 기준 내림차순으로
-- 4번째부터(offset : 3) 7번째 데이터까지만(4 ~ 7 -> 4개) 조회
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
-- 4번째 데이터부터 : offset 3
-- 7번째 데이터까지 : row_count 4
LIMIT 3, 4;
-- LIMIT count OFFSET offset 구문 사용 가능(순서만 바뀜)
-- LIMIT 4 OFFSET 3;


-- 04. Grouping data

-- GROUP BY

SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

-- GROUP BY 활용 1
-- tracks 테이블에서 Composer 필드를 그룹화하여
-- 각 그룹에 대한 Bytes의 평균 값을 
-- 내림차순 조회
-- 단, Bytes의 각 그룹별 평균값을 담은 필드명은 AVGofBytes로 변경
SELECT
  Composer, AVG(Bytes) AS AVGofBytes
FROM 
  tracks
GROUP BY
  Composer
ORDER BY
  -- 평균 값을 내림차순하여 조회
  -- 주의사항 : 만약 조회시 필드명을 변경하였을 경우, 변경한 필드명을 아래에서 사용 
  AVGofBytes DESC;



-- 에러
-- GROUP BY 키워드 사용시 주의사항
-- 만약, 그룹화할 항목에 세부 조건을 부여 시, WHERE 사용 X
-- HAVING 키워드를 통해 세부 조건 부여
-- GROUP BY -> HAVING 순으로 작성
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks

WHERE
  avgOfMinute < 10
GROUP BY
  Composer;


-- 에러 해결
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;
