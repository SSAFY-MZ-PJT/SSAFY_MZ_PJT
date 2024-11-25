// stores/auth.js

import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import api from '@/api';

export const useAuthStore = defineStore('auth', () => {
  // state
  const isLoading = ref(false)
  const error = ref(null)
  const isAuthenticated = ref(false); // 반드시 ref로 선언
  const token = ref(localStorage.getItem('accessToken'));
  const user = ref(null);
  // const userId = ref(localStorage.getItem('userId')); // 로그인 후 저장된 userId


  // 회원가입
  async function registerUser(payload) {
    isLoading.value = true
    error.value = null

    try {
      const response = await axios.post("http://localhost:8000/accounts/signup/", payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })

      if (response.status === 201) {
        alert("회원가입이 완료되었습니다! 이메일을 확인해주세요.")
        return true
      }
    } catch (err) {
      if (err.response) {
        error.value = err.response.data
        let errorMessage = '회원가입 실패: '

        if (typeof err.response.data === 'object') {
          // 객체인 경우 각 필드의 에러 메시지를 추출
          const errorMessages = Object.entries(err.response.data)
            .map(([field, message]) => `${field}: ${message}`)
            .join('\n')
          errorMessage += errorMessages
        } else {
          errorMessage += err.response.data
        }

        alert(errorMessage)
      } else {
        console.error("Error:", err)
        error.value = "알 수 없는 오류가 발생했습니다."
        alert(error.value)
      }
      return false
    } finally {
      isLoading.value = false
    }
  }

  //로그인
  const logIn = async function(payload) {
    try {
      const response = await axios.post(
        'http://localhost:8000/accounts/login/',
        {
          email: payload.email,  // 서버에서 기대하는 키 이름 확인
          password: payload.password,
        },
        {
          headers: {
            'Content-Type': 'application/json',  // JSON 형식으로 명시
          },
        }
      );
      console.log('로그인 완료', response.data);
      const token = response.data.key; // `key`가 토큰 값인 것으로 확인
      // const userId = response.data.userId; // 로그인한 사용자의 ID
      
      // 로그인 성공 시 처리
      localStorage.setItem('accessToken', token); // `key`로 저장
      // localStorage.setItem('userId', userId);

      // Axios 기본 헤더에 토큰 추가
      axios.defaults.headers.common['Authorization'] = `Token ${token}`;

      console.log('토큰 저장 완료:', localStorage.getItem('accessToken'));
      isAuthenticated.value = true; // 여기서 true로 설정

    } catch (error) {
      isAuthenticated.value =false; // 여기서 true로 설정
      console.error('로그인 실패:', error.response?.data || error.message);
      throw error;
    }
  }

  // 로그아웃
  const logout = () => {
    localStorage.removeItem('accessToken'); // 토큰 삭제
    delete axios.defaults.headers.common['Authorization']; // 헤더 초기화
    isAuthenticated.value = false; // 상태 초기화
    user.value = null; // 유저 정보 초기화
  };
  

  // 인증자 확인
  // 상태 복원 (앱 초기화 시 호출)
  const restoreAuthState = async () => {
    const savedToken = localStorage.getItem("accessToken");
    if (savedToken) {
      token.value = savedToken;
      axios.defaults.headers.common["Authorization"] = `Token ${savedToken}`;
      try {
        const response = await axios.get("http://localhost:8000/accounts/me/");
        user.value = response.data;
        isAuthenticated.value = true; // 유효한 사용자일 경우 인증됨
      } catch (error) {
        console.error("Error verifying token:", error);
        isAuthenticated.value = false; // 토큰이 유효하지 않음
        logout(); // 로그아웃 처리
      }
    } else {
      isAuthenticated.value = false;
    }
  };

  // // // 프로필 정보 가져오기
  // const fetchUserProfile = async () => {
  //   try {
  //     const userId = localStorage.getItem('userId'); // 저장된 userId 가져오기
  //     const response = await axios.get(`http://localhost:8000/accounts/${userId}/`);
  //     return response.data; // 사용자 프로필 데이터 반환
  //   } catch (error) {
  //     console.error("사용자 프로필 가져오기 실패:", error);
  //     throw error;
  //   }
  // };
  
  // expose managed state as return value
  return {
    isLoading,
    error,
    registerUser,
    logIn,
    logout,
    isAuthenticated,
    restoreAuthState,
  }
},{persist:true})