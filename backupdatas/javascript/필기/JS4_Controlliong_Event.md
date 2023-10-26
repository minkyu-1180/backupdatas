# JS
# 4. Controlling Event

## 목차
1. 이벤트
2. event handler 활용

## 1. 이벤트
### 1-1. 개요
#### 일상/웹의 이벤트
일상속의 이벤트
- 컴퓨터 키보드를 눌러 텍스트를 입력하는 것
- 전화벨이 울려 전화가 왔음을 알리는 것
- 손을 흔들어 인사하는 것
- 전화기의 버튼을 눌러서 통화를 사용하는 것
- 리모컨을 사용하여 채널을 변경하는 것
웹에서의 이벤트
- 버튼을 클릭했을 때 팝업 창이 출력되는 것
- 마우스 커서의 위치에 따라 드래그 앤 드롭 하는 것
- 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것
웹에서는 이벤트를 통해 특정 동작을 수행한다
### 1-2. event
#### event
event : 무엇인가 일어났다는 신호, 사건
- 모든 DOM 요소는 이러하느 event를 만들어낸다
event object : DOM에서 이벤트가 발생했을 때 생성되는 객체
- DOM 요소는 event를 받고, 받은 event를 '처리'할 수 있음
  - event handler를 통해 받은 event를 처리
#### event의 종류
[이벤트의 종류](https://developer.mozilla.org/en-US/docs/Web/API/Event)
- mouse, input, keyboard, touch 등...

## 2. event handler

### 2-1. event handler
event handler : 이벤트가 발생했을 때 실행되는 함수
- 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것
1. .addEventListener() : 특정 이벤트를 DOM 요소가 수신 할 때 마다 콜백 함수를 호출
- 구조 : EventTarget.addEventListner(type, handler)
  - EventTarget : DOM 요소
  - type : 수신할 이벤트
    - 문자열로 작성(ex. 'click')
  - handler : 콜백 함수
    - 발생한 Event object를 유일한 매개변수로 수신
  - 대상(EventTarget : DOM 요소)에 특정 Event(type)가 발생하면 지정한 이벤트를 받아 할 일(handler)을 등록한다
.addEventListner 활용 : 버튼을 클릭하면 버튼 요소 출력하기
- 이벤트 : 버튼을 클릭 
- 콜백 함수 : 버튼 요소 출력
- 버튼에 이벤트 처리기를 부착 -> 클릭 event가 발생할 경우, 이벤트가 발생한 버튼의 정보를 출력
.addEventListner()의 콜백함수 특징
- 발생한 이벤트를 나타내는 Event 객체를 유일한 매개변수로 받는다
- 아무것도 반환하지 않는다
#### bubbling
bubbling : 한 요소에 이벤트가 발생할 경우, 이 요소에 할당된 이벤트 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현산
- 최상단의 조상 요소(document)를 만날 때 까지, 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작
이벤트가 정확히 어디서 발생했는지 접근하는 방법
1. event.target : 이벤트가 발생한 가장 안쪽의 요소를 참조하는 속성
- 실제 이벤트가 발생한 요소
- 버블링과 상관 없이 변화 X
2. event.currentTarget : 현재 요소
- 항상 이벤트 핸들러가 부착된 요소만을 참조하는 속성
- this = event.currentTarget