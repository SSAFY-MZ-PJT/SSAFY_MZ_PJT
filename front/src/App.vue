<template>
  <div id="app">
    <Navbar />
    <main>
      <RouterView />
    </main>
    <p class="mt-5"></p>
    <Footer />
  </div>
</template>

<script setup>
import Footer from '@/components/Footer.vue';
import Navbar from '@/components/Navbar.vue';
import Search from '@/components/Search.vue';
</script>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 전체 화면 높이를 채움 */
}

footer {
  margin-top: auto; /* 푸터가 항상 페이지의 하단에 배치되도록 설정 */
}

</style>
