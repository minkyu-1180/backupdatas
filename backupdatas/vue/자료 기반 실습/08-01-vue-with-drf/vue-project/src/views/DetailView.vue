<template>
  <div>
    <h1>Detail</h1>
    <!-- <p>{{ article }}</p> -->
    <!-- article에 null값이 들어있는 경우 방지 -->
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>생성일자 : {{ article.created_at }}</p>
      <p>최근 수정일자 : {{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref()
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,

  })
    .then((response) => {
      // console.log(response)
      article.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})

</script>

<style>

</style>
