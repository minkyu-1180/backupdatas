<template>
  <div>
    <form @submit.prevent="createTodo()" ref="formTag">
      <input type="text" v-model="todoText">
      <input type="submit" value="Todo 생성">
    </form>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'


// 사용자 입력 데이터를 받을 동적 변수
const todoText = ref('')
const formTag = ref(null)
const store = useCounterStore()


const createTodo = function () {
  // 반응형 객체를 넣었기 때문에 .value 사용
  // 사용하지 않으면 동기화됨
  store.addTodo(todoText.value)
  // input value를 초기화
  // todoText.value = ''
  formTag.value.reset()
}
</script>

<style scoped>

</style>