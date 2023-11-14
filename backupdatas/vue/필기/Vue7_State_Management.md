# Vue
## 7. State Management

## 목차
1. State Management
2. State Management Library(Pinia)
3. Pinia 실습

## 1. State Management
### State Management
State Management : 상태(데이터) 관리
- Vue Component는 이미 반응형 상태를 관리하고 있음

#### 컴포넌트 구조의 단순화
1. 상태(State) : 앱 구동에 필요한 기본 데이터
2. 뷰(View) : 상태를 선언적으로 매핑하여 시각화
3. 기능(Actions) : 뷰에서 사용자 입력에 대해 반응적으로 상태를 변경할 수 있게 정의된 동작
- 단방향 흐름(상태 -> 뷰 -> 기능 -> 상태 -> ...)의 간단한 표현
```vue
<template>
  <!-- 뷰(view) -->
  <div>{{ count }}</div>
</template>

<script setup>
import { ref } from 'vue'
// 상태(State)
const count = ref(0)

// 기능(Actions)
const increment = function () {
  count.value++
}
</script>
```
#### 상태관리의 단순성이 무너지는 경우
상태관리의 단순성이 무너지는 경우 : 여러 컴포넌트가 상태를 공유할 때 발생
1. 여러 뷰가 동일한 상태에 종속되는 경우
- 공유 상태를 공통 조상 컴포넌트로 끌어올린 다음 props로 전달하는 것
- 계층 구조가 깊어질 경우 비효율적이고 관리가 어려워진다
2. 서로 다른 뷰의 기능이 동일한 상태를 변경시켜야 하는 경우
- 발신된 이벤드(emited event)를 통해 상태의 여러 복사본을 변경 및 동기화하는 것
- 관리의 패턴이 깨지기 쉽고, 유지 관리할 수 없는 코드가 됨
#### 상태관리 해결책
Pinia : 각 컴포넌트의 공유 상태를 추출하여 전역에서 참조할 수 있는 저장소(중앙 저장소)
- 컴포넌트 트리는 하나의 큰 "view"가 되고 모든 컴포넌트는 트리 계층 구조에 관계 없이 상태에 접근하거나 기능을 사용할 수 있음
- Vue의 공식 상태 라이브러리
## 2. State Management Library(Pinia)
### Pinia
Pinia : Vue 공식 상태 관리 라이브러리
#### Pinia 설치
- Vite 프로젝트 빌드 시 Pinia 라이브러리 추가
- Vite 프로젝트/src/stores/counter.js에서 { defineStore } 모듈 import 확인
- npm install 후 npm run dev -> 개발자 도구에서 Pinia 확장 프로그램 확인 가능
#### Pinia의 구성 요소
1. store : 중앙 저장소(stores/counter.js)
- 모든 컴포넌트가 공유하는 상태, 기능 등이 작성됨
- 기본 저장소 이름 : counter(변경 가능)
2. state : 반응형 상태(데이터)
- ref() === state
3. getters : 계산된 값
- computed() === getters
4. actions : 메서드
- function() === actions
5. plugin : 애플리케이션의 상태 관리에 필요한 추가 기능을 제공하거나 확장하는 도구나 모듈
- 애플리케이션의 상태 관리를 더욱 간편하고 유연하게 만들어주며 패키지 매니저로 설치 이후 별도 설정을 통해 추가됨
## 3. Pinia 실습
### Pinia를 활용한 Todo 프로젝트 구현
1. Todo CRUD
2. Todo 개수 계산
- 전체 Todo
- 완료된 Todo
- 미완료된 todo
#### 컴포넌트 구성
App - (TodoForm, TodoList-TodoListItem)