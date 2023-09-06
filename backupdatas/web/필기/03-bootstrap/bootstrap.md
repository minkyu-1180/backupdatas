# 3. Bootstrap

## 목차
### 1. Bootstrap
 - 개요
 - Typogrphy
 - Colors
 - Component
### 2. Semantic Web
  - 개요
  - Semantic in HTML
  - Semantic in CSS

## 1. Bootstrap

### Bootstrap
CSS 프론트엔드 프레임워크(Toolkit)
- 미리 만들어진 다양한 디자인 요소들을 제공하여 웹사이트를 빠르고 쉽게 개발할 수 있도록 하는 것
- [Bootstrap공식문서](https://getbootstrap.com/)
#### Bootstrap 기본 사용법
bootstrap은 기본적으로 클래스 사용
- {property}{sides}-{size} 형태로 클래스가 구성
![Alt text](<bootstrap에서 클래스 이름으로 spacing 표현-1.PNG>)
- Property :
- Sides : 방향
  - 쓰지 않을 경우, 네 방향 모두
- Size : 크기(브라우저의 기본 픽셀 : 16px)
  - rem * 16 = px가 되는 형태

#### Typography
Content - Typography에 가서 직접 써보기
#### Colors
Bootstrap color system : bootstrap이 지정하고 제공하는 색상 시스템
- Utilities - Colors에 가서 직접 써보기

### Component
Bootstrap Component : Bootstrap에서 제공하는 UI 관련 요소
- 버튼(Buttons), 네비게이션 바(Navbar), 카드(Cards), 폼, 드롭다운, 경고창(Alerts)
#### Component의 장점
일관된 디자인 제공 -> 웹사이트의 구성 요소 구축에 유용

## 2. Semantic Web

### Semantic Web
웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식
- 이 요소가 시각적으로 어떻게 보여질까??
- -> 이 요소가 가진 목적과 역할을 파악하기
![Alt text](<semantic web.PNG>)
#### HTML semantic element
검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하는 것에 도움
- header
- nav
- main
- article
- section
- aside
- footer
** 기능간의 차이는 X, 역할에 대한 구분
![Alt text](<semantic elements.PNG>)

#### semantic in CSS
OOCSS(Object Oriented CSS) - 객체 지향적 접근법을 적용하여 CSS 구성
- 효율적이고, 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인
- bootstrap도 OOCSS를 활용하여 클래스 이름 구성
OOCSS의 기본 원칙
- 구조와 스킨을 분리
- 컨테이너와 콘텐츠를 분리