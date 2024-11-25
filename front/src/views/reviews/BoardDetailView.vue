<template>
    <div>
        <Search />
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
              </div>
            </div>
      
            <!-- Highlighted Reviews -->
            <div class="mt-5">
              <h4 class="fw-bold mb-4">Highlighted Reviews</h4>
              <div class="row">
                <!-- Best Review -->
                <div class="col-md-6" v-if="bestReview">
                  <div class="review-card p-3 mb-4"
                  :style="{ backgroundColor: getReviewBgColor(bestReview.rating) }">
                    <div class="d-flex align-items-center mb-2">
                      <span class="rating-badge">
                        <span>★</span> {{ bestReview.rating }}/10
                      </span>
                      <h5 class="mb-0 ms-3">{{ bestReview.title }}</h5>
                    </div>
                    <p class="text-muted mb-1">Date: {{ bestReview.date }}</p>
                    <p>{{ bestReview.text }}</p>
                    <div class="d-flex align-items-center">
                      <i
                        :class="bestReview.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                        @click="toggleLike(bestReview.id)"
                      ></i>
                      <span class="like-count ms-2">• {{ bestReview.likes }} likes</span>
                    </div>
                  </div>
                </div>
      
                <!-- Worst Review -->
                <div class="col-md-6" v-if="worstReview">
                  <div class="review-card p-3 mb-4"
                  :style="{ backgroundColor: getReviewBgColor(worstReview.rating) }">
                    <div class="d-flex align-items-center mb-2">
                      <span class="rating-badge">
                        <span>★</span> {{ worstReview.rating }}/10
                      </span>
                      <h5 class="mb-0 ms-3">{{ worstReview.title }}</h5>
                    </div>
                    <p class="text-muted mb-1">Date: {{ worstReview.date }}</p>
                    <p>{{ worstReview.text }}</p>
                    <div class="d-flex align-items-center">
                      <i
                        :class="worstReview.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                        @click="toggleLike(worstReview.id)"
                      ></i>
                      <span class="like-count ms-2">• {{ worstReview.likes }} likes</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
      
            <!-- All Reviews Section -->
            <div class="mt-5 mb-5">
              <h4 class="fw-bold pb-4">All Reviews</h4>
              <div v-for="review in paginatedReviews" :key="review.id" class="review-card p-3 mb-4"
              :style="{ backgroundColor: getReviewBgColor(review.rating) }">
                <div class="d-flex align-items-center mb-2">
                  <span class="rating-badge">
                    <span>★</span> {{ review.rating }}/10
                  </span>
                  <h5 class="mb-0 ms-3">{{ review.title }}</h5>
                </div>
                <p class="text-muted mb-1">Date: {{ review.date }}</p>
                <p>{{ review.text }}</p>
                <div class="d-flex align-items-center">
                  <i
                    :class="review.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                    @click="toggleLike(review.id)"
                  ></i>
                  <span class="like-count ms-2">• {{ review.likes }} likes</span>
                </div>
              </div>
            </div>
            </div>
            <!-- Pagination -->
            <nav aria-label="Page navigation">
            <ul class="pagination justify-content-center">
                <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)">
                    &laquo;
                </a>
                </li>
                <li
                class="page-item"
                v-for="page in totalPages"
                :key="page"
                :class="{ active: currentPage === page }"
                >
                <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
                </li>
                <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)">
                    &raquo;
                </a>
                </li>
            </ul>
            </nav>
        </div>
    </div>
  </template>
  
<script setup>
import { reactive, computed } from "vue";
import Search from "@/components/Search.vue";

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
  reviews: [
    {
      id: 1,
      title: "Amazing Sequel!",
      rating: 10,
      date: "March 30, 2024",
      text: "This movie is a masterpiece. The acting, the visuals, and the storyline were phenomenal!",
      likes: 256,
      liked: false,
    },
    {
      id: 2,
      title: "A True Sci-Fi Epic",
      rating: 1,
      date: "April 1, 2024",
      text: "The story was lacking and didn't meet the expectations set by the first film.",
      likes: 150,
      liked: false,
    },
    {
      id: 3,
      title: "Great Movie",
      rating: 8,
      date: "April 5, 2024",
      text: "Overall, a great continuation of the story with amazing visuals.",
      likes: 100,
      liked: false,
    },
    {
      id: 4,
      title: "Great Movie",
      rating: 8,
      date: "April 5, 2024",
      text: "Overall, a great continuation of the story with amazing visuals.",
      likes: 100,
      liked: false,
    },
    {
      id: 5,
      title: "Great Movie",
      rating: 7,
      date: "April 5, 2024",
      text: "Overall, a great continuation of the story with amazing visuals.",
      likes: 100,
      liked: false,
    },
  ],
});

const bestReview = computed(() =>
  movie.reviews.reduce(
    (prev, curr) => (curr.rating > prev.rating ? curr : prev),
    movie.reviews[0]
  )
);

const worstReview = computed(() =>
  movie.reviews.reduce(
    (prev, curr) => (curr.rating < prev.rating ? curr : prev),
    movie.reviews[0]
  )
);

const currentPage = reactive({ value: 1 });
const itemsPerPage = 3;

const totalPages = computed(() =>
  Math.ceil(movie.reviews.length / itemsPerPage)
);

const paginatedReviews = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  return movie.reviews.slice(start, start + itemsPerPage);
});

const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

const toggleLike = (id) => {
  const review = movie.reviews.find((r) => r.id === id);
  if (review) {
    review.liked = !review.liked;
    review.likes += review.liked ? 1 : -1;
  }
};

const getReviewBgColor = (rating) => {
  if (rating >= 8) return "#E3E8DE"; // Light green for high ratings
  if (rating >= 5) return "#F2F4F0"; // Light grey for average ratings
  return "#FAFAFA"; // Lightest grey for low ratings
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

.like-icon {
  font-size: 1.5rem;
  color: #797979;
  cursor: pointer;
  transition: color 0.3s ease;
}

.like-icon:hover {
  color: #545454;
}

.like-count {
  font-size: 1rem;
  color: #545454;
}

.review-card {
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  background-color: #ffffff; /* Default background */
}

.rating-badge {
  background-color: transparent;
  color: #000;
  font-weight: bold;
  border: none;
  padding: 5px 10px;
}

.rating-badge span {
  color: #ffd700; /* Gold for stars */
}

.pagination .page-link {
  color: #254E01;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.pagination .page-link:hover {
  background-color: #254E01;
  color: #ffffff;
}

.pagination .page-item.active .page-link {
  background-color: #254E01;
  color: #ffffff;
  border: none;
}
</style>
