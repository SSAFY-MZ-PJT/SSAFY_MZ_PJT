import { createRouter, createWebHistory } from 'vue-router'
import GuidepageView from '../views/GuidepageView.vue'

import SignUpView from '../views/account/SignUpView.vue'
import LogInView from '../views/account/LogInView.vue'

import ProfileMeView from '../views/profile/ProfileMeView.vue'
import ProfileView from '../views/profile/ProfileView.vue'

import MainView from '../views/movies/MainView.vue'
import RecommendDetailView from '../views/movies/RecommendDetailView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'

import UserupdateView from '../views/account/UserupdateView.vue'

import { useAuthStore } from '../stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // account
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/accounts/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/userupdate',
      name: 'UserupdateView',
      component: UserupdateView
    },

    // profile
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

    // movies
    {
      path: '/main',
      name: 'MainView',
      component: MainView
    },
    {
      // path: '/movies:(어떤 추천인가에 따라 이름지정)',
      path:'/movies',
      name: 'RecommendDetailView',
      component: RecommendDetailView
    },
    {
      // path: '/movies:movies.id',
      path:'/010307',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    
    
    {
      path: '/guidepage',
      name: 'GuidepageView',
      component: GuidepageView
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
