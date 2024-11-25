<template>
  <div class="card h-100">
    <div class="position-relative">
      <!-- Movie Poster -->
      <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }" class="card-link">
      <img
      :src="movie.poster_image_url"
      class="card-img-top poster-image"
      :alt="movie.title"
      />
      </router-link>
      <!-- Favorite Button -->
      <button
      class="bookmark-btn position-absolute top-0 end-0 btn btn-sm m-1"
      @click="toggleFavorite(movie.id)"
          :class="{ 'active': movie.isFavorite }"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            fill="currentColor"
            class="bi bi-bookmark"
            viewBox="0 0 16 16"
          >
            <path
              d="M2 2v13.5l6-3.5 6 3.5V2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1z"
              :fill="movie.isFavorite ? '#002C0C' : 'currentColor'"
            />
          </svg>
        </button>
      </div>
      <div class="card-body">
        <h6 class="card-title text-truncate fw-bold">
          {{ movie.title }}
        </h6>
        <p class="text-muted mb-1">
          📅 {{ movie.release_date }} &nbsp;&nbsp;
          <span class="text-warning fw-bold">★ {{ movie.rating.toFixed(1) }}</span>
        </p>
        <div class="d-flex align-items-center justify-content-between">
          <!-- Trailer Button -->
          <button class="btn custom-button btn-sm" @click.stop="playTrailer(movie.trailer_url)">
            ▶ Trailer
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    movie: {
      type: Object,
      required: true,
    },
  });
  
  const toggleFavorite = (id) => {
    console.log(`Toggle favorite for movie with id: ${id}`);
  };
  
  const playTrailer = (url) => {
    window.open(url, "_blank");
  };
  </script>
  
  <style scoped>
  .card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    overflow: hidden;
    background-color: #ffffff;
    height: 100%;
    transition: transform 0.3s ease;
  }
  
  .card:hover {
    transform: scale(1.05);
    z-index: 2;
  }
  
  .card-img-top {
    object-fit: cover;
    height: 250px;
  }
  
  .poster-image {
    width: 100%;
    height: 375px;
    object-fit: cover;
  }
  
  .bookmark-btn {
    background-color: rgba(0, 0, 0, 0.3);
    border: none;
    border-radius: 50%;
    padding: 0.5rem;
    color: white;
    transition: all 0.3s ease;
  }
  
  .bookmark-btn:hover {
    background-color: rgba(0, 0, 0, 0.6);
  }
  
  .bookmark-btn.active {
    background-color: rgba(255, 255, 255, 0.8);
  }
  
  .custom-button {
    width: 100%;
    background-color: #f3f3f3;
    color: #686868 !important;
    border: 1px solid #f3f3f3 !important;
    transition: all 0.3s ease;
  }
  
  .custom-button:hover:not(:disabled) {
    background-color: #c4302b !important;
    color: #ffffff !important;
    border-color: #c4302b !important;
  }
  .card-link {
  text-decoration: none; /* 밑줄 제거 */
  }

  .card-link:hover {
    text-decoration: none; /* 호버 상태에서도 밑줄 제거 */
  }
</style>
  