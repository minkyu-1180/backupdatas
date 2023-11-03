# Vue
## 2. Basic Syntax-01

## 목차
1. Template Syntax
2. Dynamically data binding
3. Event Handling
4. Form Input Bindings

## 1. Template Syntax
### Template Syntax
Template Syntax : DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구분을 사용
- 선언적인 바인딩 : Vue instance와 DOM을 연결
- HTML 기반 템플릿을 통해 확장된 문법 제공
#### Template Syntax의 종류
1. Text Interpolation : 데이터 바인딩의 가장 기본 형태
```js
// 1. Text Interpolation
<p>Message : {{ msg }}</p>

// 2. Raw HTMl
// CSS
<div v-html='rawHtml'></div>
// Scripts
const rawHtml = ref('<span style="color:red">This should be red.</span>')

// 3. Attribute Bindings
// CSS
<div v-bind:id="dynamicId"></div>
// Scripts
const dynamicId = ref('my-id')
// 위의내용과 동일
<div id="my-id"></div>

// 4. JavaScript Expressions
<div>{{ number + 1 }}</div>
<div>{{ ok ? 'YES' : 'NO' }}</div>
<div>{{ msg.split('').reverse().join('') }}</div>
<div :id="`list-${id}`"></div>
```
- 이중 중괄호 구문 사용(called 콧수염 구문)
  - 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
- msg 속성이 변경될 때 마다 업데이트됨
2. Raw HTML
- 콧수염 구문은 데이터를 일반 텍스트로 해석
  - 실제 HTML을 출력하기 위해 v-html 사용
3. Attribute Bindings
- 콧수염 구문은 HTML 속성 내에서 사용할 수 없음
  - v-bind를 사용하여 HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화
- 바인딩 값이 null 또는 undefined인 경우 렌더링 요소에서 제거(id 속성이 비활성화)
4. JavaScript Expressions
- Vue는 모든 데이터 바인딩 내에서 JS 표현식의 모든 기능 지원
- Vue 템플릿에서 JS 표현식 사용 가능 위치
  - 1. 콧수염 구문 내부
  - 2. 모든 directive 속성(v-) 값
- 각 바인딩에는 하나의 단일 표현식만 포함(선언식, 삼항 표현식 등 사용 불가)
#### Directive
Directive : 'v-' 접두사가 있는 특수 속성
- Directive 속성 값 : 단일 JS 표현식(v-for, v-on 제외)
- 표현식 값이 변경될 때, DOM에 반응적으로 업데이트 적용
전체 구문 : v-{Name}:{Argument}.{Modifiers}="Value"

## 2. Dynamically data binding
### v-bind
v-bind : 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩
#### v-bind의 사용처
1. Attribute Bindings(HTML 속성에 바인딩)
- HTMl의 속성 값을 Vue의 상태 속성 값과 동기화
  - ':'로 v-bind: 표현 가능(shorthand)
- Dynamic attribute name(동적 인자 이름)
  - 대괄호로 감싸서 directive argument에 JS 표현식 사용 가능
  - 대괄호 안에 작성하는 이름은 반드시 소문자로 구성(브라우저가 속성 이름을 소문자로 강제 변환
  - )
2. Class and Style Bindings(Class 또는 Inline )
- v-bind를 사용하여 다른 속성과 마찬가지로 동적으로 문자열 값 할당 가능
  - 문자열 연결을 사용하여 값 생성은 오류 발생의 위험
  - Vue는 클래스 및 스타일과 함께 v-bind를 사용할 때 객체 또는 배열을 활용한 개선 사항 제공


## 3. Event Handling
### v-on
v-on : DOM 요소에 이벤트 리스너를 연결 및 수신