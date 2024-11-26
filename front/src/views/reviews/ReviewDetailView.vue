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
          <div class="d-flex justify-content-end">
            <a href="" class="text-muted me-3" >수정하기</a>
            <a href="" class="text-muted me-3">삭제</a>
          </div>
        </div>

        <!-- Comments Section -->
        <div class="comments-section">
          <!-- Comments Header -->
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h4>{{ comments.length }} Comments</h4>
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

          <!-- 댓글 목록 -->
          <div v-for="comment in sortedComments" :key="comment.id" class="comment-item mb-4">
            <div class="d-flex align-items-start">
              <img :src="comment.user.profileImage || '@/assets/Navbaricons/user.png'" alt="User Profile" class="rounded-circle me-3" width="50" />
              <div>
                <div class="d-flex justify-content-between align-items-center">
                  <h6 class="mb-1 fw-bold me-3">{{ comment.user.username }}</h6>
                  <small class="text-muted">{{ formatDate(comment.created_at) }}</small>
                </div>
                <p class="mb-2">{{ comment.content }}</p>
                <div class="d-flex align-items-center">
                  <a href="#" class="text-muted reply-btn" @click.prevent="toggleReplyInput(comment.id)">Reply</a>
                </div>

                <!-- 대댓글 목록 -->
                <div v-for="reply in comment.replies || []" :key="reply.id" class="reply-item mt-3">
                  <div class="d-flex align-items-start">
                    <img :src="reply.user.profileImage || '@/assets/Navbaricons/user.png'" alt="User Profile" class="rounded-circle me-3" width="40" />
                    <div>
                      <div class="d-flex justify-content-between align-items-center">
                        <h6 class="mb-1 fw-bold me-3">{{ reply.user.username }}</h6>
                        <small class="text-muted">{{ formatDate(reply.created_at) }}</small>
                      </div>
                      <p class="mb-2">{{ reply.content }}</p>
                    </div>
                  </div>
                </div>

                <!-- 대댓글 입력창 -->
                <div v-if="replyInput[comment.id] !== undefined" class="reply-form mt-2 d-flex align-items-center">
                  <input
                    type="text"
                    v-model="replyInput[comment.id]"
                    class="form-control me-2"
                    placeholder="Write a reply..."
                  />
                  <button class="btn custom-button" @click="addReply(comment.id)">Reply</button>
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
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

// API URL 설정
const BASE_URL = "http://localhost:8000";

// 라우터 사용
const route = useRoute();

// 데이터 상태
const review = ref({});
const comments = ref([]);
const isLoadingReview = ref(true);
const isLoadingComments = ref(true);
const likes = ref(0);
const liked = ref(false);
const newComment = ref("");
const sortedComments = ref([]);

// 대댓글 상태
const replyInput = ref({});

// 날짜 포맷 함수
const formatDate = (date) => {
  const options = { year: "numeric", month: "long", day: "numeric" };
  return new Date(date).toLocaleDateString(undefined, options);
};

// 리뷰 상세 정보 가져오기 (Review Post용)
const fetchReviewDetails = async () => {
  const reviewId = Number(route.params.id); // 리뷰 ID
  const movieId = route.params.movieId; // 영화 ID

  try {
    const reviewsResponse = await axios.get(`${BASE_URL}/reviews/${movieId}/`);
    const allReviews = reviewsResponse.data;

    const targetReview = allReviews.find((review) => review.id === reviewId);
    if (!targetReview) {
      throw new Error("Review not found.");
    }

    review.value = targetReview;
    likes.value = targetReview.likes.length;
    liked.value = targetReview.likes.some((user) => user.id === 1); // 현재 사용자 ID: 1로 가정
  } catch (error) {
    console.error("Error fetching review details:", error);
    alert("Failed to load review details.");
  } finally {
    isLoadingReview.value = false;
  }
};

// 댓글 가져오기 (Comments Section용)
const fetchReviewDetail = async () => {
  const reviewId = Number(route.params.id); // 리뷰 ID

  try {
    const commentsResponse = await axios.get(`${BASE_URL}/reviews/${reviewId}/comments/`);
    comments.value = commentsResponse.data.map((comment) => ({
      ...comment,
      user: comment.user || { username: "Unknown", profileImage: "@/assets/Navbaricons/user.png" },
      profileImage: comment.user.profileImage || "@/assets/Navbaricons/user.png", // 기본 이미지 설정
    }));
    sortedComments.value = [...comments.value];
  } catch (error) {
    console.error("Error fetching comments:", error);
    alert("Failed to load comments.");
  } finally {
    isLoadingComments.value = false;
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
  if (!newComment.value.trim()) return;

  try {
    const response = await axios.post(`${BASE_URL}/reviews/${review.value.id}/comments/`, {
      content: newComment.value,
    });
    const newCommentData = {
      ...response.data,
      user: response.data.user || { username: "You", profileImage: "@/assets/Navbaricons/user.png" },
      likes: [],
    };
    comments.value.push(newCommentData);
    sortedComments.value = [...comments.value];
    newComment.value = "";
  } catch (error) {
    console.error("Error adding comment:", error);
  }
};

// 댓글에 대한 reply 입력창 토글
const toggleReplyInput = (commentId) => {
  if (replyInput.value[commentId] !== undefined) {
    // 이미 열려 있다면 닫기
    delete replyInput.value[commentId];
  } else {
    // 열려있지 않다면 빈 문자열로 초기화
    replyInput.value[commentId] = "";
  }
};

// 대댓글 추가
const addReply = async (commentId) => {
  const content = replyInput.value[commentId];

  if (!content || typeof content !== "string" || !content.trim()) {
    alert("Reply cannot be empty.");
    return;
  }

  try {
    const response = await axios.post(
      `${BASE_URL}/reviews/${review.value.id}/comments/${commentId}/replies/`,
      { content }
    );

    const targetComment = comments.value.find((c) => c.id === commentId);
    if (targetComment) {
      if (!targetComment.replies) targetComment.replies = [];
      targetComment.replies.push({
        ...response.data,
        user: response.data.user || { username: "You", profileImage: "@/assets/Navbaricons/user.png" },
      });
    }
    replyInput.value[commentId] = ""; // 입력 필드 초기화
  } catch (error) {
    console.error("Error adding reply:", error);
    alert("Failed to add reply.");
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



// 컴포넌트 마운트 시 데이터 로드
onMounted(() => {
  fetchReviewDetails(); // 리뷰 상세 정보
  fetchReviewDetail(); // 댓글 정보
});
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
