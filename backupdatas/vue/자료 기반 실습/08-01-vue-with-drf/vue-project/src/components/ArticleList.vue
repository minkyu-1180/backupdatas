<template>
  <div>
    <h3>Article List</h3>
    <!-- store.articles 배열의 객체반복 -->
    <!-- prop이름을 article로 해서 하향식 단방향으로 정보 보내기 -->
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article" 
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
console.log(store.articles)
</script>
