-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');


-- 1. Insert data into table

-- 테이블 생성
CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- 레코드 삽입
INSERT INTO 
  articles (title, content, createdAt)
VALUES 
  ('hello', 'world', '1700-01-01');

-- 한 번에 여러 레코드 삽입 가능
INSERT INTO 
  articles (title, content, createdAt)
VALUES 
  ('title1', 'content1', '1800-01-01'),
  ('title2', 'content2', '1900-01-01'),
  ('title3', 'content3', '2000-01-01');

INSERT INTO 
  articles (title, content, createdAt)
VALUES
  -- DATATYPE이 DATE인 field는 DATE()함수로 레코드 삽입시
  -- 해당 레코드가 생성된 시간을 자동으로 삽입
  ('mytitle', 'mycontent', DATE());


-- 2. Update data in table
-- 수정할 테이블 
UPDATE 
  articles
-- 수정할 필드
SET
  title = 'update Title'
-- 수정할 데이터(레코드)
WHERE
  id = 1;

UPDATE 
  articles
-- 한 번에 하나의 레코드의 여러 필드값 수정 가능
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

-- 3. Delete data from table

-- articles 테이블에서 id값이 1인 레코드 삭제
DELETE FROM 
  articles
WHERE 
  id = 1;

-- 심화
-- articles 테이블에서 
-- createdAt을 기준으로 오름차순했을 경우(레코드 생성 순서에 따라 정렬)
-- 위에 있는 2개(no offset, rowcount=2)를 선정했을 때
-- 그 2개의 레코드에 포함된 id값에 대해 삭제 진행
DELETE FROM 
  articles
-- 삭제할 레코드 조건 : id값
-- 여러 id값 삭제
-- 삭제할 id값 선정 : id IN (SELECT 어쩌고저쩌고) 
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);
