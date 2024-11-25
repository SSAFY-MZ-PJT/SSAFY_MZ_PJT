<template>
  <div>
    <DecoBox />
    <div class="mx-4">
      <div class="container pt-5">
        <!-- Review Post -->
        <div class="review-post mb-5">
          <!-- Title and Details -->
          <h1 class="fw-bold mb-3">{{ review.title }}</h1>
          <div class="d-flex justify-content-between align-items-center mb-3">
            <p class="text-muted mb-0">{{ review.date }}</p>
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
                  <h6 class="mb-1 fw-bold">{{ comment.author }}</h6>
                  <small class="text-muted">{{ comment.date }}</small>
                </div>
                <p class="mb-2">{{ comment.text }}</p>
                <div class="d-flex align-items-center">
                  <button class="btn none-button btn-sm me-2" @click="toggleCommentLike(comment.id)">
                    <i :class="comment.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"></i>
                    <span class="like-count"> • {{ comment.likes }}</span>
                  </button>
                  <a href="#" class="text-muted reply-btn" @click.prevent="toggleReply(comment.id)">Reply</a>
                </div>

                <!-- Reply Form -->
                <div v-if="comment.showReplyForm" class="reply-form mt-3">
                  <div class="d-flex align-items-center">
                    <img
                      :src="userProfileImage"
                      alt="Reply Profile Picture"
                      class="rounded-circle me-3"
                      width="40"
                    />
                    <input
                      type="text"
                      v-model="replyText"
                      class="form-control me-2"
                      placeholder="Add a reply..."
                    />
                    <button class="btn custom-button btn-sm" @click="addReply(comment.id)">Post</button>
                  </div>
                </div>

                <!-- Replies -->
                <div v-if="comment.replies.length" class="replies mt-3">
                  <div
                    v-for="reply in comment.replies"
                    :key="reply.id"
                    class="d-flex align-items-start mb-2"
                  >
                    <img :src="reply.profileImage" alt="Reply Profile" class="rounded-circle me-3" width="40" />
                    <div>
                      <h6 class="mb-1 fw-bold">{{ reply.author }}</h6>
                      <p class="mb-0">{{ reply.text }}</p>
                      <small class="text-muted">{{ reply.date }}</small>
                    </div>
                  </div>
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
import { ref } from "vue";

// Sample data for the review post
const review = {
  title: "One Of The Greatest Sequel Ever Made, Dune: Part Two Was Easily The Best Films Of The Year So Far",
  date: "20 Feb 2024",
  rating: 10,
  content:
    "In the quiet embrace of ink and page, a story unfolded, timeless and sage, through the lens of a filmmaker's artistry, its essence soared, a masterpiece for all to see.sd",
};

// Like state for the review
const likes = ref(100);
const liked = ref(false);

const toggleLike = () => {
  liked.value = !liked.value;
  likes.value += liked.value ? 1 : -1;
};

// User profile image
const userProfileImage = "https://via.placeholder.com/50";

// Comments data
const comments = ref([
  {
    id: 1,
    author: "Courtney Henry",
    profileImage: "https://via.placeholder.com/50",
    date: "20h ago",
    text: "Ut ultricies ultrices interdum dolor sodales. Vitae feugiat vitae vitae quis id consectetur.",
    likes: 12,
    liked: false,
    showReplyForm: false,
    replies: [],
  },
  {
    id: 2,
    author: "Ronald Richards",
    profileImage: "https://via.placeholder.com/50",
    date: "6h ago",
    text: "Lorem fringilla pretium magna purus orci faucibus morbi.",
    likes: 8,
    liked: false,
    showReplyForm: false,
    replies: [],
  },
]);

const newComment = ref("");
const replyText = ref("");

// Add a new comment
const addComment = () => {
  if (newComment.value.trim()) {
    comments.value.push({
      id: Date.now(),
      author: "You",
      profileImage: userProfileImage,
      date: "Just now",
      text: newComment.value,
      likes: 0,
      liked: false,
      showReplyForm: false,
      replies: [],
    });
    newComment.value = "";
  }
};

// Sort comments
const sortedComments = ref(comments.value);
const sortComments = (type) => {
  if (type === "recent") {
    sortedComments.value = [...comments.value].sort((a, b) => b.id - a.id);
  } else if (type === "likes") {
    sortedComments.value = [...comments.value].sort((a, b) => b.likes - a.likes);
  }
};

// Toggle like for a comment
const toggleCommentLike = (id) => {
  const comment = comments.value.find((comment) => comment.id === id);
  if (comment) {
    comment.liked = !comment.liked;
    comment.likes += comment.liked ? 1 : -1;
  }
};

// Show reply form for a comment
const toggleReply = (id) => {
  const comment = comments.value.find((comment) => comment.id === id);
  if (comment) {
    comment.showReplyForm = !comment.showReplyForm;
  }
};

// Add a reply to a comment
const addReply = (id) => {
  const comment = comments.value.find((comment) => comment.id === id);
  if (comment && replyText.value.trim()) {
    comment.replies.push({
      id: Date.now(),
      author: "You",
      profileImage: userProfileImage,
      date: "Just now",
      text: replyText.value,
    });
    replyText.value = "";
    comment.showReplyForm = false;
  }
};
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
