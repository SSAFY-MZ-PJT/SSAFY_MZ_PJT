<template>
  <div>
    <Search />
    <!-- Movie Recommendations Section -->
    <div class="container mt-5">
      <!-- Section Title -->
      <h2 class="text-center fw-bold mb-4">Movie Recommendations</h2>

      <!-- Monthly Recommendation -->
      <div class="d-flex justify-content-between align-items-center">
        <a href="/movies" class="text-decoration-none text-dark d-flex align-items-center">
          <h4 class="text-start fw-bold mb-0 mx-4">• 이달의 추천 영화 →</h4>
        </a>
      </div>
      <p class="text-muted mb-5 mx-5">Movies just for you</p>

      <!-- Movie Cards Grid -->
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-4 col-sm-6 mb-4" v-for="movie in movies" :key="movie.id">
            <!-- Card -->
          <div class="card h-100">
            <div class="position-relative">
              <!-- Movie Poster -->
              <img
                :src="movie.image"
                class="card-img-top poster-image"
                :alt="movie.title"
                style="height: 250px; object-fit: cover;"
              />
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

            <!-- Card Body -->
            <div class="card-body">
              <h6 class="card-title text-truncate fw-bold">
                {{ movie.title }}
              </h6>
              <p class="text-muted mb-1">
                📅 {{ movie.date }} &nbsp;&nbsp;
                <span class="text-warning fw-bold">★ {{ movie.rating }}</span>
              </p>
              <div class="d-flex align-items-center justify-content-between">
                <!-- Trailer Button -->
                <button
                  class="btn custom-button btn-sm"
                  @click="playTrailer(movie.trailerUrl)"
                >
                  ▶ Trailer
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { reactive } from "vue";

// Movie Data
const movies = reactive([
  {
    id: 1,
    title: "Spider-Man: Across the Spider-Verse",
    rating: 8.6,
    image: "https://via.placeholder.com/300x400",
    trailerUrl: "https://youtube.com/trailer1",
    date: "March 29",
    isFavorite: false,
  },
  {
    id: 2,
    title: "Interstellar",
    rating: 8.7,
    image: "https://via.placeholder.com/300x400",
    trailerUrl: "https://youtube.com/trailer2",
    date: "March 29",
    isFavorite: false,
  },
  {
    id: 3,
    title: "Arrival",
    rating: 7.9,
    image: "https://via.placeholder.com/300x400",
    trailerUrl: "https://youtube.com/trailer3",
    date: "March 29",
    isFavorite: false,
  },
  {
    id: 4,
    title: "Inception",
    rating: 8.8,
    image: "../src/assets/Movieicons/더미.webp",
    trailerUrl: "https://youtube.com/trailer4",
    date: "March 29",
    isFavorite: false,
  },
]);

// Toggle Favorite
const toggleFavorite = (id) => {
  const movie = movies.find((movie) => movie.id === id);
  if (movie) {
    movie.isFavorite = !movie.isFavorite;
  }
};

// Play Trailer
const playTrailer = (url) => {
  window.open(url, "_blank");
};
</script>

<style scoped>
.container {
  max-width: 1200px;
}

/* 카드 디자인 */
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
  background-color: #ffffff;
  height: 100%; /* Ensure card height is consistent */
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
  height: 375px; /* Adjust for 2:3 aspect ratio */
  object-fit: cover;
}

/* Favorite Button */
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

/* Trailer Button */
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
</style>
