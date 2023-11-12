# Vue
## 5. Component State Flow

## 목차
1. Passing Props
2. Component Events

## 1. Passing Props
부모는 자식에게 데이터를 전달하며(Pass Props), 자식은 자신에게 일어난 일을 부모에게 알린다(Emit event)
### Props
Props : 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는 데 사용되는 속성
- 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩(one-way-down binding) 형성(One-Way Data Flow)
#### Props의 특징
1. 부모 속성이 업데이트 될 경우, 자식에게 흐름(반대는 X)
- 자식 컴포넌트 내부에서 props를 변경 불가
- 부모 컴포넌트가 업데이트 될 때 마다 자식 컴포넌트의 모든 props가 최신 값으로 업데이트됨
2. 단방향
- 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지
#### Passing Props 과정
0. 사전 준비
- vue 프로젝트 생성
- 초기 생성된 컴포넌트 모두 삭제(App.vue 제외)
- src/assets 내부 파일 모두 삭제
- main.js 해당 코드 삭제
1. App - Parent - ParentChild 컴포넌트 관계 작성
```vue
<!-- App 컴포넌트 작성 -->
<!-- App.vue -->

<template>
    <div>
        <Parent />
    </div>
</template>

<script setup>
import Parent from '@/components/Parent.vue'
</script>

<!-- Parent 컴포넌트 작성 -->
<!-- Parent.vue -->

<template>
    <div>
        <ParentChild />
    </div>
</template>

<script setup>
import ParentChile from '@/components/ParentChild.vue'
</script>

<!-- ParentChild 컴포넌트 작성 -->
<!-- ParentChild.vue -->
<template>
    <div><div>
</template>

<script setup>
</script>
```
### Props 선언
props 선언 : 부모 컴포넌트에서 보낸 props를 사용하기 위해 자식 컴포넌트에서 명시적인 props 선언 필요
#### Props 선언의 2가지 방식
1. 문자열 배열을 사용한 선언 : defineProps([문자열])
```vue
<!-- 문자열 배열을 사용한 props 선언 -->
<!-- ParentChild.vue -->
<script setup>
defineProps(['myMsg'])
</script>
```
2. 객체를 사용한 선언 : defineProps({
    key: value
})
- key : props이름
- value : 값이 될 데이터 타입에 해당하는 생성자 함수(Number, String...)
- 객체 선언 문법 사용 권장
```vue
<!-- 객체를 사용한 props 선언 -->
<!-- ParentChild.vue -->
<script>
defineProps({
    myMsg: String
})
</script>
```
#### prop 데이터 사용법
- template : 반응형 변수와 같은 방식으로 활용

```vue
<!-- ParentChild.vue -->
<template>
    <div>
        <p>{{ myMsg }}</p>
    </div>
</template>

<script setup>
    // props를 객체로 반환 -> JS에서 접근 가능
    const props = defineProps({
        myMsg: String
    })
    console.log(props)
    console.log(props.myMsg)
</script>
```
##### 한 단계 더 prop 내려 보내기
```vue
<!-- 1. ParentChild 컴포넌트를 부모로 갖는 ParentGrandChild 컴포넌트 생성 및 등록 -->
<!-- ParentGrandChild.vue -->
<template>
    <div></div>
</template>

<script setup>
</script>

<!-- ParentChild.vue -->
<template>
    <div>
        <p>{{ myMsg }}</p>
        <ParentGrandChild />
    </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

defineProps({
    myMsg: String,
})
</script>

<!-- 2. ParentChild 컴포넌트에서 Parent로부터 받은 prop인 myMsg를 ParentGrandChild에게 전달 -->
<!-- ParentChild.vue -->
<template>
    <div>
        <p>{{ myMsg }}</p>
        <!-- v-bind를 사용한 동적 props -->
        <ParentGrandChild :my-msg="myMsg" />
    </div>
</template>
```
- ParentGrandChild가 받아서 출력하는 prop : Parent에 정의 되어있는 prop
- Parent가 prop을 변경할 경우, 이를 전달받고 있는 ParentChild, ParentGrandChild에서도 모두 업데이트 됨

### Props 세부사항
#### Props Name Casing
- 선언 및 템플릿 참조 시 : camelCase
- 자식 컴포넌트로 전달 시 : kebab-case
#### Static props & Dynamic props 
- 지금껏 작성한 것 : 정적 props
- v-bind를 사용하여 동적으로 할당된 props를 사용 가능
```javascript
// 1. Dynamic props 정의
// Parent.vue 
import { ref } from 'vue' 
const name = ref('Alice')

// Parent.vue
<ParentChile my-msg="message" : dynamic-props="name" />


// 2. Dynamic props 선언 및 출력
// ParentChild.vue
<p>{{ dynamicProps }}</p>


defineProps({
    myMsg: String,
    dynamicProps: String,
})


```
## 2. Component Events
### $emit(event, ...args)
emit : 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 메서드
- event : 커스텀 이벤트 이름
- args : 추가 인자

#### Event 발신 및 수신
1. $emit을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트 발신
<button @click="$emit('someEvent')">클릭</button>

2. 부모는 v-on을 사용하여 수신
- 수신 후 처리할 로직 및 콜백함수 호출
<ParentComp @some-event="someCallback" my-msg="message" :dynamic-props="name" />

```vue
<!-- Parent.vue -->

<template>
    <div>
        <ParentChild @some-event="someCallback" my-msg="message" :dynamic-props="name" />
    </div>
</template>

<script setup>
    const someCallback = function () {
        console.log('ParentChild가 발신한 이벤트 수신')
    }
</script>
```

#### emit Event 선언
defineEmits()를 사용하여 명시적으로 발신할 이벤트 선언 가능
- script에서 $emit 메서드 접근 불가 -> defineEmits()를 대신 사용하여 동등한 함수 반환
```vue
<template>
    <button @click="buttonClick">클릭</button>
</template>


<script setup>
    const emit = defineEmits(['someEvent', 'myFocus'])

    const buttonClick = function () {
        emit('someEvent')
    }
</script>

```
