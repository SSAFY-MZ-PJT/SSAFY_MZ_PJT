<template>
  <div>
    <Search />
    <div class="container mt-5 pt-5">
      <!-- Movie Title and Poster -->
      <div class="row">
        <div class="col-md-3">
          <img :src="movie.poster" alt="Movie Poster" class="img-fluid rounded shadow" />
        </div>
        <div class="col-md-9">
          <div class="d-flex justify-content-between align-items-start">
            <div>
              <h1 class="fw-bold">{{ movie.title }}</h1>
              <p class="text-muted">{{ movie.year }} • {{ movie.rating }} • {{ movie.runtime }}</p>
            </div>
            <!-- Watchlist Button -->
            <button class="btn custom-button">
              <i class="bi bi-plus-lg"></i> Add to Watchlist
            </button>
          </div>

          <!-- Genres -->
          <div class="mb-3">
            <span v-for="genre in movie.genres" :key="genre" class="badge bg-secondary me-2">
              {{ genre }}
            </span>
          </div>

          <!-- Plot -->
          <p class="lead">{{ movie.plot }}</p>

          <!-- Crew -->
          <div class="mt-4">
            <h6 class="mb-3">
              <strong>Directors:</strong>&nbsp;&nbsp;<span>{{ movie.directors.join(" • ") }}</span>
            </h6>
            <h6 class="mb-3">
              <strong>Writers:</strong>&nbsp;&nbsp;<span>{{ movie.writers.join(" • ") }}</span>
            </h6>
            <h6 class="mb-3">
              <strong>Stars:</strong>&nbsp;&nbsp;<span>{{ movie.stars.join(" • ") }}</span>
            </h6>
          </div>

          <!-- Tagline -->
          <div v-if="movie.tagline" class="tagline mt-4">
            "{{ movie.tagline }}"
          </div>
        </div>
      </div>

      <!-- Cast Section -->
      <div class="mt-5">
        <h3 class="fw-bold pt-5">Cast</h3>
        <hr />
        <div class="d-flex flex-wrap gap-4">
          <div v-for="cast in movie.cast" :key="cast.name" class="text-center">
            <img :src="cast.image" alt="Cast Image" class="img-fluid shadow" width="100" />
            <p class="mt-2 mb-0 fw-bold" style="color: #002C0C;">{{ cast.name }}</p>
            <p class="text-muted small">{{ cast.role }}</p>
          </div>
        </div>
      </div>

      <!-- User Reviews Section -->
      <div class="mt-5">
        <div class="d-flex justify-content-between align-items-center pt-5">
          <!-- User Reviews Title and View All Button -->
          <div class="d-flex align-items-center">
            <h3 class="fw-bold me-3">User Reviews</h3>
            <!-- View All Reviews Button -->
            <button class="btn see-all">
              See all 1.4K
              <i class="bi bi-chevron-right"></i>
            </button>
          </div>
          <!-- Create Review Button -->
          <button class="btn custom-button">Create Review</button>
        </div>
        <hr />
        <div v-for="review in movie.reviews" :key="review.id" class="card mt-3 p-3">
          <div class="d-flex justify-content-between align-items-center">
            <h5 class="card-title mb-0 fw-bold">{{ review.title }}</h5>
            <div class="d-flex align-items-center">
              <!-- Like Button -->
              <i
                :class="review.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                @click="toggleLike(review.id)"
              ></i>
              <!-- Like Count -->
              <span class="like-count ms-2">
                • {{ review.likes }} likes
              </span>
            </div>
          </div>
          <p class="text-muted small mb-1">By {{ review.author }} • {{ review.date }}</p>
          <p class="card-text" style="color: #242424;">{{ review.text }}</p>
        </div>
      </div>


      <!-- Movie Details Section -->
      <div class="mt-5">
        <h3 class="fw-bold pt-5">Details</h3>
        <hr />
        <ul class="list-unstyled">
          <li><strong >Release Date:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.details.releaseDate }}</span></li>
          <hr />
          <li><strong>Country:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.details.countries.join(", ") }}</span></li>
          <hr />
          <li><strong>Language:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.details.languages.join(", ") }}</span></li>
          <hr />
          <li><strong>Production:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.details.production }}</span></li>
        </ul>
      </div>

      <!-- Technical Specs Section -->
      <div class="mt-5">
        <h3 class="fw-bold pt-5">Technical Specs</h3>
        <hr />
        <ul class="list-unstyled">
          <li><strong>Runtime:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.specs.runtime }}</span></li>
          <hr />
          <li><strong>Color:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.specs.color }}</span></li>
          <hr />
          <li><strong>Sound Mix:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.specs.soundMix }}</span></li>
        </ul>
      </div>
    </div>
    
  </div>
</template>


<script setup>
import Search from "@/components/Search.vue";
import { reactive } from "vue";

// 더미 데이터
const movie = reactive({
  title: "Dune: Part Two",
  year: "2024",
  rating: "PG-13",
  runtime: "2h 45m",
  genres: ["Adventure", "Action", "Drama"],
  plot: "A student becomes the ruler of a desert planet while seeking revenge against the enemies who destroyed his family.",
  poster: "https://via.placeholder.com/300x450",
  directors: ["Denis Villeneuve"],
  writers: ["Frank Herbert", "Jon Spaihts", "Eric Roth"],
  stars: ["Timothée Chalamet", "Zendaya", "Rebecca Ferguson"],
  tagline: "Beyond Fear, Destiny Awaits", // 추가된 tagline 데이터
  cast: [
    { name: "Timothée Chalamet", role: "Paul Atreides", image: "https://via.placeholder.com/100" },
    { name: "Zendaya", role: "Chani", image: "https://via.placeholder.com/100" },
    { name: "Rebecca Ferguson", role: "Jessica", image: "https://via.placeholder.com/100" },
    { name: "Javier Bardem", role: "Stilgar", image: "https://via.placeholder.com/100" },
  ],
  reviews: [
    {
      id: 1,
      title: "Amazing Sequel!",
      author: "John Doe",
      date: "March 30, 2024",
      text: "This movie is a masterpiece. The acting, the visuals, and the storyline were phenomenal!",
      likes: 256,
    },
    {
      id: 2,
      title: "A True Sci-Fi Epic",
      author: "Jane Smith",
      date: "April 1, 2024",
      text: "Dune: Part Two delivers an incredible continuation to the story. Truly a must-watch. Part Two delivers an incredible continuation to the story. Truly a must-watch. Part Two delivers an incredible continuation to the story. Truly a must-watch.",
      likes: 342,
    },
  ],
  details: {
    releaseDate: "March 29, 2024",
    countries: ["USA", "Canada", "UK"],
    languages: ["English"],
    production: "Legendary Entertainment",
  },
  specs: {
    runtime: "2h 45m",
    color: "Color",
    soundMix: "Dolby Atmos, DTS",
  },
});
const toggleLike = (id) => {
  const review = movie.reviews.find((r) => r.id === id);
  if (review) {
    review.liked = !review.liked; // 좋아요 상태 토글
    review.likes += review.liked ? 1 : -1; // 좋아요 수 조정
  }
};

</script>

<style scoped>
.container {
  max-width: 1200px;
}

.img-fluid {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
}

.badge {
  font-size: 0.9rem;
  padding: 0.5rem;
}

.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

.card-title {
  font-size: 1rem;
}

.card-text {
  font-size: 0.9rem;
}

.tagline {
  font-size: 1.5rem;
  font-style: italic;
  color: #4a4a4a;
  border-left: 5px solid #254E01;
  padding-left: 15px;
  margin-top: 20px;
}

/* 버튼들 */
button {
  transition: all 0.3s ease;
}

button:hover {
  transform: scale(1.05);
}

.custom-button {
  background-color: #ffffff;
  color: #254E01 !important;
  border: 1px solid #254E01 !important;
  transition: all 0.3s ease;
}

.custom-button:hover:not(:disabled) {
  background-color: #254E01 !important;
  color: #ffffff !important;
  border-color: #254E01 !important;
}

.custom-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Like Icon 스타일 */
.like-icon {
  font-size: 1.5rem; /* 아이콘 크기 */
  color: #797979; /* 기본 색상 */
  cursor: pointer; /* 클릭 가능 표시 */
  transition: color 0.3s ease; /* 색상 전환 효과 */
}

.like-icon:hover {
  color: #545454; /* 호버 시 색상 */
}

.like-count {
  font-size: 1rem; /* 좋아요 수 글꼴 크기 */
  color: #545454; /* 좋아요 수 색상 */
}

/* View All Reviews 버튼 스타일 */
.see-all {
  display: inline-flex;
  align-items: center;
  background-color: #f5f5f5;
  color: #575757;
  border: 1px solid #ddd;
  border: noneh;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.see-all:hover {
  background-color: #dddddd;
  color: #242424;
  text-decoration: none;
}

.see-all i {
  margin-left: 0.5rem; /* 아이콘과 텍스트 사이 간격 */
  font-size: 1.2rem;
}

/* Like Count 스타일 */
.like-count {
  font-size: 0.9rem;
  color: #797979;
}


h6 {
  margin-bottom: 1rem;
}

.space {
  margin-top: 5rem;
}

hr {
  border: none;
  border-top: 2px solid #ddd;
  margin: 2rem 0;
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
</style>
