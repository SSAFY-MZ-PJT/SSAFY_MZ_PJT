// stores/movie.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useMovieStore = defineStore('movie', {
  state: () => ({
    nowPlaying: [],
    popular: [],
    recommended: [],
    currentMovies: [], // 카테고리별 영화 데이터
    movieDetails: null,
    similarMovies: [], // 유사한 영화 데이터
    isLoading: false,
    error: null,
  }),

  actions: {
    // 좋아요 토글 액션
    async toggleFavorite(movieId) {
      try {
        const response = await axios.post(`http://localhost:8000/movies/like/${movieId}/`);
        const liked = response.data.liked;

        // 좋아요 상태 업데이트
        const updateFavoriteState = (movies) => {
          const movie = movies.find((movie) => movie.id === movieId);
          if (movie) {
            movie.isFavorite = liked;
          }
        };

        updateFavoriteState(this.nowPlaying);
        updateFavoriteState(this.popular);
        updateFavoriteState(this.recommended);

        if (this.movieDetails && this.movieDetails.id === movieId) {
          this.movieDetails.isFavorite = liked;
        }

        console.log(`Favorite toggled for movie ${movieId}:`, liked);
      } catch (error) {
        console.error('Failed to toggle favorite:', error.response?.data || error.message);
      }
    },
    
    // 메인 페이지 영화 데이터 가져오기
    async fetchMainPageMovies() {
      this.isLoading = true;
      this.error = null;

      try {
        const response = await axios.get('http://localhost:8000/movies/');
        const data = response.data;

        console.log('API 응답 데이터:', data); // API 응답 데이터 로그 확인
        this.nowPlaying = data.now_playing || []; // 현재 상영 중인 영화
        this.popular = data.popular || []; // 인기 영화
        this.recommended = data.recommended || []; // 추천 영화
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
          url = 'http://localhost:8000/movies/recommended/';
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

    // 장르가 비슷한 영화 데이터 가져오기
    async fetchSimilarMovies(genres) {
      this.isLoading = true;
      this.error = null;

      try {
        const response = await axios.get('http://localhost:8000/movies/all/');
        const allMovies = response.data;

        // 장르가 겹치는 정도에 따라 영화 정렬
        const similarMovies = allMovies
          .map(movie => ({
            ...movie,
            genreMatches: movie.genres.filter(genre => genres.includes(genre.name)).length,
          }))
          .sort((a, b) => b.genreMatches - a.genreMatches)
          .slice(0, 12); // 최대 12개

        this.similarMovies = similarMovies;
      } catch (err) {
        this.error = err.response?.data || 'Failed to fetch similar movies';
        console.error('Error fetching similar movies:', this.error);
      } finally {
        this.isLoading = false;
      }
    },

    // 영화 상세 정보 가져오기
    async fetchMovieDetails(movieId) {
      this.isLoading = true;
      this.error = null;

      try {
        const response = await axios.get(`http://localhost:8000/movies/${movieId}/`);
        console.log("영화 상세 데이터:", response.data);
        this.movieDetails = response.data;
      } catch (err) {
        this.error = err.response?.data || 'Failed to fetch movie details';
        console.error('Error fetching movie details:', this.error);
      } finally {
        this.isLoading = false;
      }
    },
  },

  // 상태를 로컬 스토리지에 저장하도록 설정
  persist: {
    key: 'movieStore', // 로컬 스토리지 키
    storage: window.localStorage, // 상태를 로컬 스토리지에 저장
    paths: ['nowPlaying', 'popular', 'recommended', 'movieDetails'], // 저장할 상태 지정
  },
},{persist:true});
