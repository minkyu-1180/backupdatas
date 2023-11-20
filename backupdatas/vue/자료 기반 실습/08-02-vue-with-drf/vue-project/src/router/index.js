import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})



// 인증되지 않은 사용자에 대한 메인 페이지 접근 제한
// 전역 네빅이션 가드 beforeEach 활용
import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  // 게시글 전체 조회를 할 때, token값이 없는 경우
  // 로그인 페이지로 넘어감
  if (to.name === 'ArticleView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }

  // 이미 로그인이 되어있는 상태에서 회원가입View 혹은 로그인View로 넘어가려 할 때
  if ((to.name === 'SignUpView' || to.name === 'LogInView') & (store.isLogin)) {
    window.alert('현재 로그인이 되어있는 상태입니다.')
    return { name: 'ArticleView' }
  }
})
export default router
