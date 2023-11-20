import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()

  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null) // 토큰을 저장할 변수 생성
  // 로그인 되어있는지?
  // computed를 활용하여 token 값이 변할 때만 계산
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  }) 
  

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      // 접근 권한 요청을 위한 headers 생성
      // Postman에서 Headers에 작성한 그대로 
      headers: { Authorization: `Token ${token.value}`}
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 회원가입 요청
  const signUp = function (payload) {
    // 구조 분해 할당
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      // 단축 속성
      data: { username, password1, password2 }
    })
      .then((response) => {
        console.log(response)
        // 회원가입 성공 후 자동으로 로그인 진행
        const password = password1
        logIn({ username, password })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: { username, password }
    })
      .then((response) => {
        // 로그인 성공 -> token.value에 해당 토큰 저장
        console.log(response.data)
        token.value = response.data.key
        // 로그인 성공 후, 게시글 페이지로 
        router.push({ name: 'ArticleView' })
      })
      .catch((error) => {
        console.log(error)
      })

  }

  return { articles, API_URL, token, getArticles, signUp, logIn, isLogin }
}, { persist: true })
