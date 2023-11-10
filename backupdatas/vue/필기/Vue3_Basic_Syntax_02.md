# Vue
## 3. Basic Syntax 3

## 목차

1. Computed Property
2. Conditional Rendering
3. List Rendering
4. Watchers
5. Lifecycle Hooks
6. Vue Style Guide

## 1. Computed Property
### Computed
computed() : 계산된 속성을 정의하는 함수
- 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄여주는 함수
```javascript
const { createApp, ref, computed } = Vue
```
#### computed의 특징
- 반환되는 값 : computed ref 객체(.value로 참조 / template에서는 .value 생략 가능)
- computed 속성은 의존된 반응형 데이터를 자동으로 추적
  - 의존하는 데이터가 변경될 때만 재평가

#### computed vs method
computed와 동일한 로직을 처리하는 method
- 실제로 두 가지 접근 방식은 완전히 동일
computed와 method의 차이
- computed : 의존된 반응형 데이터를 기반으로 캐시(cached) 된다
  - cached : 데이터나 결과를 일시적으로 저장해두는 임시 저장소(같은 데이터나 결과를 빠르게 접근할 수 있도록 돕는 공간)
- 의존하는 데이터가 변경될 경우에만 재평가됨
  - 즉, 의존된 반응형 데이터가 변경되지 않는 한, 다시 평가 X(이전에 계산된 결과를 즉시 반환)
- method : 렌더링이 발생할 때 마다 항상 함수를 실행
##### computed와 method의 적절한 사용처
computed
- 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
- 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지
method 
- 단순히 특정 동작을 수행하는 함수를 정의할 때 사용
- 데이터에 의존하는지 여부와 관계없이 항상 동일한 결과를 반환하는 함수



```javascript
// computed와 동일한 로직을 처리하는 method

// computed
const RestOfTodos = computed(() => {
  return todos.value.length > 0 ? 'Rest exists' : 'Done'
})
// computed 사용시 html
<p>{{ RestOftodos }}</p>

// method
const getRestOfTodos = function () => {
  return todos.value.length > 0 ? 'Rest exists' : 'Done'
}
// method 사용시 html
<p>{{ getRestOftodos() }}</p>

```
## 2. Conditional Rendering
### v-if
v-if : 표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링
- directive -> 하나의 요소에 적용
- v-else-if directive를 사용하여 v-if에 대한 else if 블록을 나타낼 수 있음
- v-else directive를 사용하여 v-if에 대한 else 블록을 나타낼 수 있음
#### 여러 요소에 대한 v-if 적용
v-if는 directive이기 때문에 단일 요소에만 연결 가능
- template 요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용 가능
### v-show
v-show : 표현식 값의 T/F를 기반으로 요소의 가시성(visibility)을 전환
- v-show 요소는 항상 렌더링 되어서 DOM에 남게 됨
- CSS display 속성만 전환
#### v-if vs v-show
공통점 : 조건부 렌더링 
차이점 
v-if : Cheap initial load, expensive toggle
- 초기 조건이 false인 경우, 아무 작업도 수행 X
- 토글 비용이 비쌈
- else, else-if 등 사용 가능
- 실행 중에 조건이 변경되지 않는 경우 권장
v-show : Expensive initial load, cheap toggle
- 초기 조건에 관계 없이 항상 렌더링
- 초기 렌더링 비용이 더 높음
- 무언가를 매우 자주 전환해야 하는 경우 권장

## 3. List Rendering
### v-for
v-for : 소스 데이터(Array, Object, Number, String, iterable)를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링
- alias in expression 형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭 제공
```javascript
<div v-for="item in items">
  {{ item.text }}
</div>
<div v-for="(item, index) in items">
</div>
<div v-for="(value, key, index) in items">
</div>
```
#### v-for with key
v-for는 반드시 key와 함께 사용해야 한다
- 내부 컴포넌트의 상태를 일관되게 유지하기 위맣
- 데이터의 예측 가능한 행동 유지(Vue 내부 동작 관련)
```javascript
// v-for with key
let id=0
const items = ref([
  { id:id++, name:'Alice'},
  { id::id++, name:'Bella'},
])

// html
// v-for 뒤에서 key 설정(고유값으로 설정)
<div v-for="item in items" :key="item.id">
  {{ item }}
</div>
```
#### v-for with v-if
v-for와 v-if를 함께 사용하지 않는다
- 동일한 요소에서 v-if가 v-for보다 우선순위가 더 높다
- v-if 조건은 v-for 범위의 변수에 접근할 수 없다
##### 해결 방법
1. computed
2. template
## 4. Watchers
### watch
watch() : 반응형 데이터를 감시하고, 감시하는 데이터가 변경될 경우 콜백 함수를 호출
#### watch의 구조
```javascript
watch(variable, (newValue, oldValue) => {
  // do something
})
```
- variable : 감시하는 변수
- newValue : 감시하는 변수가 변화된 값
- oldValue : 감시하는 변수가 변화되기 전의 값
#### computed와 watchers 비교
공통점
- 데이터의 변화를 감지하고 처리
- 의존(감시)하는 원본 데이터를 직접 변경 X
  - 변경되었을 때 작동
차이점
1. 동작
- computed : 의존하는 데이터 속성의 계산된 값을 반환
- watchers : 특정 데이터 속성의 변화를 감시하고 작업을 수행
1. 사용 목적
- computed : 템플릿 내에서 사용되는 데이터 연산용
- watchers : 데이터 변경에 따른 특정 작업 처리용
1. 사용 예시
- computed : 연산된 길이, 필터링된 목록 계산 등
- 비동기 API 요청, 연관 데이터 업데이트 등
## 5. Lifecycle Hooks
### Lifecycle Hooks
Lifecycle Hooks : Vue 인스턴스의 생애주기 동안 특정 시점에 실행되는 함수
- 개발자가 특정 단계에서 의도하는 로직이 실행될 수 있도록 함
#### Lifecycle Hooks의 특징
Vue는 Lifecycle Hooks에 등록된 콜백 함수들을 인스턴스와 자동으로 연결함
- hooks 함수들은 반드시 동기적으로 작성
- 
## 6. Vue Style Guide
