// src/api/index.js

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Django API 서버 URL
  headers: {
    'Content-Type': 'application/json',
  },
});

// 인증 토큰 자동 추가
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('accessToken');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

export default api;
