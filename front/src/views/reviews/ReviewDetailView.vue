<!-- ReviewDetailView -->
<template>
  <div>
    <DecoBox />
    <div class="mx-4">
      <div v-if="isLoading" class="text-center my-5">
        <p>Loading review details...</p>
      </div>
      <div v-else class="container pt-5">
        <!-- Review Post -->
        <div class="review-post mb-5">
          <!-- Title and Details -->
          <h1 class="fw-bold mb-3">{{ review.title }}</h1>
          <div class="d-flex justify-content-between align-items-center mb-3">
            <p class="text-muted mb-0">{{ formatDate(review.created_at) }}</p>
            <div class="d-flex align-items-center">
              <span class="rating-badge">
                <span>★</span> {{ review.rating }}/10
              </span>
              <button class="btn none-button like-btn" @click="toggleLike">
                <i :class="liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"></i>
                <span class="like-count"> • {{ likes }}</span>
              </button>
            </div>
          </div>
          <hr />
          <!-- Content -->
          <p class="pb-5 pt-3 fs-5">{{ review.content }}</p>
        </div>

        <!-- Comments Section -->
        <div class="comments-section">
          <!-- Comments Header -->
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h4>{{ comments.length }} Comments</h4>
            <div>
              <a href="#" class="text-muted me-3" @click.prevent="sortComments('recent')">최신순</a>
              <a href="#" class="text-muted" @click.prevent="sortComments('likes')">좋아요순</a>
            </div>
          </div>
          <hr />

          <!-- Comment Form -->
          <div class="comment-form d-flex align-items-center mb-5">
            <img :src="userProfileImage" alt="Profile Picture" class="rounded-circle me-3" width="50" />
            <input
              type="text"
              v-model="newComment"
              class="form-control me-2"
              placeholder="Add a comment..."
            />
            <button class="btn custom-button" @click="addComment">Post</button>
          </div>

          <!-- Comments List -->
          <div v-for="comment in sortedComments" :key="comment.id" class="comment-item mb-4">
            <div class="d-flex align-items-start">
              <img :src="comment.profileImage" alt="User Profile" class="rounded-circle me-3" width="50" />
              <div>
                <div class="d-flex justify-content-between align-items-center">
                  <h6 class="mb-1 fw-bold">{{ comment.user }}</h6>
                  <small class="text-muted">{{ formatDate(comment.created_at) }}</small>
                </div>
                <p class="mb-2">{{ comment.content }}</p>
                <div class="d-flex align-items-center">
                  <button class="btn none-button btn-sm me-2" @click="toggleCommentLike(comment.id)">
                    <i :class="comment.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"></i>
                    <span class="like-count"> • {{ comment.likes }}</span>
                  </button>
                  <a href="#" class="text-muted reply-btn" @click.prevent="toggleReply(comment.id)">Reply</a>
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
import DecoBox from "@/components/DecoBox.vue";
import { ref, onMounted, cloneVNode } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

// API URL 설정
const BASE_URL = "http://localhost:8000";

// 라우터 사용
const route = useRoute();

// 데이터 상태
const review = ref({});
const comments = ref([]);
const isLoading = ref(true);
const likes = ref(0);
const liked = ref(false);
const newComment = ref("");
const sortedComments = ref([]);

// 날짜 포맷 함수
const formatDate = (date) => {
  const options = { year: "numeric", month: "long", day: "numeric" };
  return new Date(date).toLocaleDateString(undefined, options);
};

// 리뷰 상세 정보 및 댓글 가져오기
const fetchReviewDetails = async () => {
  const reviewId = route.params.id;
  try {
    const [reviewResponse, commentsResponse] = await Promise.all([
      axios.get(`${BASE_URL}/reviews/${reviewId}/`),
      axios.get(`${BASE_URL}/reviews/${reviewId}/comments/`),
    ]);

    console.log(reviewResponse.data)
    review.value = reviewResponse.data;
    comments.value = commentsResponse.data;
    likes.value = review.value.likes_count;
    liked.value = review.value.liked || false;
    sortedComments.value = [...comments.value];
  } catch (error) {
    console.error("Error fetching review details:", error);
  } finally {
    isLoading.value = false;
  }
};

// 좋아요 토글
const toggleLike = async () => {
  try {
    await axios.post(`${BASE_URL}/reviews/like/${review.value.id}/`);
    liked.value = !liked.value;
    likes.value += liked.value ? 1 : -1;
  } catch (error) {
    console.error("Error toggling like:", error);
  }
};

// 댓글 추가
const addComment = async () => {
  if (newComment.value.trim()) {
    try {
      const response = await axios.post(`${BASE_URL}/reviews/${review.value.id}/comments/`, {
        content: newComment.value,
      });
      comments.value.push(response.data);
      sortedComments.value = [...comments.value];
      newComment.value = "";
    } catch (error) {
      console.error("Error adding comment:", error);
    }
  }
};

// 댓글 정렬
const sortComments = (type) => {
  if (type === "recent") {
    sortedComments.value = [...comments.value].sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
  } else if (type === "likes") {
    sortedComments.value = [...comments.value].sort((a, b) => b.likes - a.likes);
  }
};

// 댓글 좋아요 토글
const toggleCommentLike = async (commentId) => {
  try {
    await axios.post(`${BASE_URL}/reviews/like/${commentId}/`);
    const comment = comments.value.find((c) => c.id === commentId);
    if (comment) {
      comment.liked = !comment.liked;
      comment.likes += comment.liked ? 1 : -1;
    }
  } catch (error) {
    console.error("Error toggling like for comment:", error);
  }
};

// 컴포넌트 마운트 시 리뷰와 댓글 로드
onMounted(fetchReviewDetails);
</script>


<style scoped>
.container {
  max-width: 1000px;
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

/* 버튼 스타일 */
button {
  transition: all 0.3s ease;
}

button:hover {
  transform: scale(1.05);
}

.custom-button {
  background-color: #ffffff;
  color: #254E01 ;
  border: 1px solid #254E01 ;
  transition: all 0.3s ease;
}

.custom-button:hover:not(:disabled) {
  background-color: #254E01 ;
  color: #ffffff ;
  border-color: #254E01 ;
}

.custom-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* 좋아요 감싸는 버튼 스타일 */
.none-button {
  background-color: #ffffff;
  color: none ;
  border: none ;
  transition: all 0.3s ease;
}

.none-button:hover:not(:disabled) {
  background-color: none ;
  color: #ffffff ;
  border: none ;
}

.none-button:disabled {
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

.comment-item {
  border-bottom: 1px solid #ddd;
  padding-bottom: 1rem;
}
</style>
