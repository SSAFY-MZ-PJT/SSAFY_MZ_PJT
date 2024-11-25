<template>
    <div>
      <Search />
      <div class="container mt-5">
        <!-- Section Title -->
        <h2 class="text-center fw-bold mb-4">Search Results</h2>
        <p class="text-muted text-center">
          Explore the movies matching your search query.
        </p>
  
        <!-- Movie Cards Grid -->
        <div class="mt-5">
          <div v-if="isLoading" class="text-center">
            <p>Loading movies...</p>
          </div>
          <div v-else-if="searchedMovies.length === 0" class="text-center">
            <p>No results found for "{{ route.query.q }}"</p>
          </div>
          <div v-else>
            <div class="container">
              <div class="movie-grid">
                <!-- Movie Cards -->
                <div
                  class="movie-card"
                  v-for="movie in paginatedMovies"
                  :key="movie.id"
                >
                  <div class="card h-100 mt-3 me-2">
                    <div class="position-relative">
                      <!-- Movie Poster -->
                      <router-link
                        :to="{ name: 'MovieDetailView', params: { id: movie.id } }"
                        class="card-link"
                      >
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
                        :class="{ active: movie.isFavorite }"
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
                        📅 {{ movie.release_date }} &nbsp;&nbsp;
                        <span class="text-warning fw-bold">
                          ★ {{ movie.rating.toFixed(1) }}
                        </span>
                      </p>
                      <div class="d-flex align-items-center justify-content-between">
                        <!-- Trailer Button -->
                        <button
                          class="btn custom-button btn-sm"
                          @click="playTrailer(movie.trailer_url)"
                        >
                          ▶ Trailer
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
  
            <!-- Pagination -->
            <div class="mt-5 pt-4">
              <nav aria-label="Page navigation">
                <ul class="pagination justify-content-center">
                  <!-- Previous 5 -->
                  <li class="page-item" :class="{ disabled: currentPage <= 5 }">
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(currentPage - 5)"
                    >
                      &laquo; Prev 5
                    </a>
                  </li>
  
                  <!-- Previous Page -->
                  <li class="page-item" :class="{ disabled: currentPage === 1 }">
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(currentPage - 1)"
                    >
                      &laquo;
                    </a>
                  </li>
  
                  <!-- Page Numbers -->
                  <li
                    class="page-item"
                    v-for="page in visiblePages"
                    :key="page"
                    :class="{ active: page === currentPage }"
                  >
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(page)"
                    >
                      {{ page }}
                    </a>
                  </li>
  
                  <!-- Next Page -->
                  <li
                    class="page-item"
                    :class="{ disabled: currentPage === totalPages }"
                  >
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(currentPage + 1)"
                    >
                      &raquo;
                    </a>
                  </li>
  
                  <!-- Next 5 -->
                  <li
                    class="page-item"
                    :class="{ disabled: currentPage > totalPages - 5 }"
                  >
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(currentPage + 5)"
                    >
                      Next 5 &raquo;
                    </a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import Search from "@/components/Search.vue";
  import { useRoute } from "vue-router";
  import { ref, computed, onMounted } from "vue";
  import axios from "axios";
  
  // Route and State
  const route = useRoute();
  const searchedMovies = ref([]);
  const isLoading = ref(false);
  
  // Pagination
  const currentPage = ref(1);
  const itemsPerPage = 15;
  
  const paginatedMovies = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return searchedMovies.value.slice(start, end);
  });
  
  const totalPages = computed(() =>
    Math.ceil(searchedMovies.value.length / itemsPerPage)
  );
  
  const visiblePages = computed(() => {
    const start = Math.floor((currentPage.value - 1) / 5) * 5 + 1;
    const end = Math.min(start + 4, totalPages.value);
    const pages = [];
    for (let i = start; i <= end; i++) {
      pages.push(i);
    }
    return pages;
  });
  
  // Fetch Search Results
  const fetchSearchResults = async () => {
    const query = route.query.q;
    if (!query) return;
  
    isLoading.value = true;
  
    try {
      const response = await axios.get("http://localhost:8000/movies/search/", {
        params: { query },
      });
      searchedMovies.value = response.data.searched_movies;
    } catch (error) {
      console.error("Error fetching search results:", error);
      alert("Failed to fetch search results. Please try again.");
    } finally {
      isLoading.value = false;
    }
  };
  
  // Page Change
  const changePage = (page) => {
    if (page >= 1 && page <= totalPages.value) {
      currentPage.value = page;
      window.scrollTo(0, 0);
    }
  };
  
  // Toggle Favorite
  const toggleFavorite = (id) => {
    console.log(`Toggled favorite for movie with id: ${id}`);
  };
  
  // Play Trailer
  const playTrailer = (url) => {
    window.open(url, "_blank");
  };
  
  // Initial Fetch
  onMounted(fetchSearchResults);
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
  .movie-grid {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  }
  
  .movie-card {
    display: flex;
    flex-direction: column;
  }
  
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
  
  .poster-image {
    width: 100%;
    height: 375px;
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
  
  /* Pagination */
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
  
  .card-link {
    text-decoration: none; /* 밑줄 제거 */
    }
  
    .card-link:hover {
      text-decoration: none; /* 호버 상태에서도 밑줄 제거 */
    }
  </style>
  