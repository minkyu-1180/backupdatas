# JS
# 1. Intro and DOM

## 목차
1. History of JavaScript
- 웹 브라우저와 JavaScript
- ECMAScript
2. JavaScript and DOM
- DOM
- DOM 선택
- DOM 조작
  - DOM 요소 조작


## 1. History of JavaScript
### 1-1. 웹 브라우저와 JavaScript
#### 웹의 탄생
웹의 탄생(1990)
- 팀 버너스리 경이 WWW, 하이퍼텍스트 시스템 고안
- URL, HTTP 최초 설계 및 구현
- 초기 웹 : 정적 텍스트 페이지만 지원
#### 웹 브라우저의 대중화
웹 브라우저의 대중화(1993)
- Netscape 사의 최초 상용 웹 브라우저 Netscape Navigator 출시
- 당시 약 90% 이상의 시장 점유율 보유
#### JavaScript의 탄생
JavaScript의 탄생(1995)
- 당시 Netscape 소속 개발자 Brancon Eich가 스크립트 언어 Mocha 개발
- 이후, LiveScript로 이름을 변경
  - 당시 가장 인기있던 프로그래밍 언어인 Java의 명성에 기대보고자, JavaScript로 이름 변경
- Netscape Navigator 2.0에 탑재되어 웹 페이지에 동적 기능을 추가하는 데 사용됨
#### JavaScript 파편화
JavaScript 파편화(1996)
- Microsoft가 자체 웹 브라우저인 Internet Exploser 3.0에 JavaScript와 유사한 JScript 도입
- 이처럼, 많은 회사들이 자체적으로 JavaScript를 독자적으로 변경하고, 이를 자체 브라우저에 탑재 
#### 1차 브라우저 전쟁
1차 브라우저 전쟁(1995-2001)
- Microsoft는 IE를 자사 윈도우 운영체제에 내장하여 무료로 배포
- IE의 시장 점유율은 2002년 약 96%에 달하며 Netscape 몰락
- 추후, Brandon Eich와 함께 Netscape에서 나온 핵심 개발진이 모질라 재단을 설립하여 Firefox 브라우저 출시(2003)
- 이를 통해, 웹 표준의 부재로 인해 각 기업에서 웹 표준의 중요성을 인식
#### ECMA Script 출시
ECMA Script 출시(1997)
- JavaScript의 파편화를 막기 위해 1997년 ECMA에서 ECMAScript라는 표준 언어 정의
- 이때부터 JavaScript는 ECMAScript 표준에 기반을 두고 발전하기 시작
#### 2차 브라우저 전쟁
2차 브라우저 전쟁(2004-2017)
- IE의 독주에 대한 Firefox의 대항 : 2008년까지 30%의 점유율 차지
- Google의 Chrome 브라우저 출시(2008)
  - 출시 3년만에 Firefox 점유율을 넘어서고, 그로부터 반년 뒤 IE의 점유율을 넘어섬
- 이를 통해, 웹의 기능이 크게 확장되며 웹 애플리케이션의 비약적인 발전
### 1-2. ECMAScript
#### ECMAScript
ECMAScript : 정보와 통신 시스템을 위한 국제 표준화 기구(Ecma International)이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
- 스크립트 언어가 준수해야 하는 규칙, 세부사항 등을 제공
#### ECMAScript와 JavaScript
JavaScript : ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
- EMAScript의 명세를 기반으로 하여 웹 브라우저나 Node.js와 같은 환경에서 실행
## 2. JavaScript and DOM
### 2-1. DOM
#### DOM의 개요
웹 브라우저에서의 JavaScript : 웹 페이지의 동적인 기능 구현
#### JavaScript 실행 환경 종류
1. HTML script 태그
2. js 확장자 파일
3. 브라우저 Console
#### DOM
DOM(The Document Object Model) : 웹 페이지(Document)를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함
#### DOM의 특징
1. DOM에서 모든 요소, 속성, 텍스트는 하나의 객체
2. 모두 document 객체의 자식으로 구성
3. DOM tree
- 브라우저는 HTML 문서를 해석하여 DOM tree라는 객체 트리로 구조화
  - 객체 간의 상속 구조 존재
4. DOM의 핵심 : 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API
####  document 객체
document 객체
- 웹 페이지 객체
- DOM tree의 진입점
- 페이지를 구성하는 모든 객체 요소 포함
- document.attribute로 객체의 속성을 지정하여 사용
### 2-2. DOM 선택
#### DOM 조작시 기억해야 하는 것
웹 페이지를 동적으로 만들기 == 웹 페이지를 조작하기
#### DOM 조작 순서
1. 조작 하고자 하는 요소 선택(탐색)
2. 선택된 요소의 콘텐츠 또는 속성 조작
#### 선택 메서드
1. document.querySelector() : 요소 한 개 선택
- 제공한 선택자와 일치하는 element 한 개 선택
- 제공한 CSS selector를 만족하는 첫 번째 element 객체 반환(없을 경우, null 반환)
1. document.querySelectorAll() : 요소 여러 개 선택
- 제공한 선택자와 일치하는 여러 element 선택
- 제공한 CSS selector를 만족하는 NodeList 반환
### 2-3. DOM 조작
#### 속성 조작
1. 클래스 속성 조작 : classList 
- 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
- element.classList.add() : 지정한 클래스 값 추가
- element.classList.remove() : 지정한 클래스 값 제거
- element.classList.toggle() : 클래스가 존재할 경우, 제거 후 false 반환(존재하지 않을 시, 클래스를 추가하고 true 반환)
2. 일반 속성 조작 : Attribute 관련
- Element.getAttribute() : 해당 요소에 지정된 값 반환(조회)
- Element.setAttribute(name, value) : 지정된 요소의 속성 값 설정(해당 요소에 이미 속성이 있을 경우, 기존 값을 갱신)
- Element.removeAttribute() : 요소에서 지정된 이름을 가진 속성 제거
#### HTML 콘텐츠 조작
HTML 콘텐츠 조작 : textContent
- 요소의 텍스트 콘텐츠를 표현

### 2-3-1. DOM 요소 조작
DOM 요소 조작 메서드
1. document.createElement(tagName) : 작성한 tagName의 HTMl 요소를 생성하여 반환
2. Node.appendChild() : 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입하고, 추가된 Node 객체 반환
3. Node.removeChild() : DOM에서 자식 Node를 제거 후 제거된 Node 반환
### 2-3-2. Style 조작
style : 해당 요소의 모든 style 속성 목록을 포함하는 속성
```javascript
const pTag = document.querySelector('p')
// style 속성 지정
pTag.style.color = 'crimson'
pTag.style.fontSize = '2rem'
```

### 참고

#### DOM의 기본 구성 단위
DOM 트리의 각 부분은 Node 객체로 표현
- Document Node : HTML 문서 전체를 나타내는 노드
- Element Node : HTML 요소를 나타내는 노드
- Text Node : HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타내는 노드
- Attribute Node : HTML 요소의 속성을 나타내는 노드