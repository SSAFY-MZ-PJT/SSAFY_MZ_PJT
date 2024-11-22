// stores/auth.js
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', () => {
  // state
  const isLoading = ref(false)
  const error = ref(null)
  const isAuthenticated = ref(false); // 반드시 ref로 선언
  const token = ref(localStorage.getItem('accessToken'));
  const user = ref(null);

  // 회원가입s
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
  
      // 로그인 성공 시 처리
      localStorage.setItem('accessToken', token); // `key`로 저장
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
  const restoreAuthState = () => {
    const savedToken = localStorage.getItem('accessToken');
    if (savedToken) {
      token.value = savedToken;
      axios.defaults.headers.common['Authorization'] = `Token ${savedToken}`;
      isAuthenticated.value = true; // 반응형 상태 업데이트
    } else {
      token.value = null;
      isAuthenticated.value = false;
    }
  };

  // // fetchUser 함수 단순화
  // const fetchUser = async () => {
  //   try {
  //     if (!token.value) {
  //       throw new Error('토큰이 없습니다. 로그인 상태를 확인하세요.');
  //     }

  //     const response = await axios.get('http://localhost:8000/accounts/user/', {
  //       headers: {
  //         Authorization: `Token ${token.value}`,
  //       },
  //     });

  //     user.value = response.data; // 사용자 정보 저장
  //     isAuthenticated.value = true;
  //     console.log('사용자 정보 가져오기 성공:', response.data);
  //   } catch (err) {
  //     console.error('사용자 정보 가져오기 실패:', err.response?.data || err.message);
  //     user.value = null;
  //     isAuthenticated.value = false;
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
    // fetchUser
  }
},{persist:true})