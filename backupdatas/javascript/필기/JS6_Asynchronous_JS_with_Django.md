# JS
## 6. Ajax with Django

## 목차
1. Ajax와 서버
2. Ajax with follow
3. Ajax with likes

## 1. Ajax와 서버
### 1-1. 개요
#### Ajax
Ajax(Asynchronous JavaScript + XML) : JS의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술
- 요즘은 XML이 아닌 XHR, JSON 객체 활용이 증가

#### Ajax를 활용한 클라이언트 서버 간 동작
1. Client : 이벤트 발생
2. Client : XML 객체 생성 및 요청
3. Server : Ajax 요청 처리
4. Server : 응답 데이터 생성
5. Server : JSON 데이터 응답
6. Client : 응답 데이터를 활용하여 DOM 조작
## 2. Ajax with follow

## 3. Ajax with likes
### Ajax 좋아요 적용
#### 유의 사항
Ajax 적용은 팔로우와 모두 동일
- 단, 팔로우와 다르게 좋아요 버튼은 한 페이지에 여러 개가 존재
  - forEach()
  - querySelectorAll() 사용