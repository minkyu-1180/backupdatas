-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터를 위한 테이블 생성

-- 사용자의 정보(id, name)을 담을 users 테이블 생성
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);
-- users table의 id값을 외래 키로 참조하여 사용할
-- 게시글 관련 articles 테이블 생성
CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  -- 테이블에서 외래 키 참조 방법
  -- 외래 키를 담을 필드 명 : userId
  -- 외래 키 : id
  -- 외래 키를 를 받아올 테이블 : users -> users(id)를 참조(REFERENCES)
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);


-- users 테이블에 레코드 생성
-- id : 1 / name : 하석주
-- id : 2 / name : 송윤미
-- id : 3 / name : 유하선
INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

-- articles 테이블에 레코드 생성
-- userId : 1(users(id) = 1)인 사용자가 작성한 게시글 : 3개(제목1, 제목3, 제목5)
INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN

-- 모든 필드 조회
SELECT
  * 
-- 메인 테이블 : articles
FROM 
  articles
-- INNER JOIN 할 테이블 : users
INNER JOIN 
  users 
  -- INNER JOIN할 조건 : users.id(pk)값이랑 articles.userId(fk)값이랑
  -- 같은 필드값 조회
  ON users.id = articles.userId;

-- INNER JOIN 활용 1
-- 1번 회원(하석주)가 작성한 모든 게시글의 제목과 작성자명 조회

-- 게시글의 제목, 작성자명 조회
SELECT 
  -- 어떤 테이블의 필드값을 조회할 것인지 확실하게 명시
  -- 게시글의 제목
  articles.title, 
  -- 해당 게시글을 작성한 사용자의 이름
  users.name 
-- 게시글로부터 조회(main table 선정)
FROM 
  articles
-- INNER JOIN할 테이블 : users
INNER JOIN 
  users
  -- 조건 : user.id(pk)와 articles.userId(fk)가 같은 레코드에 대해 INNER JOIN 실행 
  ON users.id = articles.userId
-- INNER JOIN의 조건 : 1번 회원
WHERE users.id = 1;


-- LEFT JOIN
-- LEFT JOIN 활용 1

-- articles 테이블(LEFT)의 모든 필드값 조회
-- 조회 시, users 테이블(RIGHT)와 LEFT JOIN
-- LEFT JOIN 조건 : articles.userId(fk) = users.id(pk)
-- 왼쪽 테이블의 레코드 중, 오른쪽 테이블의 레코드와 일치하지 않는 레코드들은
-- 일치하지 않는 필드값에 대해 NULL 부여
SELECT * FROM articles
LEFT JOIN users 
  ON users.id = articles.userId;

-- LEFT JOIN 활용 2
-- LEFT JOIN 시, 게시글을 작성한 이력이 없는 회원 정보 조회
-- user(LEFT) article(RIGHT)로 두고, 뽑았을 때, article.userId 가 NULL값인 애
SELECT * FROM users
LEFT JOIN articles 
  ON articles.userId = users.id
WHERE articles.userId IS NULL;


-- 심화 (직접 해보기)
-- CREATE TABLE articles (
  -- id INTEGER PRIMARY KEY AUTOINCREMENT,
  -- title VARCHAR(50) NOT NULL,
  -- content VARCHAR(100) NOT NULL,
  -- userId INTEGER NOT NULL,
  -- FOREIGN KEY (userId) 
  --   REFERENCES users(id)
--     ON DELETE SET NULL
-- );

-- INSERT INTO 
--   users (name)
-- VALUES 
--   ('권미자'),
--   ('류준하'),
--   ('정영식'),
--   ('테스트');

-- DELETE FROM users 
-- WHERE id = 4;
