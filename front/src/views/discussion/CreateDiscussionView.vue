<template>
    <div>
        <DecoBox />
      <div class="mx-4">
        <div class="container mt-5 pt-5">
          <!-- Movie Title and Poster -->
          <div class="row pb-5">
            <div class="col-md-3">
              <img :src="movie.poster" alt="Movie Poster" class="img-fluid rounded shadow" />
            </div>
            <div class="col-md-9">
              <div class="d-flex justify-content-between align-items-start">
                <div>
                  <h1 class="fw-bold">{{ movie.title }}</h1>
                  <p class="text-muted">{{ movie.year }} • {{ movie.rating }} • {{ movie.runtime }}</p>
                </div>
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
                <h6 class="mb-3" style="color: #797979;">
                  <strong>Directors:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.directors.join(" • ") }}</span>
                </h6>
                <h6 class="mb-3" style="color: #797979;">
                  <strong>Writers:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.writers.join(" • ") }}</span>
                </h6>
                <h6 class="mb-3" style="color: #797979;">
                  <strong>Stars:</strong> &nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.stars.join(" • ") }}</span>
                </h6>
              </div>
              <!-- Tagline -->
              <div v-if="movie.tagline" class="tagline mt-4">
                  "{{ movie.tagline }}"
              </div>
            </div>
        </div>
  
          <!-- Review Form -->
          <div class="review-form text-center mt-5">
            <h4 class="fw-bold mb-2">My Rate</h4>
            <div class="mb-4">
              <span
                v-for="star in 5"
                :key="star"
                @click="setRating(star)"
                class="star"
                :class="{ active: star <= rating }"
              >
                ★
              </span>
            </div>
            <div class="mb-3">
              <input type="text" v-model="review.title" placeholder="Title" class="form-control" />
            </div>
            <div class="mb-3">
              <textarea v-model="review.detail" placeholder="Detail" class="form-control" rows="15"></textarea>
            </div>
            <div class="d-flex justify-content-end mt-5 pt-5">
              <button class="btn custom-button" @click="submitReview">Create</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
  import DecoBox from "@/components/DecoBox.vue";
  import { reactive, ref } from "vue";
  
  // Movie Data
  const movie = reactive({
    title: "Dune: Part Two",
    year: "2024",
    rating: "PG-13",
    runtime: "2h 45m",
    genres: ["Adventure", "Action", "Drama"],
    plot: "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family.",
    poster: "https://via.placeholder.com/300x450",
    directors: ["Denis Villeneuve"],
    writers: ["Frank Herbert", "Jon Spaihts", "Eric Roth"],
    stars: ["Timothée Chalamet", "Zendaya", "Rebecca Ferguson"],
    tagline: "Beyond Fear, Destiny Awaits", // 추가된 tagline 데이터
  });
  
  // User Review Data
  const review = reactive({
    title: "",
    detail: "",
  });
  
  const rating = ref(0);
  
  // Set User Rating
  const setRating = (value) => {
    rating.value = value;
  };
  
  // Submit Review
  const submitReview = () => {
    if (!review.title || !review.detail || rating.value === 0) {
      alert("Please fill in all fields and provide a rating.");
      return;
    }
    // Add submission logic here
    alert("Review submitted successfully!");
  };
</script>
  
<style scoped>
.tagline {
  font-size: 1.5rem;
  font-style: italic;
  color: #4a4a4a;
  border-left: 5px solid #254E01;
  padding-left: 15px;
  margin-top: 20px;
}

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
  
  /* Star Rating */
  .star {
    font-size: 3rem;
    color: #ddd;
    cursor: pointer;
    transition: color 0.3s ease;
  }
  
  .star.active {
    color: #ffd700;
  }
  
  .star:hover {
    color: #ffb700;
  }
  
  /* Form Styling */
  .form-control {
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
  }
  
  .review-form button {
    width: 120px;
    font-size: 1rem;
  }
</style>
  