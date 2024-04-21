<script setup>
import Sidebar from "@/components/Sidebar.vue";
</script>

<template>
  <div class="container">
    <Sidebar :userId="$route.params.userId" :path="$route.path" />
    <div class="course__inner">
      <div class="firstcol">
        <h3 class="course__title">Выберите предмет</h3>
        <ul class="course__list">
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="lesson"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">Алгоритмы и структуры данных</p>
            </label>
          </li>
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="lesson"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">Алгоритмы и структуры данных</p>
            </label>
          </li>
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="lesson"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">Алгоритмы и структуры данных</p>
            </label>
          </li>
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="lesson"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">Алгоритмы и структуры данных</p>
            </label>
          </li>
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="lesson"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">Алгоритмы и структуры данных</p>
            </label>
          </li>
        </ul>
        <div class="course__paginate">
          <a href="#" class="course__page course__page--active">1</a>
          <a href="#" class="course__page">2</a>
          <a href="#" class="course__page">3</a>
        </div>
      </div>
      <div class="secondcol">
        <div class="course__item">
          <h4 class="course__item-title">
            Бинарные деревья. Ввод дерева. Обход. Высота дерева
          </h4>
          <div class="course__files">
            <div class="course__file">
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
              <a href="#" class="course__files-link">Лекция</a>
            </div>
            <div class="course__file">
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
              <a href="#" class="course__files-link">Задание</a>
            </div>
          </div>
        </div>
        <div class="course__item">
          <h4 class="course__item-title">
            Дерево минимальной высоты. Ввод дерева. Вывод дерева
          </h4>
          <div class="course__files">
            <div class="course__file">
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
              <a href="#" class="course__files-link">Лекция</a>
            </div>
            <div class="course__file">
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
              <a href="#" class="course__files-link">Задание</a>
            </div>
          </div>
        </div>
        <div class="course__paginate course__paginate--files">
          <a href="#" class="course__page course__page--active">1</a>
          <a href="#" class="course__page">2</a>
          <a href="#" class="course__page">3</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.secondcol {
  margin-bottom: 30px;
}
.course__inner {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 219px;
}
.course__title {
  margin-left: 25px;
  margin-top: 15px;
  font-size: 24px;
  line-height: 36px;
  margin-bottom: 20px;
  font-weight: 400;
}
.course__list {
  list-style: none;
  margin-left: 25px;
  &-item label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
}
.course__item-radio--custom {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #000000;
  border-radius: 2px;
  position: relative;
  transition: 0.2s ease-in;
}
.course__item-radio--custom::before {
  content: "";
  display: inline-block;
  width: 10px;
  height: 10px;
  background-image: url(../assets/checked.svg);
  background-repeat: no-repeat;
  background-size: contain;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0);
  margin-top: 1px;
  transition: 0.2s ease-in;
}
.course__item-radio--real:checked + .course__item-radio--custom::before {
  transform: translate(-50%, -50%) scale(1);
}
.course__item-radio--real:checked + .course__item-radio--custom{
  border: 2px solid #02457a;
}
.course__item-radio--real{
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.course__item-text {
  font-size: 20px;
  line-height: 30px;
}
.course__paginate {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-right: 25px;
  &--files {
    justify-content: center;
    margin-bottom: 20px;
  }
}
.course__page {
  font-size: 14px;
  line-height: 17px;
  color: rgba(#000, 0.2);
  padding-top: 5px;
  padding-bottom: 5px;
  padding-left: 10px;
  padding-right: 10px;
  &:hover {
    border-radius: 4px;
    background-color: rgba(#0000000d, 0.05);
  }
  &--active {
    background-color: #02457a;
    color: #fff;
    border-radius: 4px;
    &:hover {
      background-color: #02457a;
      color: #fff;
      border-radius: 4px;
    }
  }
}
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
