// stores/review.js
import { defineStore } from "pinia";
import axios from "axios";

export const useReviewStore = defineStore("review", {
  state: () => ({
    baseUrl: "http://localhost:8000/",
    currentUser: null, // 현재 로그인한 사용자 정보
  }),
  actions: {
    setCurrentUser(user) {
      this.currentUser = user;
    },

    async fetchMoviesWithReviews() {
      try {
        const moviesResponse = await axios.get(`${this.baseUrl}movies/all/`);
        const movies = moviesResponse.data;
    
        const moviesWithReviews = await Promise.all(
          movies.map(async (movie) => {
            try {
              const reviewsResponse = await axios.get(`${this.baseUrl}reviews/${movie.id}/`);
              const reviews = reviewsResponse.data;
              return { ...movie, reviews };
            } catch (err) {
              console.error(`Failed to fetch reviews for movie ${movie.id}:`, err);
              return { ...movie, reviews: [] }; // 리뷰가 없으면 빈 배열로 반환
            }
          })
        );
    
        console.log("Movies with Reviews:", moviesWithReviews); // 디버깅용
        return moviesWithReviews;
      } catch (err) {
        console.error("Failed to fetch movies:", err);
        throw err;
      }
    },

    async toggleLike(reviewId) {
      await axios.post(`${this.baseUrl}reviews/like/${reviewId}/`);
    },

    async fetchMovieDetails(movieId) {
      const movieResponse = await axios.get(`${this.baseUrl}movies/${movieId}/`);
      const reviewsResponse = await axios.get(`${this.baseUrl}reviews/${movieId}/`);
      return {
        movie: movieResponse.data,
        reviews: reviewsResponse.data,
      };
    },

    async submitReview(reviewData) {
      try {
        const response = await axios.post(`${this.baseUrl}reviews/${reviewData.movieId}/`, {
          title: reviewData.title.trim(),
          content: reviewData.content.trim(),
          rating: reviewData.rating,
          user: this.currentUser.id, // currentUser에서 user id 가져오기
        });

        return response.data;
      } catch (error) {
        console.error("Error submitting review:", error.response?.data || error.message);
        throw error;
      }
    },
  },
},{persist:true});
