// stores/auth.js
import {ref} from "vue";
import {defineStore} from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", () => {
  // gpt왈
  const isAuthenticated = ref(false);
  const user = ref(null);
  const token = ref(null);
  // state
  const isLoading = ref(false);
  const error = ref(null);

  // Axios 기본 헤더 설정
  if (token.value) {
    axios.defaults.headers.common["Authorization"] = `Token ${token.value}`;
  }

  // 로그인
  async function login(email, password) {
    try {
      const API_URL = "http://localhost:8000/accounts/login/";

      const response = await axios({
        method: "post",
        url: API_URL,
        data: {
          email: email,
          password: password
        }
      });

      console.log("로그인 완료:", response.data);

      // 로그인 성공 시 토큰 저장
      token.value = response.data.token; // 서버에서 반환된 토큰
      localStorage.setItem("accessToken", token.value);

      // Axios 기본 헤더에 추가
      axios.defaults.headers.common["Authorization"] = `Token ${token.value}`;

      isAuthenticated.value = true;

      // 유저 정보 가져오기
      await fetchUser();
    } catch (error) {
      console.error("로그인 실패:", error);

      // 인증 실패 시 초기화
      isAuthenticated.value = false;
      token.value = null;
      localStorage.removeItem("accessToken");
      throw error;
    }
  }

  // 로그아웃
  function logout() {
    token.value = null;
    isAuthenticated.value = false;
    user.value = null;
    localStorage.removeItem("accessToken");
    delete axios.defaults.headers.common["Authorization"]; // Axios 헤더 초기화
  }

  // 유저 정보 가져오기
  async function fetchUser() {
    try {
      const response = await axios.get("http://localhost:8000/accounts/user/");
      user.value = response.data;
    } catch (err) {
      console.error("유저 정보 가져오기 실패:", err);
      isAuthenticated.value = false;
    }
  }

  // actions
  async function registerUser(payload) {
    isLoading.value = true;
    error.value = null;

    try {
      const response = await axios.post("http://localhost:8000/accounts/signup/", payload, {
        headers: {
          "Content-Type": "application/json"
        }
      });

      if (response.status === 201) {
        alert("회원가입이 완료되었습니다! 이메일을 확인해주세요.");
        return true;
      }
    } catch (err) {
      if (err.response) {
        error.value = err.response.data;
        let errorMessage = "회원가입 실패: ";

        if (typeof err.response.data === "object") {
          // 객체인 경우 각 필드의 에러 메시지를 추출
          const errorMessages = Object.entries(err.response.data).map(([field, message]) => `${field}: ${message}`).join("\n");
          errorMessage += errorMessages;
        } else {
          errorMessage += err.response.data;
        }

        alert(errorMessage);
      } else {
        console.error("Error:", err);
        error.value = "알 수 없는 오류가 발생했습니다.";
        alert(error.value);
      }
      return false;
    } finally {
      isLoading.value = false;
    }
  }

  // expose managed state as return value
  return {
    isLoading,
    error,
    registerUser,
    isAuthenticated,
    user,
    login,
    logout,
    fetchUser
  };
});
