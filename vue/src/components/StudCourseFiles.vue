<script setup>
import { onMounted, ref } from "vue";
const file = ref(null);
const props = defineProps({
  topic: String,
  type: String,
  id: Number,
});

onMounted(() => {
  console.log(props.id);
});
</script>

<template>
  <div class="course__item">
    <h4 class="course__item-title">
      {{ props.topic }}
    </h4>
    <div class="course__files">
      <div v-if="type == 'Lecture'" class="course__file">
        <a :href="`http://127.0.0.1:8000/files/34/dw`">
          <svg
            width="40"
            height="40"
            viewBox="0 0 40 40"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M24.9998 3.33325H9.99984C9.11578 3.33325 8.26794 3.68444 7.64281 4.30956C7.01769 4.93468 6.6665 5.78253 6.6665 6.66659V33.3333C6.6665 34.2173 7.01769 35.0652 7.64281 35.6903C8.26794 36.3154 9.11578 36.6666 9.99984 36.6666H29.9998C30.8839 36.6666 31.7317 36.3154 32.3569 35.6903C32.982 35.0652 33.3332 34.2173 33.3332 33.3333V11.6666L24.9998 3.33325Z"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M23.3335 3.33325V9.99992C23.3335 10.884 23.6847 11.7318 24.3098 12.3569C24.9349 12.9821 25.7828 13.3333 26.6668 13.3333H33.3335"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </a>
        <p class="course__files-link">Лекция</p>
      </div>
      <div v-if="type == 'Practice'" class="course__file">
        <a :href="`http://127.0.0.1:8000/files/${props.id}/dw`">
          <svg
            width="40"
            height="40"
            viewBox="0 0 40 40"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M24.9998 3.33325H9.99984C9.11578 3.33325 8.26794 3.68444 7.64281 4.30956C7.01769 4.93468 6.6665 5.78253 6.6665 6.66659V33.3333C6.6665 34.2173 7.01769 35.0652 7.64281 35.6903C8.26794 36.3154 9.11578 36.6666 9.99984 36.6666H29.9998C30.8839 36.6666 31.7317 36.3154 32.3569 35.6903C32.982 35.0652 33.3332 34.2173 33.3332 33.3333V11.6666L24.9998 3.33325Z"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M23.3335 3.33325V9.99992C23.3335 10.884 23.6847 11.7318 24.3098 12.3569C24.9349 12.9821 25.7828 13.3333 26.6668 13.3333H33.3335"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </a>
        <p class="course__files-link">Задание</p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.course__item {
  margin-left: 25px;
  margin-top: 20px;
  width: 984px;
  &-title {
    font-weight: 600;
    color: #fff;
    padding-top: 13px;
    padding-bottom: 13px;
    padding-left: 25px;
    background-color: #02457a;
    border-radius: 10px;
    margin-bottom: 20px;
  }
}
.course__file {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}
.course__files-link {
  font-size: 16px;
  line-height: 24px;
  color: #000;
}
</style>
