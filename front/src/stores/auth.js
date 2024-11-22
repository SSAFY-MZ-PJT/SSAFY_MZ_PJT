// stores/auth.js
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', () => {
  // state
  const isLoading = ref(false)
  const error = ref(null)

  // actions
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
  
      // 로그인 성공 시 처리
      // 예: 토큰 저장, 상태 업데이트
      localStorage.setItem('accessToken', response.data.token);
    } catch (error) {
      console.error('로그인 실패:', error.response?.data || error.message);
      throw error;
    }
  }
  

  // expose managed state as return value
  return {
    isLoading,
    error,
    registerUser,
    logIn
  }
},{persist:true})