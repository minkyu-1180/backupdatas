<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <!-- 제목 -->
        <input type="text" v-model="title">
      </div>
      <div>
        <!-- 내용 -->
        <textarea v-model="content"></textarea>
      </div>
      
      <!-- 제출버튼 -->
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
// axios 필요
const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value,
    }
  })
    .then((response) => {
      // console.log(response)
      
      router.push({ name: 'ArticleView'})
    })
    .then((error) => {
      console.log(error)
    })
  }


</script>

<style>

</style>
