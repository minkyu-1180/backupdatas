<template>
  <div>
    <h1>Article Page</h1>
    <!-- 게시글 생성을 위한 RouterLink -->
    <RouterLink :to="{name: 'CreateView'}">
      [CREATE]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
// 1. ArticleView 컴포넌트에 ArticleList 컴포넌트와 ArticleListItem 컴포넌트 등록 및 출력
import ArticleList from "@/components/ArticleList.vue"
// lifecycle : ArticleView에 요청이 갈 때 나와야 함 -> onMounted 사용
import { onMounted } from 'vue'
import { useCounterStore } from "@/stores/counter"
import { RouterLink } from 'vue-router'


const store = useCounterStore()
// onMounted가 될 때, store.getArticles() 호출
// 지금 하려는 것 : vue -> django 페이지로 요청 보내기 
// 서로 다른 Origin(URL의 Protocol, Host, Port가 모두 같아야 함)을 가짐 -> 응답을 막음(SOP 정책)
// CORS 정책의 등장(교차 출처 리소스 공유) : 서로 다른 출처의 데이터 공유 가능
// CORS 적용 방법 : "HTTP Response Header"(Access-Control-Allow-Origin)
// django-pjt/settings.py에서 적절한 조치를 취해서 통과시키기
onMounted(() => {
  store.getArticles()
})
</script>

<style>

</style>
