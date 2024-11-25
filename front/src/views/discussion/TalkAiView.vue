<!-- src/views/discussion/TalkAiView.vue -->

<template>
    <div class="mt-5 md-5">
      <div class="chat-page">
        <div class="chat-header">
          <!-- <h2 class="fw-bold">{{ discussion.title }}</h2>
          <p class="text-muted">Discussing: <strong>{{ movie.title }}</strong></p> -->
        </div>
  
        <!-- Chat Messages -->
        <div class="chat-container">
          <div
            v-for="message in messages"
            :key="message.id"
            class="message"
            :class="{ 'from-user': message.sender === 'user', 'from-character': message.sender === 'character' }"
          >
            <div class="message-avatar" v-if="message.sender === 'character'">
              <img
                :src="selectedCharacter.image"
                :alt="selectedCharacter.name"
                class="avatar"
              />
            </div>
            <div class="message-content">
              <p class="sender-name">
                {{ message.sender === "character" ? selectedCharacter.name : "You" }}
              </p>
              <p class="message-text">{{ message.text }}</p>
            </div>
            <div class="message-avatar" v-if="message.sender === 'user'">
              <img
                src="https://via.placeholder.com/50"
                alt="User Avatar"
                class="avatar"
              />
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
    </div>
  </template>
  
  <script setup>
import { ref, reactive } from "vue";
import axios from "axios";

const messages = reactive([]);
const newMessage = ref("");

const sendMessage = async () => {
  if (!newMessage.value.trim()) return;

  messages.push({ sender: "You", text: newMessage.value });
  const userMessage = newMessage.value;
  newMessage.value = "";

  try {
    const response = await axios.post("http://127.0.0.1:8000/chats/", {
      message: userMessage,
    });

    messages.push({ sender: "AI", text: response.data.ai_response });
  } catch (error) {
    console.error("Error:", error);
  }
};
</script>
  
  <style scoped>
  .chat-page {
    display: flex;
    flex-direction: column;
    height: 100vh;
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
  