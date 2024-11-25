<template>
    <footer class="footer bg-white text-dark p-5">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-md-8 row align-items-center">
              <div class="text-md-start text-center">
                <ul class="list-inline mb-0">
                  <li class="col-md-4 list-inline-item mb-3">
                    <a href="#" class="text-dark text-decoration-none">이달의 영화 추천</a>
                  </li>
                  <li class="col-md-4 list-inline-item mb-3">
                    <router-link :to="{name:'GuidepageView'}" class="text-dark text-decoration-none">
                      Help
                    </router-link>  
                  </li>
                  <li class="col-md-4 list-inline-item mb-3">
                    <a href="#" class="text-dark text-decoration-none">유저들의 영화 추천</a>
                  </li>
                  <li class="col-md-4 list-inline-item mb-3">
                    <a href="https://github.com/SSAFY-MZ-PJT/SSAFY_MZ_PJT" class="text-dark text-decoration-none">GitHub</a>
                  </li>
                  <li class="col-md-4 list-inline-item mb-3">
                    <router-link :to="{name:'BoardView'}" class="text-dark text-decoration-none">
                      게시판
                    </router-link>
                  </li>
                </ul>
              </div>
            </div>
          <div class="col-md-4 text-md-end text-center">
            <div class="social-icons mb-3">
              <a href="https://www.netflix.com/kr/" target="netflix" class="me-3">
                <img src="@/assets/Footericons/netflix.png" alt="netflix" width="24" height="24">
              </a>
              <a href="https://www.disneyplus.com/ko-kr" target="disneyplus" class="me-3">
                <img src="@/assets/Footericons/disney-plus.png" alt="disneyplus" width="30" height="30">
              </a>
              <a href="https://www.youtube.com/" target="youtube" class="me-3">
                <img src="@/assets/Footericons/youtube.png" alt="youtube" width="30" height="30">
              </a>
            </div>
            <p class="mb-0">&copy; 2024 YourCompany. All Rights Reserved.</p>
          </div>
        </div>
      </div>
    </footer>
  </template>
  
  <script setup>

import { RouterLink } from 'vue-router';

  </script>
  
<style >
.footer {
    position: relative;
    bottom: 0;
    width: 100%;
    background-color: #ffffff; /* 흰색 배경 */
    color: #212529; /* 어두운 텍스트 */
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1); /* 얇은 그림자 */
  }
  
  .footer p {
    font-size: 0.9rem;
    margin: 0;
  }
  
  .footer a {
    color: #212529; /* 기본 링크 색상 */
    transition: color 0.3s;
  }
  
  .footer a:hover {
    color: #084e0d; /* 링크 호버 시 파란색 강조 */
  }
.list-inline-item {
    margin-bottom: 1rem; /* 하단 공간 추가 */
  }

.social-icons a {
    display: inline-block;
    margin-right: 10px; /* 아이콘 간의 간격 */
}

.social-icons img {
    transition: transform 0.3s ease;
}

.social-icons img:hover {
    transform: scale(1.2); /* 호버 시 확대 효과 */
}

</style>
  