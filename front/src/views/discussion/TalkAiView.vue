<!-- src/views/discussion/TalkAiView.vue -->

<template>
  <div class="chat-page mt-5">
    <!-- Chat Messages -->
    <div class="chat-container mt-5">
      <div
        v-for="message in messages"
        :key="message.id"
        class="message"
        :class="{ 'from-user': message.sender === 'user', 'from-character': message.sender === 'character' }"
      >
        <div class="message-avatar" v-if="message.sender === 'character'">
          <img
            :src="characterImage"
            :alt="characterName"
            class="avatar"
          />
        </div>
        <div class="message-content">
          <p class="sender-name">
            {{ message.sender === "character" ? characterName : username }}
          </p>
          <p class="message-text">{{ message.text }}</p>
        </div>
        <div class="message-avatar" v-if="message.sender === 'user'">
          <img :src="profileImage || defaultProfileImage" :alt="username" class="avatar" />
        </div>
      </div>
    </div>

    <!-- Message Input -->
    <div class="chat-input-container">
      <input
        type="text"
        v-model="newMessage"
        placeholder="Type your message here..."
        class="chat-input"
        @keyup.enter="sendMessage"
      />
      <button class="btn custom-button" @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from "vue";
import { useUserStore } from "@/stores/auth.js";
import axios from "axios";

// Pinia Store 가져오기
const userStore = useUserStore();
const { username, profileImage } = userStore;
const defaultProfileImage = "@/assets/Navbaricons/user.png"; // 기본 이미지 경로

// Chat 상태 관리
const messages = reactive([]);
const newMessage = ref("");

// Props로 캐릭터 정보 전달
const props = defineProps({
  characterName: {
    type: String,
    required: true,
  },
  characterPersonality: {
    type: String,
    required: true,
  },
  characterImage: {
    type: String,
    required: true,
  },
});

// Initialize Chat
const initializeChat = async () => {
  try {
    const response = await axios.post("http://127.0.0.1:8000/chats/", {
      name: props.characterName,
      personality: props.characterPersonality,
    });
    messages.push({
      id: Date.now(),
      sender: "character",
      text: response.data.ai_response,
    });
  } catch (error) {
    console.error("Error initializing chat:", error);
  }
};

// Send User Message
const sendMessage = async () => {
  if (!newMessage.value.trim()) return;

  messages.push({
    id: Date.now(),
    sender: "user",
    text: newMessage.value,
  });

  const userMessage = newMessage.value;
  newMessage.value = "";

  try {
    const response = await axios.post("http://127.0.0.1:8000/chats/", {
      message: userMessage,
    });
    messages.push({
      id: Date.now(),
      sender: "character",
      text: response.data.ai_response,
    });
  } catch (error) {
    console.error("Error sending message:", error);
  }
};

/// Fetch User Data and Initialize Chat
onMounted(async () => {
  if (!userStore.username) {
    // 사용자 정보가 없으면 데이터를 가져옵니다.
    await userStore.fetchUserData();
  }
  initializeChat();
});
</script>

  
  <style scoped>
  .chat-page {
    display: flex;
    flex-direction: column;
    height: 90vh;
    max-width: 800px;
    margin: 0 auto;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #fdfdfd;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .chat-header {
    padding: 20px;
    background-color: #86a16e;
    color: white;
    border-radius: 10px 10px 0 0;
  }
  
  .chat-container {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    background-color: #fafafa;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .message {
    display: flex;
    gap: 10px;
    align-items: flex-start;
  }
  
  .message-avatar {
    flex-shrink: 0;
  }
  
  .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }
  
  .message-content {
    max-width: 75%;
    padding: 10px;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .message-content .sender-name {
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  .message-content .message-text {
    font-size: 1rem;
  }
  
  .from-user {
    flex-direction: row-reverse;
    align-self: flex-end;
  }
  
  .from-user .message-content {
    background-color: #d1e7dd;
  }
  
  .from-character .message-content {
    background-color: #fff;
  }
  
  .chat-input-container {
    display: flex;
    gap: 10px;
    padding: 20px;
    background-color: #f7f7f7;
    border-top: 1px solid #ddd;
  }
  
  .chat-input {
    flex: 1;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
  }
  
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
  </style>
  