<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink :to="{ name: 'home' }">Home</RouterLink>
        <span v-if="!isLogin"> | </span>
        <RouterLink v-if="!isLogin" :to="{ name: 'SignUpView' }">SignUp</RouterLink>
        <span v-if="!isLogin"> | </span>
        <RouterLink v-if="!isLogin" :to="{ name: 'LogInView' }">LogIn</RouterLink>
      </nav>
    </div>
  </header>
  
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

import { useArticleStore } from './stores/articles';

const store = useArticleStore()
const isLogin = store.isLogin
</script>
        
<style scoped>
</style>
