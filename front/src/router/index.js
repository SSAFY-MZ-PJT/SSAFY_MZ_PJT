import { createRouter, createWebHistory } from 'vue-router';
import GuidepageView from '../views/GuidepageView.vue';

import SignUpView from '../views/account/SignUpView.vue';
import LogInView from '../views/account/LogInView.vue';

import ProfileMeView from '../views/profile/ProfileMeView.vue';
import ProfileView from '../views/profile/ProfileView.vue';

import MainView from '../views/movies/MainView.vue';
import RecommendDetailView from '../views/movies/RecommendDetailView.vue';
import MovieDetailView from '../views/movies/MovieDetailView.vue';

import UserupdateView from '../views/account/UserupdateView.vue';

import BoardView from '../views/reviews/BoardView.vue';
import BoardDetailView from '../views/reviews/BoardDetailView.vue';
import ReviewDetailView from '../views/reviews/ReviewDetailView.vue';
import ReviewCreateView from '../views/reviews/ReviewCreateView.vue';

import CreateDiscussionView from '../views/discussion/CreateDiscussionView.vue';
import TalkAiView from '../views/discussion/TalkAiView.vue';
import EmailVerificationView from '../views/account/EmailVerificationView.vue';

import { useAuthStore } from '../stores/auth';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // account
    {
      path: '/email-verification',
      name: 'EmailVerification',
      component: EmailVerificationView,
    },
    {
      path: '/account/login',
      name: 'LogInView',
      component: LogInView,
    },
    {
      path: '/account/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    {
      path: '/account/userupdate',
      name: 'UserupdateView',
      component: UserupdateView,
    },

    // profile
    {
      path: '/profile',
      name: 'ProfileMeView',
      component: ProfileMeView,
    },
    {
      path: '/profile/profileother',
      name: 'ProfileView',
      component: ProfileView,
    },

    // movies
    {
      path: '/movies/main',
      name: 'MainView',
      component: MainView,
    },
    {
      path: '/movies/:category',
      name: 'RecommendDetailView',
      component: RecommendDetailView,
      props: true,
    },
    {
      path: '/movies/:id',
      name: 'MovieDetailView',
      component: MovieDetailView,
      props: true,
    },

    // reviews
    {
      path: '/reviews/board',
      name: 'BoardView',
      component: BoardView,
    },
    {
      path: '/reviews/:movieId/boarddetail',
      name: 'BoardDetailView',
      component: BoardDetailView,
      props: true,
    },
    {
      path: '/reviews/:id',
      name: 'ReviewDetailView',
      component: ReviewDetailView,
      props: true,
    },
    {
      path: '/reviews/create/:id',
      name: 'ReviewCreateView',
      component: ReviewCreateView,
    },
    // discussion
    {
      path: '/craetediscussion',
      name: 'CreateDiscussionView.vue',
      component: CreateDiscussionView,
    },
    {
      path: '/talkai',
      name: 'TalkAiView',
      component: TalkAiView,
    },

    {
      path: '/',
      name: 'GuidepageView',
      component: GuidepageView,
    },
  ],

  // 스크롤 동작 설정
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition; // 브라우저 뒤로가기/앞으로가기를 클릭했을 때 이전 위치로 이동
    } else {
      return { top: 0 }; // 항상 맨 위로 이동
    }
  },
});

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

export default router;
