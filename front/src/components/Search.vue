<template>
     <div class="search-bar-container">
          <div class="container">
            <p class="text-center">Welcome to Cinerium</p>
            <p class="text-center pb-3">Recommendations</p>
            <div class="input-group">
              <input 
                type="text" 
                class="form-control" 
                placeholder="Find the best movies to watch..." 
                aria-label="Search"
                aria-describedby="search-button">
              <button 
                class="btn" 
                type="button" 
                id="search-button">
                Search
              </button>
            </div>
          </div>
        </div>
</template>

<script setup>

</script>

<style scoped>
/* 검색 바 컨테이너 */
.search-bar-container {
    background: linear-gradient(to bottom, #002C0C, #FFFFFF); /* 상단에서 하단으로 그라데이션 */
    padding: 70px 0; /* 상하 여백 */
    text-align: center; /* 텍스트 중앙 정렬 */
  }
  
  /* p 태그 스타일링 */
  .search-bar-container p {
    font-size: 2rem; /* 큰 글씨 크기 */
    color: #FFFFFF; /* 하얀색 글씨 */
    font-weight: bold; /* 글씨 굵게 */
    margin-bottom: 6px; /* 아래쪽 여백 */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
  }
  
  /* 입력 필드와 버튼 스타일 */
  .input-group {
    max-width: 600px; /* 검색바의 최대 너비 */
    margin: 0 auto; /* 중앙 정렬 */
    
  }
  
  .input-group .form-control {
    border-radius: 20px 0 0 20px; /* 왼쪽 둥근 모서리 */
    border: 1px solid #ccc; /* 기본 테두리 */
    padding: 10px 15px; /* 적절한 내부 여백 */
  }
  
  .input-group .btn {
    border-radius: 0 20px 20px 0; /* 오른쪽 둥근 모서리 */
    padding: 10px 20px; /* 버튼 크기 조정 */
    background-color: #254E01; /* 버튼 배경색 */
    color: #ffffff; /* 버튼 글자색 */
    font-weight: bold; /* 버튼 글씨 굵게 */
    transition: background-color 0.3s ease;
  }
  
  .input-group .btn:hover {
    background-color: #ffffff; /* 호버 시 버튼 색상 변경 */
    border-color: #254E01; /* 테두리 색상 변경 */
    color: #254E01; /* 버튼 글자색 */
  }

  .input-group .form-control:focus {
    outline: none; /* 포커스 테두리 제거 */
    box-shadow: none; /* 기본 그림자 제거 */
    border-color: #254E01; /* 테두리 색상 변경 */
}


</style>