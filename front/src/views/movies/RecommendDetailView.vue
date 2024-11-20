<template>
  <div>
    <Search />
    <!-- Section Title -->
    <div class="container mt-5">
      <h2 class="text-center fw-bold mb-4">Recommended Movie of the Month</h2>
      <p class="text-muted text-center">TV shows and movies just for you</p>
    </div>

    <!-- Movie Cards Grid -->
    <div class="container">
      <div class="row m-5">
        <div
          class="col-lg-3 col-md-4 col-sm-6 mb-4"
          v-for="movie in movies"
          :key="movie.id"
        >
          <!-- Card -->
          <div class="card h-100">
            <div class="position-relative">
              <!-- Movie Poster -->
              <img
                :src="movie.image"
                class="card-img-top poster-image"
                :alt="movie.title"
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

    <!-- 페이지 이동 바 -->
    <nav aria-label="Page navigation">
      <ul class="pagination justify-content-center">
        <!-- 이전 페이지 버튼 -->
        <li class="page-item disabled">
          <a class="page-link" href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <!-- 페이지 번호 -->
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item"><a class="page-link" href="#">2</a></li>
        <li class="page-item" aria-current="page">
          <a class="page-link" href="#">3</a>
        </li>
        <li class="page-item"><a class="page-link" href="#">4</a></li>
        <li class="page-item"><a class="page-link" href="#">5</a></li>
        <!-- 다음 페이지 버튼 -->
        <li class="page-item">
          <a class="page-link" href="#" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
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
    image: "https://via.placeholder.com/300x400",
    trailerUrl: "https://youtube.com/trailer4",
    date: "March 29",
    isFavorite: false,
  },
  {
    id: 5,
    title: "The Last of Us",
    rating: 9.0,
    image: "../src/assets/Movieicons/더미.webp",
    trailerUrl: "https://youtube.com/trailer5",
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
/* Bookmark Button */
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

.poster-image {
  width: 100%;
  height: 375px; /* Adjust for 2:3 aspect ratio */
  object-fit: cover;
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
