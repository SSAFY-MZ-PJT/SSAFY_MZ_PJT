import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore("auth", {
  state: () => ({
    isLoading: false, // 요청 상태
    error: null, // 에러 메시지
  }),
  actions: {
    async registerUser(payload) {
      this.isLoading = true;
      this.error = null;

      try {
        const response = await axios.post("http://localhost:8000/accounts/signup/", payload);
        if (response.status === 201) {
          alert("회원가입이 완료되었습니다! 로그인 페이지로 이동합니다.");
          return true; // 성공
        }
      } catch (error) {
        if (error.response) {
          this.error = error.response.data;
          alert(`회원가입 실패: ${JSON.stringify(this.error)}`);
        } else {
          console.error("Error:", error);
          this.error = "알 수 없는 오류가 발생했습니다.";
          alert(this.error);
        }
        return false; // 실패
      } finally {
        this.isLoading = false;
      }
    },
  },
});