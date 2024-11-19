import { createRouter, createWebHistory } from 'vue-router'
import GuidepageView from '../views/GuidepageView.vue'

import ProfileMeView from '../views/profile/ProfileMeView.vue'
import ProfileView from '../views/profile/ProfileView.vue'

import UserupdateView from '../views/account/UserupdateView.vue'

import { useArticleStore } from '../stores/articles'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/guidepage',
      name: 'GuidepageView',
      component: GuidepageView
    },
    {
      path: '/profile',
      name: 'ProfileMeView',
      component: ProfileMeView
    },
    {
      // path: '/profile/:username',
      path: '/profileother',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/userupdate',
      name: 'UserupdateView',
      component: UserupdateView
    },
   
  ]
})

// router.beforeEach((to, from) => {
//   const store = useArticleStore()
//   // 만약 이동하는 목적지가 메인 페이지이면서
//   // 현재 로그인 상태가 아니라면 로그인 페이지로 보냄
//   if (to.name === 'ArticleView' && !store.isLogin) {
//     window.alert('로그인이 필요합니다.')
//     return { name: 'LogInView' }
//   }

//   // 만약 로그인 사용자가 회원가입 또는 로그인 페이지로 이동하려고 하면
//   // 메인 페이지로 보냄
//   if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
//     window.alert('이미 로그인 되어있습니다.')
//     return { name: 'ArticleView' }
//   }
// })

export default router
