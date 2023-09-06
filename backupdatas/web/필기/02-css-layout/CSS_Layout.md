# CSS Layout

## 목차
### 1. CSS Box Model
  - 구성 요소
  - 박스 타입
  - 기타 display 속성
### 2. CSS Layout Position
  - CSS Position
### 3. CSS Layout Flexbox
  - 구성요소
  - 레이아웃 구성

## 1. CSS Box Model

### CSS Box Model
CSS Box Model : 모든 HTML 요소를 사각형 박스로 표현하는 개념
![Alt text](<박스 요소로 이루어진 웹페이지.PNG>)

<CSS Box Model의 구성요소>
- 내용(content) : 컨텐츠가 표시되는 영역
- 안쪽 여백(padding) : 컨텐츠 주위에 위치하는 공백 영역
- 테두리(border) : 컨텐츠, 패딩을 감싸는 영역
- 외부 간격(margin) : 다른 요소와 현재 박스 요소 사이의 공백에 해당하는 가장 바깥 영역
![Alt text](<CSS Box Model의 구성요소.PNG>)
- 개발자 도구 -> Computed에서 확인 가능(값 수정도 가능)

<Box 구성의 방향 별 명칭>
![Alt text](<Box 구성의 방향 별 명칭.PNG>)
- top, bottom, left, right

#### width & height 속성
요소의 너비와 높이 지정
- 컨텐츠 영역 대상으로 함(border 기준 X)
  - box-sizing이 content-box가 디폴트이기 때문
- 실제 박스는 크기가 더 커진다
- 해결 방법 : content 기준이 아닌, border 기준으로 설정

### 박스 타입
Normal flow : CSS를 적용하지 않을 시, 웹 페이지 요소가 기본적으로 배치되는 방향
![Alt text](<Normal Flow.PNG>)

#### block type의 특징
- 항상 새로운 행으로 나뉜다
- width, height 속성을 사용하여 너비와 높이 지정 가능
- width 속성을 지정하지 않을 시, inline 방향으로 사용 가능한 공간을 모두 차지
- 대표적인 block 타입의 태그 : h1 ~ h6, p, div

#### inline type의 특징
- 새로운 행으로 나뉘지 않음
- width와 height 속성을 사용 x
- 수직 방향 : padding, margin, border이 적용되지만, 다른 요소는 밀어낼 수 없음
- 수평 방향 : padding, margin, border가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그 : a, img, span

![Alt text](<block과 inline의 차이.PNG>)
- block : margin-left, right
- inline : text-align

#### inline-block
inline과 block 요소 사이의 중간 지점을 제공하는 display의 값
- block 요소의 특징을 가진다
  - width, height 속성 사용 가능
  - padding, margin, border로 인해 다른 요소가 밀려남
- 요소가 줄 바꿈되지 않으면서 너비와 높이를 적용하고 싶은 경우 사용

#### none
요소를 화면에 표시하지 않고, 공간조차 부여되지 않는 것