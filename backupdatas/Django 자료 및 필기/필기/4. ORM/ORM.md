# 4. ORM

## 목차
1. ORM
2. QuerySet API
3. QuerySet API 실습
  - Create
  - Read
  - Update
  - Delete

------------------

## 1. ORM
### ORM
ORM(Object-Relational-Mapping) : 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간 데이터를 변환하는 기술
#### ORM의 역할
![ORM의 역할](<ORM의 역할_1.PNG>)

## 2. QuerySet API
### QuerySet API
QuerySet API : ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
- API를 사용하여 SQL이 아닌, Python 코드로 데이터를 처리
#### QuerySet API의 구조
![QuerySet API의 구조](<QuerySetAPI의 구조_1.PNG>)
- Manager : Queryset API 즉, 메서드를 사용하기 위해 필요한 것
#### Query와 QuerySet
1. Query : 데이터베이스에 특정 데이터를 보여 달라는 요청
- 쿼리문을 작성 : 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드 작성
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되에 데이터베이스에 전달됨
2. QuerySet : 데이터베이스에서 전달 받은 객체 목록(데이터들의 모음)
- 순회가 가능한 데이터 : 한 개 이상의 데이터를 불러와 사용 가능
- Django ORM을 통해 만들어진 자료형
- 데이터 베이스가 단일 객체를 반환 시, QuerySet이 아닌, 모델(Class)의 인스턴스로 반환

## 3. QuerySet API 실습
### QuerySet API 실습 사전 준비
1. 외부 라이브러리 설치 및 설정
- pip install ipython
- pip install django-extensions(얘는 settings.py에도 추가해주기)
2. Django shell 실행
- python manage.py shell_plus
### 3-1. Create
### 3-2. Read
### 3-3. Update
### 3-4. Delete