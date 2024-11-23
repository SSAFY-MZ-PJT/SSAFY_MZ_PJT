// stores/movie.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useMovieStore = defineStore('movie', {
  state: () => ({
    nowPlaying: [],
    popular: [],
    recommended: [],
    currentMovies: [], // 상세 페이지에서 표시할 영화
    isLoading: false,
    error: null,
  }),

  actions: {
    // 메인 페이지 영화 데이터 가져오기
    async fetchMainPageMovies() {
      this.isLoading = true;
      this.error = null;

      try {
        const response = await axios.get('http://localhost:8000/movies/');
        const data = response.data;

        console.log('API 응답 데이터:', response.data); // API 응답 데이터 로그 확인
        this.nowPlaying = data.now_playing;
        this.popular = data.popular;
        this.recommended = data.recommended;
      } catch (err) {
        this.error = err.response?.data || 'Failed to fetch movies';
        console.error('Error fetching movies:', this.error);
      } finally {
        this.isLoading = false;
      }
    },

    // 카테고리별 영화 데이터 가져오기
    async fetchMoviesByCategory(category) {
      this.isLoading = true;
      this.error = null;

      try {
        let url = '';
        if (category === 'nowPlaying') {
          url = 'http://localhost:8000/movies/now_playing/';
        } else if (category === 'popular') {
          url = 'http://localhost:8000/movies/popular/';
        } else if (category === 'recommended') {
          url = 'http://localhost:8000/movies/all/';
        } else {
          throw new Error('Invalid category');
        }

        const response = await axios.get(url);
        this.currentMovies = response.data; // 영화 데이터를 상태에 저장
      } catch (err) {
        this.error = err.response?.data || 'Failed to fetch movies';
        console.error('Error fetching movies:', this.error);
      } finally {
        this.isLoading = false;
      }
    },
  },
});
