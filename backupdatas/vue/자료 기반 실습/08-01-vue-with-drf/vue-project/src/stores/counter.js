import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {
  const articles = ref([
    // { id: 1, title: 'Article 1', content: 'Content 1' },
    // { id: 2, title: 'Article 2', content: 'Content 2' },  
  ])
  const API_URL = 'http://127.0.0.1:8000'

  // DRF에 article 조회 요청을 보내는 action
  // npm install axios를 통해 
  const getArticles = function () {
    axios({
      method: 'get',
      // drf url
      url: `${API_URL}/api/v1/articles/`
    })
      .then((response) => {
        // console.log(response)
        // 받아온 데이터를 저장
        articles.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return { articles, API_URL, getArticles }
}, { persist: true })
