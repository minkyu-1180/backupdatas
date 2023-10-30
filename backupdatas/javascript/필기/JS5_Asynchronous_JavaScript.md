# JS
## 5. Asynchronous JavaScript

## 목차
1. 비동기
2. JavaScript와 비동기
3. AJAX
4. Callback과 Promise


## 1. 비동기
### 1-1. 개요
#### 동기와 비동기
Synchronous(동기) : 프로그램의 실행 흐름이 순차적으로 진행되는  것
- 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식
Asynchronous(비동기) : 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식
- 작업의 완료 여부를 신경 쓰지 않고 동시에 다른 작업들을 수행할 수 있다
#### Asynchronous의 특징
Asynchronous의 특징 : 병렬적 수행
- 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
#### 병렬적 수행 예시
1. Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만, 실제로 메일을 보내는 작업은 병렬적으로 별도로 처리된다.
2. 브라우저는 웹페이지를 먼저 처리되는 요소부터 그려 나가며, 처리가 오래 걸리는 것들은 별도로 처리가 완료 되는대로 병렬적으로 처리된다.
## 2. JavaScript와 비동기
### 2-1. JavaScript와 비동기
#### Single Thread 언어, JavaScript
Thread : 작업을 처리할 때 실제로 작업을 수행하는 주체
- multi-thread : 업무를 수행할 수 있는 주체가 여러 개
JavaScript : 한번에 하나의 일만 수행 가능(Single Thread)
- 하나의 작업을 요청한 순서대로 처리
- JavaScript가 비동기 처리 하는 방법? 
  - 비동기 처리를 할 수 있도록 도와주는 환경이 필요
#### JavaScript Runtime
JavaScript Runtime : JavaScript가 동작할 수 있는 환경
- 브라우저 또는 Node와 같은 환경에서 처리
#### 브라우저
브라우저 환경에서의 JavaScript 비동기 처리 관련 요소
1. JavaScript Engine의 Call Stack : 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리된다.
- 요청이 들어올 때 마다 순차적으로 처리하는 Stack
- 기본적인 JS의 Single Thread 작업 처리
2. Web API : 오래 걸리는 작업이 Call Stack으로 들어올 경우, Web API로 보내 별도로 처리한다.
- JS 엔진이 아닌 브라우저에서 제공하는 Runtime 환경
- 시간이 소요되는 작업 처리(setTimeout, DOM Event, AJAX 요청 등)
3. Task Queue : Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가는 것이 아닌, Task Queue(FIFO)에 순서대로 들어간다.
- 비동기 처리된 Callback 함수가 대기하는 Queue
4. Event Loop : Event Loop는 Call Stack이 비어있는 것을 계속 체크하다가, Call Stack이 빌 경우 Task Queue에서 가장 오래된(First-In) 작업을 Call Stack으로 보낸다(First-Out)
- Call Stack과 Task Queue를 지속적으로 모니터링하는 JS 내의 루프
- Call Stack이 비어있을 경우, Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push


## 3. AJAX
### AJAX & XML
#### AJAX
AJAX(Asynchronous JavaScript + XML) : JavaScript의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술
#### XML
XMLHTTPRequest 객체 : 서버와 상호작용할 때 사용하며, 페이지의 새로고침 없이도 URL에서 데이터를 가져올 수 있다.
- 사용자의 작업을 방해하지 않고 페이지의 일부를 업데이트
- 주로 AJAX 프로그래밍에서 많이 사용

Event handler는 비동기 프로그래밍의 한 형태이다
- 이벤트가 발생할 때 마다 호출되는 콜백 함수 제공
- XMLHttpRequest(XHR)는 JavaScript를 사용하여 서버에 HTTP 요청을 할 수 있는 객체
- HTTP 요청 : 응답이 올 때 까지 걸릴수 있는 작업(비동기 API)
  - 이벤트 핸들러를 XHR 객체에 연결하여 요청의 진행 상태 및 최종 완료에 대한 응답을 받음
### Axios
Axios : JavaScript에서 사용되는 HTTP 클라이언트 라이브러리
- 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구
#### Axios 구조
1. get, post등 여러 http request method 사용 가능
2. then 메서드를 사용하여 성공하면 수행할 로직 작성
3. catch 메서드를 사용하여 실패하면 수행할 로직 작성
```js
axios({
  method: 'post',
  url: '/user/12345',
  data : {
    firstName: 'Fred',
    lastNae: 'Flintstone',
  }
})
.then(요청에 성공하면 수행할 callBack 함수)
.catch(요청에 실패하면 수행할 callBack 함수)
```
#### 정리
axios : 브라우저에서 비동기로 데이터 통신을 가능하게 하는 라이브러리
- 브라우저를 위해 XMLHttpRequest 생성
- 같은 방법으로 DRF로 만든 API 서버로 요청을 보내서 데이터를 받아온 후 처리할 수 있도록 함
## 4. Callback과 Promise
### 비동기 Callback
비동기 처리의 단점
- 비동기 처리의 핵심 : 작업이 완료되는 순서에 따라 처리(Web API로 들어오는 순서 x)
  - 개발자 입장에서 코드의 실행 순서가 불명확
- 실행 결과를 예상하면서 코드를 작성할 수 없게 함
#### 비동기 콜백
비동기 콜백 함수 : 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
- 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- 작업의 순서와 동작을 제어하거나 결과를 처리하는 데 사용
#### 비동기 콜백의 한계
비동기 콜백 함수의 사용 : 어떤 기능의 실행 결과를 받아서 다른 기능을 수행할 때 사용
- 콜백 지옥 발생 : A처리를 통한 결과 발생... 첫 번째 callback 함수실행 -> 첫 번째 callback 함수가 종료되면 두 번째 callback 함수 실행 -> .... 
### Promise
Promise : JS에서 비동기 작업의 결과를 나타내는 객체
- 비동기 작업이 완료되었을 때 결과값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능 제공
- 콜백 지옥 문제를 해결하기 위한 비동기 처리용 객체
- 작업이 끝나면 실행
- 비동기 작업의 성공 또는 실패를 나타내는 객체
- Axios : JS에서 사용되는 Promise 기반의 HTTP 클라이언트 라이브러리
  - then, catch 등 수직적으로 시행
#### then & catch
then과 catch는 항상 promise 객체를 반환
- 계속해서 chaining 가능
  - 비동기 작업의 순차적인 처리 기능
  - 코드의 직관성, 가독성 증가
1. .then(callback) : 요청한 작업이 성공할 경우 해당 callback 함수 실행
- callback은 이전 작업의 성공 결과(response)를 인자로 전달 받아서 호출
2. .catch(callback) : then()이 하나라도 실패할 경우 해당 callback 함수 실행
- callback은 이전 작업의 실패 객체를 인자로 전달 받음 

then chaining의 장점
1. 가독성
2. 에러 처리
3. 유연성
4. 코드 관리

#### Promise의 보장
1. 콜백 함수는 JS의 Event Loop가 현재 실행중인 Call Stack을 완료하기 이전에는 절대 호출 X
- Promise의 callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤, then() 메서드를 이용하여 추가한 경우에도 호출 순서를 보장하며 동작
3. then()을 여러 번 사용하여 여러 개의 callback 함수 추가 가능
- 각 callback 함수는 주어진 순서대로 실행
- chaining(Promise의 최대 장점)