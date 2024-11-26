<!-- BoardDetailView -->
<template>
  <div>
    <Search />
    <div class="mx-4">
      <div v-if="isLoading" class="text-center my-5">
        <p>Loading movie details...</p>
      </div>
      <div v-else>
        <!-- Movie Details -->
        <div class="container mt-5">
          <div class="row pb-5">
            <div class="col-md-4">
              <!-- Movie Poster with Link -->
              <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
                <img :src="movie.poster_image_url" alt="Movie Poster" class="img-fluid rounded shadow" />
              </router-link>
            </div>
            <div class="col-md-8">
              <div class="d-flex justify-content-between align-items-start mb-3">
                <h1 class="fw-bold">{{ movie.title }}</h1>
              </div>
              <p class="text-muted">{{ movie.release_date }} • {{ movie.runtime }} mins</p>
              <div class="mb-3">
                <span v-for="genre in movie.genres" :key="genre.id" class="badge bg-secondary me-2">
                  {{ genre.name }}
                </span>
              </div>
              
              <div class="mt-4">
                <h6 class="mb-3" style="color: #797979;">
                  <strong>Directors:</strong>&nbsp;&nbsp;<span style="color: #002C0C;">{{ movie.director.name }}</span>
                </h6>
                <div v-if="movie.actors && movie.actors.length > 0">
                  <h6 class="mb-3" style="color: #797979;">
                    <strong>Actors:</strong>&nbsp;&nbsp;
                    <span
                      v-for="(actor, index) in movie.actors"
                      :key="actor.id"
                      style="color: #002C0C; display: inline-block;"
                    >
                    {{ actor.name }}<span v-if="index < movie.actors.length - 1">•&nbsp;</span>
                    </span>
                  </h6>
                </div>
              </div>
              
              <p class="lead">{{ movie.plot }}</p>
              <div v-if="movie.tagline" class="tagline">
                "{{ movie.tagline }}"
              </div>
              <hr>
              <div class="mt-4 d-flex justify-content-end"> 
                <button
                  class="btn custom-button"
                  @click="toggleFavorite(movieStore.movieDetails.id)"
                  :class="{ 'btn-success': movieStore.movieDetails.isFavorite, 'btn-outline-primary': !movieStore.movieDetails.isFavorite }"
                >
                  <i :class="movieStore.movieDetails.isFavorite ? 'bi bi-bookmark-check-fill' : 'bi bi-bookmark'"></i>
                  {{ movieStore.movieDetails.isFavorite ? 'Added to Watchlist' : 'Add to Watchlist' }}
                </button>
                <router-link :to="{ name: 'ReviewCreateView', params: { id: movie.id } }">
                  <button class="btn custom-button ms-3">
                    <i class="bi bi-pencil-square"></i> Create Review
                  </button>
                </router-link>
              </div>
            </div>
          </div>


          <!-- Highlighted Reviews -->
          <div class="mt-5">
            <h4 class="fw-bold mb-4">Highlighted Reviews</h4>
            <hr>
            <div class="row">
              <div
                class="col-md-6"
                v-for="review in highlightedReviews"
                :key="review.id"
                @click="navigateToReview(review.id, movie.id)"
              >
                <div class="review-card p-3 mb-4" :style="{ backgroundColor: getReviewBgColor(review.rating) }">
                  <div class="d-flex align-items-center mb-2">
                    <span class="rating-badge">
                      <span>★</span> {{ review.rating }}/10
                    </span>
                    <h5 class="mb-0 ms-3">{{ review.title }}</h5>
                  </div>
                  <p class="text-muted mb-1">Date • {{ formatDate(review.created_at) }}</p>
                  <p class="text-secondary">{{ review.content }}</p>
                  <div class="d-flex align-items-center">
                    <i
                      :class="review.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                      @click="toggleLike(review.id)"
                    ></i>
                    <span class="like-count ms-2">• {{ review.likes.length }} likes</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
            
          <!-- All Reviews -->
          <div class="mt-5">
            <h4 class="fw-bold">All Reviews</h4>
            <hr>
            <div class="row">
              <div
                v-for="review in paginatedReviews"
                :key="review.id"
                class="col-md-6 d-flex"
              >
                <div
                  class="review-card p-3 mb-4 w-100"
                  :style="{ backgroundColor: getReviewBgColor(review.rating) }"
                  @click="navigateToReview(review.id, movie.id)"
                >
                  <div class="d-flex align-items-center mb-2">
                    <span class="rating-badge">
                      <span>★</span> {{ review.rating }}/10
                    </span>
                    <h5 class="mb-0 ms-3">{{ review.title }}</h5>
                  </div>
                  <p class="text-muted mb-1">Date • {{ formatDate(review.created_at) }}</p>
                  <p class="text-secondary">{{ review.content }}</p>
                  <div class="d-flex align-items-center">
                    <i
                      :class="review.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                      @click.stop="toggleLike(review.id)"
                    ></i>
                    <span class="like-count ms-2">• {{ review.likes.length }} likes</span>
                  </div>
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
                <a class="page-link" href="#" @click.prevent="changePage(page)">
                  {{ page }}
                </a>
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
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useReviewStore } from '@/stores/review';
import { useMovieStore } from "@/stores/movie";

const movieStore = useMovieStore();
const router = useRouter()
const route = useRoute();
const reviewStore = useReviewStore();

const movie = ref({});
const reviews = ref([]);
const isLoading = ref(true);

// 날짜 포맷 함수
const formatDate = (isoDate) => {
  const date = new Date(isoDate);
  return date.toISOString().split("T")[0]; // "YYYY-MM-DD" 포맷
};

// Pagination
const currentPage = ref(1);
const itemsPerPage = 6;

const paginatedReviews = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  return reviews.value.slice(start, start + itemsPerPage);
});

const totalPages = computed(() => Math.ceil(reviews.value.length / itemsPerPage));

const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

// Highlighted Reviews Logic
const highlightedReviews = computed(() => {
  const sortedByLikes = [...reviews.value].sort((a, b) => b.likes - a.likes);

  if (sortedByLikes.every((review) => review.likes === 0)) {
    return [...reviews.value].sort((a, b) => new Date(b.created_at) - new Date(a.created_at)).slice(0, 2);
  }

  return sortedByLikes.slice(0, 2);
});

// Fetch data
const fetchMovieDetails = async () => {
  const movieId = route.params.movieId;
  try {
    const movieResponse = await reviewStore.fetchMovieDetails(movieId);
    movie.value = movieResponse.movie;
    reviews.value = movieResponse.reviews;

    console.log('Fetched Movie Details:', movie.value); // 디버깅용
  } catch (error) {
    console.error('Failed to load movie details:', error);
  } finally {
    isLoading.value = false;
  }
};

// Like toggle
const toggleLike = async (reviewId) => {
  try {
    await reviewStore.toggleLike(reviewId);
    const review = reviews.value.find((r) => r.id === reviewId);
    if (review) {
      review.liked = !review.liked;
      review.likes += review.liked ? 1 : -1;
    }
  } catch (error) {
    console.error('Failed to toggle like:', error);
  }
};

// 좋아요 토글 함수
const toggleFavorite = async (movieId) => {
  try {
    await movieStore.toggleFavorite(movieId);
  } catch (error) {
    console.error("Failed to toggle favorite:", error);
  }
};


// Review color based on rating
const getReviewBgColor = (rating) => {
  if (rating >= 8) return '#E3E8DE';
  if (rating >= 4) return '#F2F4F0';
  return '#FAFAFA';
};

const navigateToReview = (reviewId, movieId) => {
  console.log('Navigating to ReviewDetailView:', { reviewId, movieId });
  router.push({ name: 'ReviewDetailView', params: { id: reviewId, movieId } });
};

// On component mounted
onMounted(fetchMovieDetails);
</script>

<style scoped>
hr {
  border: none;
  border-top: 2px solid #ddd;
  margin: 2rem 0;
}

.container {
  max-width: 1200px;
}

.img-fluid {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  cursor: pointer; /* Make the poster clickable */
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
  flex: 1;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease; 
  cursor: pointer;
  /* border: 2px solid #babeb6; */
}

.review-card:hover {
  transform: scale(1.05); 
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); 
}

.rating-badge {
  background-color: transparent;
  color: #000;
  font-weight: bold;
  border: none;
  padding: 5px 10px;
}

.rating-badge span {
  color: #ffd700;
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

.tagline {
  font-size: 1.5rem;
  font-style: italic;
  color: #4a4a4a;
  border-left: 5px solid #254e01;
  padding-left: 15px;
  margin-top: 20px;
}
</style>
