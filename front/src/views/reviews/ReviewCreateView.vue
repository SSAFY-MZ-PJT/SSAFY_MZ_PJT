<!-- ReviewCreateView -->
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
              :class="{ active: star <= stars }"
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
import { reactive, ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useReviewStore } from "@/stores/review";

// Router and Store
const route = useRoute();
const router = useRouter();
const reviewStore = useReviewStore();
const stars = ref(0); // 별점 상태

// Movie Data
const movie = reactive({
  title: "",
  year: "",
  rating: "",
  runtime: "",
  genres: [],
  plot: "",
  poster: "",
  stars: [],
  tagline: "",
});

// User Review Data
const review = reactive({
  title: "",
  detail: "",
  rating: 0, // 별점 값 (0 ~ 10)
});

// 사용자 로그인 정보 설정 (예: 로그인한 사용자의 ID를 설정)
onMounted(() => {
  const currentUser = {
    id: 1, // 사용자 ID
    username: "testuser", // 사용자 이름
  };
  reviewStore.setCurrentUser(currentUser); // Pinia 스토어에 사용자 정보 설정
});

// Set User Rating
const setRating = (star) => {
  stars.value = star; // 별 상태 업데이트
  review.rating = star * 2; // 별점 계산 (1 ~ 5 -> 2 ~ 10)
};

// Load Movie Data
const loadMovieData = async () => {
  const movieId = route.params.id;

  try {
    const { movie: fetchedMovie } = await reviewStore.fetchMovieDetails(movieId);

    Object.assign(movie, {
      title: fetchedMovie.title || "Unknown Title",
      year: fetchedMovie.release_date || "N/A",
      rating: fetchedMovie.rating || "N/A",
      runtime: fetchedMovie.runtime || "N/A",
      genres: fetchedMovie.genres?.map((g) => g.name) || [],
      plot: fetchedMovie.plot || "Plot not available",
      poster: fetchedMovie.poster_image_url || "https://via.placeholder.com/300x450",
      stars: (fetchedMovie.actors || []).map((a) => a.name),
      tagline: fetchedMovie.tagline || "",
    });
  } catch (error) {
    console.error("Failed to load movie data:", error);
    alert("Failed to load movie data.");
  }
};

// Submit Review
const submitReview = async () => {
  if (!review.title || !review.detail || stars.value === 0) {
    alert("Please fill in all fields and provide a rating.");
    return;
  }

  const movieId = route.params.id;

  try {
    await reviewStore.submitReview({
      movieId,
      title: review.title,
      content: review.detail,
      rating: review.rating,
    });

    alert("Review created successfully!");
    router.push({ name: "BoardDetailView", params: { movieId } }); // 라우팅은 여기에서 처리
  } catch (error) {
    console.error("Failed to create review:", error);
    alert("Failed to submit review.");
  }
};

onMounted(loadMovieData);
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
  