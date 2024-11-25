<!-- src/views/discussion/CreateDiscussionView.vue -->

<template>
  <div>
    <DecoBox />
    <div class="container mt-5">
      <!-- 영화 디테일 설명 -->
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

          <!-- 장르 표시 -->
          <div class="mb-3">
            <span v-for="genre in movie.genres" :key="genre" class="badge bg-secondary me-2">
              {{ genre }}
            </span>
          </div>

          <!-- 줄거리 -->
          <p class="lead">{{ movie.plot }}</p>

          <!-- 감독, 작가, 출연진 -->
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
          <div v-if="movie.tagline" class="tagline mt-4">
            "{{ movie.tagline }}"
          </div>
        </div>
      </div>

      <!-- 토론 생성 폼 -->
      <div class="review-form mt-5">
        <h2 class="text-center fw-bold">Create a Discussion</h2>

        <!-- 평점 -->
        <div class="text-center mt-5">
          <h4 class="fw-bold mb-4">My Rate:</h4>
          <div class="mb-4 stars-container">
            <span
              v-for="star in 5"
              :key="star"
              @mouseover="hoverStars(star)"
              @mouseleave="resetStars"
              @click="setRating(star)"
              class="star"
              :class="{ active: star <= hoverRating || star <= rating }"
            >
              ★
            </span>
          </div>
        </div>

        <!-- 토론 제목 -->
        <div class="mb-4">
          <input
            type="text"
            v-model="discussion.title"
            placeholder="Enter discussion title"
            class="form-control"
          />
        </div>

        <!-- 토론 세부내용 -->
        <div class="mb-5">
          <textarea
            v-model="discussion.details"
            placeholder="Enter discussion details"
            class="form-control"
            rows="5"
          ></textarea>
        </div>

        <!-- 캐릭터 선택 -->
        <div class="character-selection text-center">
          <h4 class="fw-bold">Choose a Character to Start Discussion</h4>
          <div class="character-grid mt-5">
            <div
              v-for="character in characters"
              :key="character.id"
              class="character-card"
              :class="{ selected: selectedCharacterId === character.id }"
              @click="selectCharacter(character)"
            >
              <img
                :src="character.image"
                :alt="character.name"
                class="character-image"
              />
              <div class="character-info">
                <h5>{{ character.name }}</h5>
                <p><strong>Age:</strong> {{ character.age }}</p>
                <p><strong>Personality:</strong> {{ character.personality }}</p>
                <p><strong>Favorite Movie:</strong> {{ character.favoriteMovie }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 버튼 -->
        <div class="d-flex justify-content-between mt-5">
          <button class="btn custom-button" @click="goBack">Back</button>
          <button
            class="btn custom-button"
            :disabled="!selectedCharacterId || !discussion.title || !discussion.details"
            @click="startDiscussion"
          >
            Create
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import DecoBox from '@/components/DecoBox.vue'

const router = useRouter();

// 영화 데이터
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
  tagline: "Beyond Fear, Destiny Awaits",
});

// 캐릭터 데이터
const characters = [
  {
    id: 1,
    name: "Professor Dialogue",
    image: "src/assets/Discussions/Character1.png",
    age: 45,
    personality: "Intellectual, Curious",
    favoriteMovie: "The Matrix",
  },
  {
    id: 2,
    name: "Friendly Critic",
    image: "src/assets/Discussions/Character2.png",
    age: 35,
    personality: "Empathetic, Honest",
    favoriteMovie: "The Shawshank Redemption",
  },
  {
    id: 3,
    name: "Creative Thinker",
    image: "src/assets/Discussions/Character3.png",
    age: 29,
    personality: "Visionary, Optimistic",
    favoriteMovie: "Inception",
  },
];

// 토론 상태
const discussion = reactive({
  title: "",
  details: "",
});

// 평점
const rating = ref(0);
const hoverRating = ref(0);

const setRating = (value) => {
  rating.value = value;
};

const hoverStars = (value) => {
  hoverRating.value = value;
};

const resetStars = () => {
  hoverRating.value = 0;
};

// 선택된 캐릭터
const selectedCharacterId = ref(null);
const selectCharacter = (character) => {
  selectedCharacterId.value = character.id;
  alert(
    `Selected Character: ${character.name}\nPersonality: ${character.personality}`
  );
};

// 뒤로 가기
const goBack = () => {
  router.push("/");
};

// 토론 생성
const startDiscussion = () => {
  if (!selectedCharacterId.value || !discussion.title || !discussion.details) {
    alert("Please fill in all fields and select a character.");
    return;
  }
  alert(
    `Discussion with ${characters.find((c) => c.id === selectedCharacterId.value).name} started!`
  );
};
</script>

<style scoped>
/* 기존 스타일 유지 */

/* 별 평점 스타일 */
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

/* 버튼 스타일 복원 */
.custom-button {
  background-color: #ffffff;
  color: #254e01 !important;
  border: 1px solid #254e01 !important;
  transition: all 0.3s ease;
  padding: 10px 20px;
}

.custom-button:hover:not(:disabled) {
  background-color: #254e01 !important;
  color: #ffffff !important;
  border-color: #254e01 !important;
}

.custom-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* 캐릭터 카드 스타일 */
.character-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  justify-items: center;
}

.character-card {
  position: relative;
  width: 200px;
  text-align: center;
  background: #ffffff;
  border: 2px solid transparent;
  border-radius: 15px;
  padding: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.character-card:hover {
  background: #f7f7f7;
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.character-card.selected {
  border-color: #254e01;
  background-color: #f1f8f3;
}

.character-image {
  width: 100%;
  height: auto;
  border-radius: 10px;
  margin-bottom: 10px;
}

.character-info {
  font-size: 0.9rem;
  color: #333;
}
</style>
