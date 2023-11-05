# JavaScript 정리

## 1. Intro and DOM
### 선택 메서드 
- document.querySelector('선택자') : 요소 한 개 선택
    - 제공하는 선택자와 일치하는 element 한 개 선택
    - 제공한 CSS 선택자를 만족하는 첫 번째 element 객체 반환(없을 경우, null 반환)
- document.querySelectorAll('선택할것') : 요소 여러개 선택
    - 제공한 선택자와 일치하는 모든 element 선택
    - 제공한 CSS 선택자를 만족하는 NodeList 반환
### 조작 메서드
#### 속성 조작
1. 클래스 속성 조작 : 요소의 목록을 DOMTokenList(유사 배열) 형태로 반환
- element.classList.add() : 지정한 클래스 값 추가
- element.classList.remove() : 지정한 클래스 값 제거
- element.classList.toggle() : 클래스가 존재한다면 제거하고 false 반환(없을 경우 클래스를 추가하고 true 반환)
2. 일반 속성 조작 메서드
- element.getAttribute() : 해당 요소에 지정된 값 반환(조회)
- element.setAttribute(name, value) : 지정된 요소의 속성 값 설정
    - 속성이 이미 있을 경우, 기존 값을 갱신
- element.removeAttribute(name) : 요소에서 지정된 이름을 가진 속성 제거
#### HTML 콘텐츠 조작
- element.textContent : 요소의 텍스트 콘텐츠를 표현
- element.textContent = 'new' : 요소의 텍스트 콘텐츠 수정
#### DOM 요소 조작
- document.createElement(tagName) : 작성한 tagName의 HTML 요소를 생성하여 반환
- parentnode.appendChild(child) : 한 노드를 특정 부모 노드의 자식 NodeList 중 마지막 자식으로 삽입 후, 추가된 해당 노드 객체 반환
- parentnode.removeChild(child) : DOM에서 자식 노드를 제거 후 제거된 노드 반환
#### style 조작
- element.style.attibute = '조작내용' : 해당 객체의 스타일 요소를 설정

## 2. Basic Syntax of JavaScript
### 변수
#### 변수명 작성 규칙
- 문자, 달러($), 밑줄(_)로 시작
- 대소문자 구분
- 예약어(for, if, function 등) 사용 불가
- 카멜 케이스(camelCase) : 변수, 객체, 함수에 사용
- 파스칼 케이스(PascalCase) : 클래스, 생성자에 사용
- 대문자 스테이크 케이스(SNAKE_CASE) : 상수에 사용
#### 변수 선언 키워드
1. let : 블록 스코프를 갖는 지역 변수 선언
- 재할당 가능 / 재선언 불가능
2. const : 블록 스코프를 갖는 지역 변수 선언
- 재할당 불가능 / 재선언 불가능
- 선언 시 초기값 반드시 설정
3. var : 함수 스코프를 가지는 지역 변수
- 재할당 가능 / 재선언 가능
- 호이스팅 되는 특성으로 인한 문제 발생 가능 
    - ES6 이후 const, let 사용 권장
- var, const, let 키워드를 사용하지 않고 변수 선언 시, 자동으로 var 선언
### 데이터 타입
#### 데이터 타입의 종류
##### 원시 자료형(Primitive) 
- 변수에 값이 직접 저장되는 자료형(불변, 값 복사)
- Number, String, Boolean, undefined, null
```javascript
// 1. Number
const a = 13
const b = -5
const c = 3.14
const d = 2.99e8
const e = Infinity
const f = -Infinity
const g = NaN

// 2. String
// 곱셈, 나눗셈, 뺄셈 불가능
const firstName = 'Tony'
const lastName = 'Stark'
const fullName = firstName + lastName

// 3. 템플릿 리터럴 : 내장된 표현식 허용
// Backtick을 이용
const age = 10
const message = `홍길동은 ${age}세 입니다.`

// 4. null
// 변수의 값이 없음을 의도적으로 표현시 사용
let a = null // 의도적으로 null을 할당
console.log(a) // null
typeof null // "object" (설계 당시 버그로 인해 원시 자료형 임에도 object type)
 
// 5. undefined 
// 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당
let b // 값을 할당 X
console.log(b) // undefined
typeof undefined // "undefined"

// 6. boolean
// undefined, null : 항상 false
// 0, -0, NaN : false
// 빈 문자열 : false
```
2. 참조 자료형(Reference) : Objects(Object, Array, Function) 
- 객체의 주소가 저장되는 자료형(가변, 주소가 복사)


### 연산자
#### 할당 연산자
- +=, -=, *=, %= 등의 단축 연산자 지원
- 증가, 감소 연산자 존재(++, --)
    - +=, -=등 보다 명시적인 표현 사용 권장
#### 비교 연산자(<, >)
피연산자들을 비교하고, 결과값을 boolean으로 반환
- <, >
#### 동등 연산자(==)
두 피연산자가 같은 값으로 평가되는 지 비교 후 boolean값 반환
- 암묵적 타입 변환
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
```javascript
console.log(1 == 1) // true
console.log('hello' == 'hello') // true
console.log('1' == 1) // true
console.log(0 == false) // true
```
#### 일치 연산자(===)
두 피연산자의 값과 타입이 모두 같은 경우 true 반환
- 같은 객체를 가리키거나, 같은 타입 & 같은 값인지 비교(엄격한 비교)
- 특수한 경우를 제외하고는 일치연산자 사용 권장
```javascript
console.log(1 === 1) // true
console.log('hello' === 'hello') // true
console.log('1' === 1) // false
console.log(0 === false) // false
```
#### 논리 연산자(&&, ||, !)
- 단축평가 지원
```javascript
true && false
true && ture
false || true
false || false
! true

1 && 0
0 && 1
4 && 7
1 || 0
0 || 1
```
### 조건문 
#### if 
```javascript
// if 조건문 
if (조건식1) {
   // 조건식 1이 true일 때의 결과
} else if (조건식) {
    // 조건식 2가 true일 때의 결과 
} else {
    // 조건식 1과 2과 false일 때의 결과
}

/// 조건 삼항 연산자 : 세 개의 피연산자를 받는 유일한 연산자
const func2 = function (person) {
    // person > 17이 true일 경우, ? 바로 뒤의 문자열 'Yes' 반환
    // false일 경우, : 바로 뒤의 문자열 'No' 반환
    return person > 17 ? 'Yes' : 'No'
}
```
### 반복문
#### while
while : 조건문이 참일 경우 문장을 계속해서 수행
#### for
for : 특정 조건이 거짓으로 판별될 때 까지 반복
- 초기문, 조건문, 증감문을 세미콜론(;)으로 나누어 소괄호(()) 내부에 작성
#### for...in
for ... in : 객체의 열거 가능한 속성에 대해 반복
- 속성 열거 -> 인덱스 반환 보장 X
- 인덱스의 순서가 중요할 경우 사용 X
#### for...of
for ... of : 반복 가능한 객체에 대해 반복
- 배열의 경우, for 또는 for..of 반복문 사용
- dictionary 같은 경우, not iterable -> 사용 불가
```javascript 
// while 
let i = 0
while (i < 6) {
    console.log(i)
    i ++
}
// for
// 초기 : i = 0
// 조건문 내부 진입 조건 : i < 6
// 조건문 내부 표현식 실행 후, 증감문 실행 : i += 1
for (let i = 0; i < 6; i++) {
    console.log(i)
}

// for...in
const fruits = {a : 'apple', b : 'banana'}
for (const fruit in fruits) {
    console.log(fruit) // a, b
    console.log(fruits[fruit]) // apple, banana
}
// for...of
const numbers = [1, 2, 3]
for (const number of numbers) {
    console.log(number) // 1, 2, 3
}
```
### 참고
NaN을 반환하는 경우
- 숫자로서 읽을 수 없을 때(Number(undefined))
- 결과가 허수인 수학 계산(Math.sqrt(-1))
- 피연산자가 NaN(7 ** NaN)
- 정의할 수 없는 계산식(0 * Infinity)
- 문자열을 포함하면서 덧셈이 아닌 계산식('가'/3)

## 3. JavaScript Reference data types
### 함수
Function : 참조 자료형에 속하며 모든 함수는 Function object
#### 함수의 정의
함수의 구조
- 이름
- 매개변수
- 함수 body statement
- return 값(없을 경우, undefined 반환)
#### 함수 정의 방법
1. 선언식(declaration)

2. 표현식(expression)
- 익명 함수 사용 가능
- 선언식과 달리, 표현식으로 정의한 함수는 호이스팅 되지 않음(함수 정의 전 사용 불가)
- 사용 권장
```javascript
// 함수 선언식
function func () {
    statements
}
// 함수 표현식
const func = function () {
    statements
}
```
#### 매개변수
매개변수 정의 방법
1. 기본 함수 매개변수 : 값이 없거나 undefined가 전달될 경우, 이름이 붙은 매개변수를 기본값으로 초기화(default 적용)

2. 나머지 매개변수 : 임의의 수의 인자를 배열로 허용하여 가변 인자 나타내는 방법
- 함수 정의 시, 나머지 매개변수 하나만 작성 가능
- 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치
- 매개변수의 개수가 인자의 개수보다 많은 경우, 누락된 인자는 undefined 할당
- 매개변수의 개수가 인자의 개수보다 적은 경우, 초과 입력한 인자는 사용 X
- para1, para2, ...restPara처럼 나머지 매개변수 앞에 ...를 작성
```javascript
// 기본함수 매개변수
const func1 = function (name='adam') {
    return `Hi! ${name}!`
}
func1() // Hi! adam!
// 나머지 매개변수
const func2 = function (para1, para2, ...restPara) {
    return [para1, para2, restPara]
}
func2(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
func2(1, 2) // [1, 2, []]
```
#### 매개변수와 인자의 개수 불일치
```javascript
// 매개변수의 개수 > 인자 개수
// 누락된 인자는 undefined로 할당
const threeArgs = function (para1, para2, para3) {
    return [para1, para2, para3]
}
threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]

// 매개변수의 개수 < 인자 개수
// 초과 입력한 인자는 사용 X
const oneArgs = function (para) {
    return para
}
oneArgs(1, 2) // 1
```

#### Spread Syntax
Spread Syntax(전개 구문) : 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것(확장, 전개)
- 전개 대상에 따라 역할이 다름
    - 함수와의 사용
    - 객체와의 사용(이후)
    - 배열과의 사용(이후)
```javascript
// 전개 구문 활용
// 함수와의 사용
// 1. 함수 호출(확장)
function myFunc(x, y, z) {
    return x + y + z
}
let numbers = [1, 2, 3]
console.log(myFunc(...numbers)) // 6

// 2. 나머지 매개변수(압축)
function myFunc2(x, y, ...rest) {
    return [x, y, rest]
}
console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
```
#### 화살표 함수
화살표 함수 : 함수 표현식의 간결한 표현법
- function 키워드 제거 후, 매개변수와 중괄호 사이에 화살표 작성
    - 함수의 매개변수가 하나일 경우, 매개변수를 감싸는 괄호(()) 제거 가능(권장 X)
- 함수 body 부분의 statement가 한 줄일 경우, {}와 return 제거 가능
- 인자가 없을 경우, () 또는 _로 표시 가능
- 객체를 반환하는 경우, return을 명시적으로 작성
    - return을 작성하기 않을 경우, 반환할 객체를 소괄호로 감싸야 함
```javascript
// 일반 함수 표현식
const arrow = function (name) {
    return `hello, ${name}!`
}

// 화살표 함수 표현식
const arrow = name => `hello, ${name}`
```
### 객체
#### Object
Object : 키로 구분된 데이터 집합을 저장하는 자료형
#### Object의 구조
- 중괄호를 이용하여 작성
- 중괄호 내부 속성 : key:value 쌍
    - key : String형만 허용
    - value : 모든 자료형 허용
- 점(.) 또는 대괄호([])를 이용하여 해당 객체의 요소에 접근, 수정, 삭제 가능
    - key의 이름에 띄어쓰기 같은 구분자가 있을 경우, 대괄호 접근만 가능
    - 접근 : object.key / object[key]
        - key의 이름에 띄어쓰기가 있을 시, 대괄호로 접근
    - 수정 : object.key = '수정 내용'
    - 삭제 : delete object.key
- in 연산자를 사용하여 속성이 객체에 존재하는지에 대한 여부 확인 가능
- object.method() 방식으로 호출 가능
    - 메서드는 객체를 행동할 수 있게 함
- 키의 이름과 값으로 쓰이는 변수의 이름이 같은 경우, 단축 구문 사용 가능
- 메서드 선언 시 function 키워드 생갹 가능
- 구조 분해 할당(배열, 객체를 분해하여 속성을 변수에 쉽게 할당)
```javascript
// 단축 구문
// 객체 생성
const name='Alice'
const age = 30
const user = {
    name,
    age,
}

// 메서드선언
const myObj2 = {
    myFunc() {
        return 'Hello'
    }
}

// 구조 분해 할당
const user = {
    firstName : 'MK',
    userId : 'minkyu1180',
    userAge : 15,
}
const {firstName, userId, userAge } = user
// 구조 분해 할당 활용
function printInfo({name, age, city}) {
    console.log(`이름 : ${name}, 나이 : ${age}, 도시 : ${city}`)
}

const person = {
    name : 'Bob',
    age : 35,
    city : 'London',
}
printInfo(person)

// Object with 전개 구문
// 얕은 복사에 활용 가능
const obj = {b:2, c:3, d:4}
const newObj = {a:1, ...obj, e:5}
console.log(newObj) // {a:1, b:2, c:3, d:4, e:5}
```

#### this
this : 함수나 메서드를 호출한 객체를 가리키는 키워드
- JS의 함수는 호출 시 this를 암묵적으로 전달 받음
- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
- this 키워드를 사용하여 객체에 대한 특정 작업(method) 수행 가능
- 대상이 전역 객체일 경우, 단순 호출
- 대상이 메서드를 호출한 객체일 경우, 메서드 호출
```javascript
// 단순 호출
const myFunct = function () {
    return this
}
console.log(myFunc()) // window

// 메서드 호출
const person = {
    name : 'MK',
    greeting : function () {
        return `Hello, my name is ${this.name}`
    }
}
console.log(person.greeting())
```

#### Optional Chaining('?.')
속성이 없는 중첩 객체에 에러 없이 접근 가능
- 참조 대상이 null 또는 undefined인 경우, 에러 발생 대신 평가를 멈추고 undefined 반환
```javascript
const user = {
    name:'Alice',
    greeting: function () {
        return 'hello'
    }
}
// ?. 사용
console.log(user.address?.street)
console.log(user.nonMethod?.())
// && 연산자 사용
console.log(user.address && user.address.street) // console.log(user.address?.street)와 똑같음
```

#### JSON
JSON(JavaScript Object Notation) : Key-Value 형태로 이루어진 자료 표기법
- 형식이 있는 문자열
- JS에서 JSON을 사용하기 위해서는 Object 자료형으로 변경 후 사용
```javascript
const object = {
    coffee : 'Americano',
    iceCream : 'Cookie',
}
// obj -> JSON
const objToJson = JSON.stringify(object) // string 타입

// JSON -> obj
const jsonToObj = JSON.parse(objToJson)
// object 타입
```

### 배열
Array : 순서가 있는 데이터 집합을 저장하는 자료구조
- 대괄호를 이용하여 작성
- 배열의 요소 자료형 : 제약 X
- length 속성을 통해 배열에 담긴 요소의 개수 확인 가능
#### 배열의 메서드
##### push / pop
- pop() : 배열의 끝 요소를 제거 후 반환
- push() : 배열의 끝 요소를 추가
#### shift / unshift 
- shift() : 배열의 앞 요소를 제거 후 반환
- unshift() : 배열의 앞 요소를 추가
#### Array Helper Methods
배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 함수(callback)를 받음
- 3가지 매개변수로 구성
    - item : 처리할 배열의 요소(필수)
    - index : 처리할 배열 요소의 인덱스(선택)
    - array : forEach를 호출한 배열(선택)
##### forEach
forEach() : 인자로 주어진 콜백함수를 배열 요소 각각에 대해 실행
- 반환 값 : undefined
map() : 배열 내의 모든 요소 각각에 대해 콜백함수를 호출하고, 함수 호출 결과를 모아서 새로운 배열 반환
```javascript
// forEach
const names = ['kim', 'lee', 'park']

names.forEach(callBack (item, index, array) {
    console.log(item, index, array)
})

// map
const result = names.map(callBack (item, index, array) {
    return item.length
})

```

## 3. Event
### Controlling Event
Event : 무엇인가 일어났다는 신호, 사건
- 모든 DOM 요소는 이러한 event를 만들어낸다.
- event object : DOM에서 이벤트가 발생했을 때 생성되는 객체
- event handler : 이벤트가 발생했을 때 실행되는 함수(ex. .addEventListner())
    - DOM요소가 event를 받음
    - event handler를 통해 받은 event를 처리
#### .addEventListener(type, handler)
- type : 수신할 이벤트 이름(문자열로 작성)
- handler : 발생한 이벤트 객체를 수신하는 콜백 함수
#### target & currentTarget
target : 이벤트가 발생한 가장 안쪽 요소를 참조하는 속성
- 실제 이벤트가 시작된 target 요소
- 버블리이 진행 되어도 변화 X
currentTarget : 현재 요소
- 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
- this


```javascript
// 버튼을 클릭하면(event) 버튼 요소 출력(event handler)

// 1. 버튼 선택
const btn = document.querySelector('#btn')

// 2. 콜백함수 정의
// 발생한 이벤트(event) 객체를 유일한 매개변수로 받음(반환 X)
const callBack = function (event) {
    console.log(event)
    console.log(event.currentTarget)
    console.log(this)
}

// 3. 이벤트 핸들러를 이벤트 대상(버튼)에 부착
btn.addEventListener('click', callBack)
```

### 버블링
버블링 : 한 요소에 이벤트가 발생 시, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작
- 가장 최상단의 조상 요소(document)를 만날 때 까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작

#### preventDefault()
.preventDefault() : 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정
- event.preventDefault()

## 4. Asynchrounous JavaScript
### 비동기
Synchronous(동기) : 프로그램의 실행 흐름이 순차적으로 진행되는 것
- 하나의 작업이 완료된 후, 다음 작업이 실행
Asynchronous(비동기) : 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 것
- 동시에 다른 작업들을 수행 가능
- 병렬적 수행
- 당장 처리 불가능한(시간이 필요한) 작업들은 별도로 요청을 보낸 뒤, 응답이 빨리 오는 작업부터 처리
#### JS와 비동기
JavaScript는 SingleThread언어이다
- 작업 처리 시, 실제로 작업을 수행하는 주체가 하나
- JS에서는 어떻게 비동기 처리가 이루어질까?
#### JS Runtime
JavaScript Runtime : JavaScript가 동작할 수 잇는 환경
- 비동기와 관련한 작업은 브라우저 또는 Node와 같은 환경에서 처리
##### 브라우저 환경에서의 JS 비동기 처리 관련 요소
1. JS Engine의 Call Stack
2. Web API
3. Task Queue
4. Event Loop
#### 비동기 처리 동작
1. 모든 작업은 Call Stack으로 들어간 후 처리
2. 오래 걸리는 작업이 Call Stack으로 들어간 경우, 해당 작업을 Web API로 보내서 처리하도록 한다
3. Web API에서 처리가 끝난 작업들은 바로 Call Stack으로 들어가는 것이 아닌, Task Queue에 순서대로 들어간다
4. Event Loop가 Call Stack의 상태를 체크하다가, 비어있따면 Task Queue에서 가장 먼저 처리되어 들어온 작업을 Call Stack으로 전달한다.

### AJAX
AJAX(Asynchronous JS + XML) : JS의 비동기 구조와 XML 객체를 활용하여 비동기적으로 서버와 통신하여 웹 페이지의 일부분만 업데이트하는 웹 개발 기술
- 요즘은 XML 대신 JSON을 더 많이 사용하기는 함
XMLHttpRequest 객체 : 서버와 상호작용할 때 사용하며, 페이지의 새로고침 없이도 URL에서 데이터를 가져올 수 있음
- 사용자의 작업을 방해하지 않고 페이지의 일부를 업데이트
- 주로 AJAX 프로그래밍에 많이 사용됨

### Axios
Axios : JavaScript에서 사용되는 HTTP 클라이언트 라이브러리
- 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구
- get, post 등 여러 http request method 사용 가능
- then 메서드 사용 : 성공하면 수행할 콜백함수 작성
- catch 메서드 사용 : 실패하면 수행할 콜백함수 작성
```javascript
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
axios({
    method : 'post',
    url : '/user/12345/',
    data : {
        firstName : 'Fred',
        lastName : 'Flinstone',
    }
})
    .then(요청에 성공시 수행할 콜백함수)
    .catch(요청에 실패하면 수행할 콜백함수)
</script>
```
#### Axios 실습
```javascript
// html
<button>냥냥펀치</button>

// script
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
const URL = ''
const btn = document.querySelector('button')

const getCats = function () {
    axios({
        method:'get',
        url:URL,
    })
      .then((response) => {
        imgUrl = response.data[0].url
        imgElem = document.createElement('img')
        imgElem.setAttribute('src', imgUrl)
        document.body.appendChild(imgElem)
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
        console.log('실패했다옹')
      })
}
btn.addEventListener('click', getCats)

```
### Callback과 Promise
#### 비동기 처리의 단점
Web API로 들어오는 순서가 아닌, 작업이 완료되는 순서에 따라 처리
- 개발자 입장에서 코드의 실행 순서가 불명확
- 콜백 함수를 사용함으로써 해결
```javascript
// 비동기 콜백
const asyncTask = function (callBack) {
    setTimeout(function () {
        console.log('비동기 작업 완료')
        callback()

    }, 2000)
}

// 비동기 작업 수행 후, 콜백 실행
asyncTask(function () {
    console.log('작업 완료 후 콜백 실행')
})
```
비동기 콜백의 한계 : 콜백 지옥
- 이를 해결하기 위해 Promise 객체를 사용

#### Promise
JavaScript에서 비동기 작업의 결과를 나타내는 객체
- 비동기 작업이 완료되었을 때 결과값을 반환 or 실패시 에러를 처리할 수 있는 기능 제공
- Axios도 결국 Promise 기반의 라이브러리
```javascript
//promise

word1()
    .then((result1) => {
        // work2
        return result2
    })
    .then((result2) =>{
        // work3
        return result3
    })
    .catch((error) => {
        // error handling
    })
```
then과 catch는 항상 promise 객체 반환
- chaining 가능
- axios로 처리한 비동기 로직이 항상 promise 객체 반환 -> then을 계속 이어나가면서 작성 가능

#### then 메서드 chaining의 장점
1. 가독성
- 비동기 작업의 순서와 의존 관계의 명확
2. 에러 처리
- 각각의 비동기 작업 단계에서 발생하는 에러를 분할 가능
3. 유연성
- 각 단계마다 필요한 데이터 가공 및 다른 비동기 작업 수행 가능
4. 코드 관리
- 비동기 작업을 분리함으로써 코드 관리에 용이