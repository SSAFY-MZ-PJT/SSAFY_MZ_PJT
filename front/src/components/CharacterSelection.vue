<!-- src/components/CharacterSelection.vue -->

<template>
    <div class="character-selection">
      <h4>Choose a Character</h4>
      <div class="character-grid">
        <div
          v-for="character in characters"
          :key="character.id"
          class="character-card"
          @click="selectCharacter(character)"
        >
          <img :src="character.image" :alt="character.name" class="character-image" />
          <h5>{{ character.name }}</h5>
          <p>{{ character.personality }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";

  const emit = defineEmits(["characterSelected"]); // "characterSelected" 이벤트 선언
  
  const characters = ref([
    {
      id: 1,
      name: "Finn",
      personality: "Friendly and knowledgeable",
      image: new URL('@/assets/Discussions/Character1.png', import.meta.url).href,
    },
    {
      id: 2,
      name: "Bella",
      personality: "Sarcastic but insightful",
      image: new URL('@/assets/Discussions/Character2.png', import.meta.url).href,
    },
    {
      id: 3,
      name: "Alice",
      personality: "Energetic and charismatic",
      image: new URL('@/assets/Discussions/Character3.png', import.meta.url).href,
    }
  ]);
  
  // 캐릭터 선택 시 부모에게 데이터 전달
  const selectCharacter = (character) => {
    emit("characterSelected", character);
  };
  </script>
  
  <style scoped>
  .character-selection {
    text-align: center;
  }
  .character-grid {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }
  .character-card {
    cursor: pointer;
    border: 1px solid #ddd;
    padding: 1rem;
    border-radius: 8px;
    transition: transform 0.2s;
  }
  .character-card:hover {
    transform: scale(1.05);
  }
  .character-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
  }
  </style>
  