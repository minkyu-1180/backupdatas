# Vue
## 6. Router

## 목차
1. Routing
2. Vue Router
3. Navigation Guard

## 1. Routing
### Routing
Routing : 네트워크에서 경로를 선택하는 프로세스
- 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술
#### SSR에서의 Routing
1. 서버가 사용자가 방문한 URL 경로를 기반으로 응답 전송
2. 링크를 클릭하면 브라우저는 서버로부터 HTML 응답을 수신하고, 새 HTML로 전체 페이지를 다시 로드
3. SPA에서 routing은 브라우저의 클라이언트 측에서 수행
4. 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져와 전체 페이지를 다시 로드하지 않음
- 페이지는 1개이지만, 링크에 따라 여러 컴포넌트를 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 함
#### routing이 없을 경우
- 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
- 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - URL이 1개이기 때문에 새로 고침 시 처음 페이지로 되돌아감
    - 링크를 공유할 시 첫 페이지만 공유 가능
- 브라우저의 뒤로 가기 기능을 사용할 수 없음
## 2. Vue Router
### Vue Router
Vue Router : Vue 공식 라우터
- Vite로 프로젝트 생성 시 Router 추가
    - Add Vue Router for Single Page Application development에서 Yes 선택
```vue
<!-- App.vue -->
<template>
    <header>
        <nav>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/about">About</RouterLink>
        </nav>
    </header>
    <!-- URL에 해당하는 컴포넌트를 표시 -->
    <!-- 어디에나 배치하여 레이아웃에 맞출 수 있음 -->
    <RouterView />
</template>
```
router/index.js : 라우팅에 관련된 정보 및 설정이 작성되는 곳
- router에 URL과 컴포넌트를 
views : RouterView 위치에 렌더링 할 컴포넌트를 배치
- 기존 components 폴더와 기능적으로 다른 것은 없으며 단순 분류의 의미로 구성됨
- 일반 컴포넌트와 구분하기 위해 컴포넌트 이름을 View로 끝나도록 작성하는 것을 권장
### Basic Routing
#### 라우팅 기본
1. index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)
2. RouterLink의 to 속성으로 index.js에서 정의한 주소 속성 값(path) 사용
### Named Routes
Named Routes : 경로에 이름을 지정하는 라우팅
- name 속성 값에 경로에 대한 이름 지정
- 경로에 연결하기 위해 RouterLink에 v-bind를 사용하여 "to" prop 객체로 전달
#### Named Routes의 장점
- 하드 코딩 된 URL을 사용하지 않아도 됨
- URL 입력 시 오타 방지
```javascript
// index.js
const router = createRouter({
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        ...
    ]
})
```
```vue
<!-- App.vue -->
<RouterLink :to="{name: 'home'}">Home</RouterLink>
<RouterLink :to="{name: 'about'}">About</RouterLink>
```
### Dynamic Route Matching with Params
Dynamic Route Matching with Params : 매개 변수를 사용한 동적 경로 매칭
- 주어진 패턴 경로를 동일한 컴포넌트에 매핑 해야 하는 경우 활용
- 예를 들어 모든 사용자의 ID를 활용하여 프로필 페이지 url을 설계 할 경우?
    - url/1
    - url/2
    - url/3 등, 일정한 패턴의 URL 작성 반복
#### 매개 변수를 사용한 동적 경로 매칭 활용
1. UserView 컴포넌트 작성
```vue
<template>
    <div>
        <h1>UserView</h1>
    </div>
</template>
```
2. UserView 컴포넌트 라우트 등록
- 매개변수는 콜론(:)으로 표기
```javascript
// 매개변수를 사용한 동적 경로 매칭 활용
// index.js
import UserView from '../views/UserView.vue'

const router = createRouter({
    routes: [
        {   // 매개변수를 사용하여 UserView 컴포넌트 라우트 등록
            // 매개변수는 콜론(:)으로 표기
            path: '/user/:id',
            name: 'user',
            component: UserView
        },
    ]
})
```
3. 컴포넌트에서 라우트의 매개변수 참조
```vue
<!-- UserView.vue -->
<template>
    <div>
        <h1>UserView</h1>
        <!-- 라우트 매개변수는 컴포넌트에서 $route.params로 참조 가능 -->
        <h2>{{ $route.params.id }}번 User 페이지</h2>
    </div>
</template>
```
4. 권장 방법 : Composition API 방식으로 작성
```javascript
// Composition API 방식 

// UserView.vue
// template
<div>
    <h1>UserView</h1>
    <h2>{{ userId }}번 User 페이지</h2>
</div>


// script
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)
```

### Programmatic Navigation
프로그래밍 방식 네비게이션 : router의 인스턴스 메서드를 사용하여 RouterLink로 a태그를 만드는 것 처럼, 프로그래밍으로 네비게이션 관련 작업 수행 가능
- 다른 위치로 이동 : router.push()
- 현재 위치 바꾸기 : router.replace()
#### router.push() 
router.push() : 다른 URL로 이동하는 메서드
- 새 항목을 history stack에 push 하므로, 사용자가 브라우저 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
- RouterLink를 클릭했을 때 내부적으로 호출되는 메서드
    - <RouterLink :to=""> vs router.push()
    - RouterLink를 클릭하는 행위(선언적) === router.push()를 호출하는 것(프로그래밍적)
```javascript
// router.push 인자 활용 참고

// literal string path
router.push('/users/alice')

// object with path
router.push({path: 'users/alice'})

// named route with params to let the router build the url
router.push({name : 'user', params: {username : 'alice'}})

// with query, resulting in /register?plan=private
router.push({path: '/register', query: {plan: 'private' }})
```
#### router.replace()
router.replace : 현재 위치 바꾸기
- push 메서드와 달리 history stack에 새로운 항목을 push하지 않고 다른 URL로 이동
    - 따라서, 이동 전의 URL로 뒤로 가기 불가
    - <RouterLink :to="" replace> vs router.replace
    - RouterLink클 클릭하는 행위(선언적) === router.replace를 호출하는 것(프로그래밍적)

## 3. Navigation Guard
### Navigation Guard
Navigation Guard : Vue router를 통해 특정 URL에 접근할 때, 다른 URL로 redirect를 하거나 취소하여 네비게이션 보호
- 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함
#### Navigation Guard의 종류
1. Globally(전역 가드) 
- 애플리케이션 전역에서 동작
- index.js에서 정의
2. Per-route(라우터 가드)
- 특정 route에서만 동작
- index.js의 각 routes에 정의
3. In-component(컴포넌트 가드)
- 특정 컴포넌트 내에서만 동작
- 컴포넌트 Script에 정의
#### Globally Guard
router.beforeEach() : 다른 URL로 이동하기 직전에 실행되는 함수
- Global Before Guards
```javascript
// router.beforeEahc의 구조
router.beforeEach((to, from) => {
    ...
    return false
})
// to : 이동할 URL 정보가 담긴 Route 객체
// from : 현재 URL 정보가 담긴 Route 객체
// 선택적 반환값 
// 1. false -> 현재 내비게이션 취소
// 2. Route Location (ex. {name: 'About'}) -> router.push()를 호출하는 것 처럼 위치를 전달하여 다른 위치로 redirect
// 3. no return -> 'to' URL Route 객체로 이동
```
#### Per-route
router.beforeEnter() : route에 진입했을 때만 실행되는 함수
- 매개변수, 쿼리 값이 변경될 때는 실행되지 않고, 다른 경로에서 탐색할 때만 실행됨
- index.js의 routes 객체에서 정의
- 함수의 to, from, return 인자는 beforeEach와 동일
```javascript
// router.beforeEnter의 구조
const router = createRouter({
    routes: [
    {
        path: 'user/:id',
        name: 'user',
        component: UserView,
        beforeEnter: (to, from) => {
            ..., 
            return false
        }
    }
    ]
})
```
#### In-component
컴포넌트 가드의 종류
1. onBeforeRouteLeave : 현재 라우트에서 다른 라우트로 이동하기 전에 실행
- 사용자가 현재 페이지를 떠나는 동작에 대한 로직 처리
```javascript
// onBeforeRouteLeave 활용
// UserView.vue
import { onBeforeRouteLeave } from 'vue-router'

onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('정말 떠나실 건가요?')
    if (answer === false) {
        return false
    }
})

```
2. onBeforeRouteUpdate : 이미 렌더링된 컴포넌트가 같은 라우트 내에서 업데이트 되기 전에 실행
- 라우트 업데이트 시 추가적인 로직 처리
```javascript
// onBeforeRouteUpdate 활용
// UserView.vue
<button @click="routeUpdate">100번 유저 페이지</button>

import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const routeUpdate = function () {
    router.push({ name: 'user', parames: { id: 100 } })
}

onBeforeRouteUpdate((to, from) => {
    userId.value = to.paramse.id
})

```