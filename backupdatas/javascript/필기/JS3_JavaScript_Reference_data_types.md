# JS
# 3. JavaScript Reference data types

## 목차
1. 함수
2. 객체
3. 배열

## 1. 함수
### 개요
#### Function 
Function : 참조 자료형
- 모든 함수는 Function object

### 함수의 정의
#### 함수의 구조
1. 함수 이름
2. 함수의 매개변수
3. 함수의 body를 구성하는 statement
4. return값이 없을 경우, undefined 반환
```javascript
function name([param[, param, [..., param]]]) {
  statements

  return value
}
```
#### 함수 정의의 2가지 방법
1. 선언식(function declaration)
2. 표현식(function expression)
- 익명 함수 사용 가능
- 호이스팅이 되지 않으므로, 함수 정의 전 먼저 사용 X
- 표현식을 권장
```javascript
// 선언식
function funcName() {
  statements
}

// 표현식
const funcName = function () {
  statements
}
```
### 매개변수
#### 매개변수 정의 방법
1. 기본 함수 매개변수(Default function parameter) : 값이 없거나 undefined가 전달될 경우, 이름이 붙은 매개변수를 기본값으로 초기화
2. 나머지 매개변수(Rest parameters) : 임의의 수의 인자를 배열로 허용하여 가변 인자를 나타내는 방법
- 작성 규칙
  - 1. 함수 정의 시, 나머지 매개변수 하나만 작성 할 수 있다.
  - 2. 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 한다.
#### 매개변수와 인자의 개수가 불일치 할 때
1. 매개변수의 개수 > 인자의 개수 : 누락된 인자는 undefined로 할당
2. 매개변수의 개수 < 인자의 개수 : 초과 입력한 인자를 사용하지 않음
```javascript
const threeArgs = function (para1, para2, para3) {
  return [para1, para2, para3]
}
// 매개변수의 개수 > 인자의 개수
threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(2, 3) // [2, 3, undefined]

// 매개변수의 개수 < 인자의 개수
threeArgs(1, 2, 3, 4) // [1, 2, 3]
```
#### Spread syntax
Spread syntax(...) : 전개 구문
- 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것(확장, 전개)
- 전개 대상에 따라 다른 역할을 가짐
1. 함수와의 사용
- 함수 호출 시 인자 확장
- 나머지 매개변수(압축)
```javascript
// 전개 구문
// 함수와의 사용

// 1. 함수 호출 시 인자 확장
function myFunc (x, y, z) {
  return x + y + z
}
let numbers = [1, 2, 3]
console.log(myFunc(...numbers)) // 함수 소출 시, 인자 확장

// 2. 나머지 매개변수(압축)
function myFunc2(x, y, ...restArgs) {
  return [x, y, restArgs]
}

console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
console.log(myFunc2(1, 2)) // [1, 2, []]
```
2. 객체와의 사용(객체 파트에서 설명)
3. 배열과의 사용(배열 파트에서 설명)

#### 화살표 함수
화살표 함수 표현식(Arrow function expressions) : 함수 표현식의 간결한 표현법
1. function 키워드 제거 후, 매개변수와 중괗로 사이에 화살표(=>) 작성
2. 함수의 매개변수가 한 개일 경우, 매개변수를 감싸는 괄호(()) 생략 가능(생략하지 않는 것을 권장)
3. 함수 본문의 표현식이 한 줄일 경우, 중괄호({})와 return 제거 가능

## 2. 객체
객체 : 키로 구분된 데이터 집합(data collection)을 저장하는 자료형
### 구조 및 속성
#### 객체 구조
1. 중괄호를 이용해 작성
2. 중괄호 안에는 key:value 쌍으로 구성된 속성(property)를 여러 개 작성 가능
3. key는 문자형만 허용
4. value는 모든 자료형 허용
5. 점, 또는 대괄호로 객체 요소에 접근 가능
- key의 이름에 띄어쓰기 같은 구분자가 있을 경우, 대괄호 접근만 가능
```javascript
// 객체 구조
conts user = {
  name:'Alice',
  'key with space' : true,
  greeting : function () {
    return 'hello'
  }
}
// 속성 참조
console.log(user.name) // Alice
console.log(user['key with space']) // true
// 속성 추가
user.address = 'korea'
// 속성 수정
user.name = 'Minkyu'
// 속성 삭제
delete user.address

// in 연산자 : 속성이 객체에 존재하는지에 대한 여부 확인
console.log('greeting' in user)
```
### 객체와 함수
#### Method
Method : 객체의 속성에 정의된 함수
- object.method() 방식으로 호출
#### this
this : 함수는 메서드를 호출한 객체를 가리키는 키워드
this 키워드를 통해 객체에 대한 특정 작업을 수행 가능
- 함수를 호출하는 방법에 따라 가리키는 대상이 달라진다.
  - 단순 호출 -> 전역 객체 대상
  - 메서드 호출 -> 메서드를 호출한 객체
- JavaScript의 함수는 호출 시, this를 암묵적으로 전달받는다
- Pythond의 self, Java의 this 선언 시 값이 이미 정해지는 것에 비해, JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고, 호출 시에 결정된다(동적 할당)
```javascript
// method와 this 사용
const person = {
  name:'Alice',
  greeting: function () {
    return `Hello my name is ${this.name}`
  },
}

console.log(person.greeting())

// 단순 호출
const myFunc = function () {
  return this
}
console.log(myFunc()) // window

// 메서드 호출
const myObj = {
  data: 1,
  myFunc: function () {
    return this
  },
}
console.log(myObj.myFunc()) // myObj
```
#### 추가 객체 문법
1. 단축 속성
- 키 이름과 값이 쓰이는 변수의 이름이 같은 경우, 단축 구문을 사용할 수 있다
2. 단축 메서드
- 메서드 선언 시, function 키워드를 생략 가능하다
3. 계산된 속성(computed property name)
- 키가 대괄호로 둘러싸여 있는 속성의 경우, 고정된 값이 아닌 변수 값을 사용할 수 있다.
4. 구조 분해 할당(destructing assignment)
- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있다
5. Object with 전개구문(...)
- 객체를 복사(객체 내부에서 객체 전개)
- 얕은 복사에 활용 가능
6. 유용한 객체 메서드
- Object.keys(객체명)
- Object.values(객체명)
7. Optional chaining('?.')
- 속성이 없는 중첩 객체를 에러 없이 접근 가능
- 참조 대상이 없을 경우(null or undefined) 에러 발생 대신 평가를 멈추고 undefined 반환
- Optional chaining이 없을 경우, && 연산자를 사용

### JSON
JSON(JavaScript Object Notation) 
- Key-Value의 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사구조
  - JSON : 형식이 있는 문자열
- JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경
```javascript
// 객체 생성
const jsObject = {
  coffee : 'Americano',
  iceCreame : 'Cookie and cream'.,
}

// Object -> JSON
const objToJson = JSON.stringify(jsObject)
// JSON -> Object
const jsonToObj = JSON.parse(objToJson)
```
#### new 연산자
new 연산자 : 사용자 정의 객체 타입 생성
- 기존 : 같은 key값을 가지고 있는 여러 객체를 만들어야 할 경우 : 생성할 때 마다 다른 객체를 선언하여 생성

- 매개변수 (new constructor[([arguments])])
  - constructor : 객체 인스턴스의 타입을 기술하는 함수
  - arguments : constructor와 함께 호출될 값 목록
```javascript
// new 연산자 활용
function Member(name, age, sId) {
  this.name = name
  this.age = age
  this.sId = sId
}

const member = new Member('MK', 26, 19980811)
```

## 3. 배열
### 배열
Array : 순서가 있는 데이터 집합을 저장하는 자료구조
#### 배열 구조
1. 대괄호([])를 이용해 작성
2. 배열 요소의 자료형에는 제약 없음
3. length 속성을 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음
- 음수 인덱스(끝에서부터)가 없기 때문에, length 속성을 활용하여 역순으로 인덱스에 접근 가능
#### 배열의 주오 메서드
1. push / pop : 배열의 끝 요소를 추가 / 제거(후 반환)
2. unshift / shift : 배열의 앞 요소를 추가 / 제거(후 반환)
3. Array Helper Methods : 배열을 순회하며(반복) 특정 로직 수행
- 호출 시, 인자를 함수로 받아서 호출
  - forEach : 인자로 주어진 함수(callback)를 배열 요소 각각에 대해 실행
    - arr.forEach(callback(item[, index[, array]]))
      - item : 처리할 배열의 요소
      - index : 처리할 배열 요소의 인덱스(선택 인자)
      - array : forEach를 호출할 배열(선택 인자)
    - 반환 값 : undefined(no return)
  - map : 배열 내의 모든 요소 각각에 대해 함수(callback)을 소출하고, 함수의 호출 결과를 모아 새로운 배열 반환
    - arr.map(callback[item[, index[, array]]])
      - item : 처리할 배열의 요소
      - index : 처리할 배열 요소의 인덱스(선택 인자)
      - array : map을 호출한 배열 (선택 인자)
    - 반환 값 : 배열의 각 요소에 대해 실행한 callback의 결과를 모은 새로운 배열
Callback Function : 다른 함수에 인자로 전달되는 함수
- 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업 진행
```javascript
const names = ['Alice', 'Bella', 'Cathy', ]

// forEach
names.forEach(function (item, index, array)) {
  console.log(`${item} / ${index} / ${array}`)
}

```