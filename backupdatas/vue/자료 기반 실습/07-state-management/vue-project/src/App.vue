<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoForm />
    <TodoList />
    
  </div>
</template>

<script setup>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'
import { useCounterStore } from '@/stores/counter'

// // 중앙 저장소의 state 가져오기
const store = useCounterStore()

</script>

<style scoped>
</style>
