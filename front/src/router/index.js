// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router'
import GuidepageView from '../views/GuidepageView.vue'

import SignUpView from '../views/account/SignUpView.vue'
import LogInView from '../views/account/LogInView.vue'

import ProfileMeView from '../views/profile/ProfileMeView.vue'
import ProfileView from '../views/profile/ProfileView.vue'

import MainView from '../views/movies/MainView.vue'
import RecommendDetailView from '../views/movies/RecommendDetailView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'
import SearchResultView from '../views/movies/SearchResultView.vue'

import UserupdateView from '../views/account/UserupdateView.vue'

import BoardView from '../views/reviews/BoardView.vue'
import BoardDetailView from '../views/reviews/BoardDetailView.vue'
import ReviewDetailView from '../views/reviews/ReviewDetailView.vue'
import ReviewCreateView from '../views/reviews/ReviewCreateView.vue'

import CreateDiscussionView from '../views/discussion/CreateDiscussionView.vue'
import TalkAiView from '../views/discussion/TalkAiView.vue'
import EmailVerificationView from '../views/account/EmailVerificationView.vue'

import { useAuthStore } from '../stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // account
    {
        path: '/email-verification',
        name: 'EmailVerification',
        component: EmailVerificationView
    },
    {
      path: '/account/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/account/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/account/userupdate',
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
      path: '/profile/:username',
      // path: '/profile/profileother',
      name: 'ProfileView',
      component: ProfileView
    },

    // movies
    {
      path: "/movies/main",
      name: "MainView",
      component: MainView,
    },
    {
      path: "/movies/:category",
      name: "RecommendDetailView",
      component: RecommendDetailView,
      props: true,
      beforeEnter: (to, from, next) => {
        if (isNaN(to.params.category)) next(); // category가 숫자가 아니면 이동 허용
        else next(false); // 숫자인 경우는 MovieDetailView로 이동
      },
    },
    {
      path: "/movies/:id(\\d+)", // 숫자만 허용
      name: "MovieDetailView",
      component: MovieDetailView,
      props: true,
    },
    {
      path: "/movies/search",
      name: "SearchResultView",
      component: SearchResultView,
      props: true,
    },
    
    // reviews
    {
      path: '/reviews/board',
      name: 'BoardView',
      component: BoardView,
    },
    {
      path: '/reviews/board/:movieId',
      // path: '/reviews/boarddetail',
      name: 'BoardDetailView',
      component: BoardDetailView,
      props: true,
    },
    {
      path: '/movies/:movieId/reviews/:id',
      name: 'ReviewDetailView',
      component: ReviewDetailView,
      props: true,
    },
    {
      path: '/reviews/:id',
      name: 'ReviewCreateView',
      component: ReviewCreateView
    },
    // discussion
    {
      path: '/craetediscussion',
      name: 'CreateDiscussionView',
      component: CreateDiscussionView
    },
    {
      path: '/talkai/:characterName/:characterPersonality/:characterImage',
      name: 'TalkAiView',
      component: TalkAiView,
      props: true,
    },
    
    {
      path: '/',
      name: 'GuidepageView',
      component: GuidepageView
    },
  ]
})

// router.beforeEach
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  // 인증된 사용자만 접근 가능한 페이지
  const authRequiredRoutes = [
    'ProfileMeView',
    'ProfileView',
    'MainView',
    'BoardView',
    'ReviewCreateView',
  ];

  // 인증되지 않은 사용자는 로그인 페이지로 리다이렉트
  if (authRequiredRoutes.includes(to.name) && !authStore.isAuthenticated) {
    alert('Cinerium 서비스 이용을 위해선 로그인이 필요합니다.');
    return next({ name: 'LogInView' });
  }

  // 이미 로그인한 사용자가 로그인/회원가입 페이지로 가려고 하면 메인 페이지로 리다이렉트
  if (['LogInView', 'SignUpView'].includes(to.name) && authStore.isAuthenticated) {
    alert('이미 로그인되어 있습니다.');
    return next({ name: 'MainView' });
  }

  // 기본적으로 모든 라우트 이동 허용
  next();
});


export default router
