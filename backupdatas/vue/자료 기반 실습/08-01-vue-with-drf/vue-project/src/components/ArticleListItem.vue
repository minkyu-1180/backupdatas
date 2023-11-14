<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">[Detail]</RouterLink>
    <hr> 
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

// 내려받은 props 데이터타입 명시
defineProps({
  article: Object
})
</script>
