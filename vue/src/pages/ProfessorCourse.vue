<script setup>
import Sidebar from "../components/Sidebar.vue";
</script>

<template>
  <div class="container">
    <Sidebar class="aside" :userId="$route.params.userId" :path="$route.path" />
    <div class="course__inner">
      <div class="fac">
        <p class="fac__title title">Выберите факультет</p>
        <ul class="fac__list">
          <li class="fac__list-item">
            <label>
              <input
                type="radio"
                name="fac-course"
                class="fac__item-radio--real"
              />
              <span class="fac__item-radio--custom"></span>
              <p class="fac__item-text">
                Институт компьютерных наук и технологий
              </p>
            </label>
          </li>
          <li class="fac__list-item">
            <label>
              <input
                type="radio"
                name="fac-course"
                class="fac__item-radio--real"
              />
              <span class="fac__item-radio--custom"></span>
              <p class="fac__item-text">Физико-Математический факультет</p>
            </label>
          </li>
        </ul>
      </div>
      <div class="selectors">
        <div class="selectors__course">
          <p class="course__title title">Выберите курс</p>
          <ul class="course__list">
            <li class="course__list-item">
              <label>
                <input
                  type="radio"
                  name="makecourse"
                  class="course__item-radio--real"
                />
                <span class="course__item-radio--custom"></span>
                <p class="course__item-text">1 курс</p>
              </label>
            </li>
            <li class="course__list-item">
              <label>
                <input
                  type="radio"
                  name="makecourse"
                  class="course__item-radio--real"
                />
                <span class="course__item-radio--custom"></span>
                <p class="course__item-text">2 курс</p>
              </label>
            </li>
            <li class="course__list-item">
              <label>
                <input
                  type="radio"
                  name="makecourse"
                  class="course__item-radio--real"
                />
                <span class="course__item-radio--custom"></span>
                <p class="course__item-text">3 курс</p>
              </label>
            </li>
            <li class="course__list-item">
              <label>
                <input
                  type="radio"
                  name="makecourse"
                  class="course__item-radio--real"
                />
                <span class="course__item-radio--custom"></span>
                <p class="course__item-text">4 курс</p>
              </label>
            </li>
          </ul>
        </div>
        <div class="selectors__groups">
          <p class="groups__title title">Выберите группу</p>
          <ul class="groups__list">
            <li class="groups__list-item">
              <label>
                <input
                  type="radio"
                  name="group-course"
                  class="groups__item-radio--real"
                />
                <span class="groups__item-radio--custom"></span>
                <p class="groups__item-text">ФИТ-12-23</p>
              </label>
            </li>
            <li class="groups__list-item">
              <label>
                <input
                  type="radio"
                  name="group-course"
                  class="groups__item-radio--real"
                />
                <span class="groups__item-radio--custom"></span>
                <p class="groups__item-text">ПМИ-12-23</p>
              </label>
            </li>
            <li class="groups__list-item">
              <label>
                <input
                  type="radio"
                  name="group-course"
                  class="groups__item-radio--real"
                />
                <span class="groups__item-radio--custom"></span>
                <p class="groups__item-text">ПМИ-34-23</p>
              </label>
            </li>
            <li class="groups__list-item">
              <label>
                <input
                  type="radio"
                  name="group-course"
                  class="groups__item-radio--real"
                />
                <span class="groups__item-radio--custom"></span>
                <p class="groups__item-text">ИТХ-12-23</p>
              </label>
            </li>
          </ul>
          <div class="groups__paginate">
            <a href="#" class="groups__page groups__page--active">1</a>
            <a href="#" class="groups__page">2</a>
            <a href="#" class="groups__page">3</a>
          </div>
        </div>
      </div>
      <div class="files">
        <div class="files__upload">
          <label class="upload__label">
            <input type="file" class="upload__input" />
            <span class="upload__span">
              <svg
                width="100"
                height="100"
                viewBox="0 0 100 100"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M16.6668 62.0793C13.5711 58.9164 11.2358 55.0906 9.83775 50.8915C8.4397 46.6925 8.01555 42.2303 8.59745 37.843C9.17934 33.4558 10.752 29.2585 13.1963 25.569C15.6407 21.8796 18.8925 18.7948 22.7057 16.5483C26.5188 14.3017 30.7931 12.9524 35.205 12.6025C39.6168 12.2526 44.0504 12.9113 48.17 14.5287C52.2895 16.1461 55.987 18.6798 58.9823 21.9378C61.9777 25.1958 64.1923 29.0928 65.4584 33.3335H72.9168C76.9397 33.333 80.8562 34.6265 84.0876 37.0228C87.319 39.4191 89.6939 42.7912 90.8617 46.641C92.0294 50.4907 91.9279 54.614 90.5723 58.4017C89.2167 62.1894 86.6788 65.4406 83.3334 67.6751"
                  stroke="#02457A"
                  stroke-width="3"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M50 50V87.5"
                  stroke="#02457A"
                  stroke-width="3"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M66.6668 66.6667L50.0002 50L33.3335 66.6667"
                  stroke="#02457A"
                  stroke-width="3"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </span>
          </label>
          <div class="upload__selectors">
            <label>
              <input
                type="radio"
                name="filetype"
                class="upload__selectors-radio--real"
              />
              <span class="upload__selectors-radio--custom"></span>
              <p class="upload__selectors-text">Лекция</p>
            </label>
            <label>
              <input
                type="radio"
                name="filetype"
                class="upload__selectors-radio--real"
              />
              <span class="upload__selectors-radio--custom"></span>
              <p class="upload__selectors-text">Задание</p>
            </label>
          </div>
          <button class="upload__btn">Добавить файл</button>
          
        </div>
        <div class="files__editor">
          <p class="editor__title title">Редактор задания</p>
          <div class="editor__form">
            <input
              placeholder="Название курса"
              type="text"
              class="editor__input"
            />
            <input placeholder="Тема" type="text" class="editor__input" />
            <div class="editor__files">
              <div class="editor__file">
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
                <p class="editor__file-name">Лекция</p>
                <a href="#" class="editor__file-delete">Удалить</a>
              </div>
              <div class="editor__file">
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
                <p class="editor__file-name">Лекция</p>
                <a href="#" class="editor__file-delete">Удалить</a>
              </div>
            </div>
            <button class="editor__btn">Отправить</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.aside {
  top: 0;
}
.title {
  font-size: 24px;
  line-height: 36px;
  margin-bottom: 12px;
  margin-left: 24px;
}
.fac {
  margin-top: 20px;
  padding-bottom: 12px;
  margin-bottom: 20px;
  padding-top: 12px;
  margin-left: 219px;
  background-color: #fff;
  border-radius: 12px;

  &__item-text {
    font-size: 16px;
    line-height: 24px;
  }
}
.fac__list {
  list-style: none;
  margin-left: 25px;
  &-item label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
}
.fac__item-radio--custom {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #000000;
  border-radius: 2px;
  position: relative;
  transition: 0.2s ease-in;
}
.fac__item-radio--custom::before {
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
.fac__item-radio--real:checked + .fac__item-radio--custom::before {
  transform: translate(-50%, -50%) scale(1);
}
.fac__item-radio--real:checked + .fac__item-radio--custom {
  border: 2px solid #02457a;
}
.fac__item-radio--real {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.selectors {
  margin-top: 20px;
  display: flex;
  &__course {
    margin-left: 219px;
    background-color: #fff;
    border-radius: 12px;
    padding-top: 12px;
    padding-bottom: 12px;
    padding-right: 25px;
    margin-bottom: 20px;
  }
  &__groups {
    margin-left: auto;
    background-color: #fff;
    border-radius: 12px;
    padding-top: 12px;
    padding-bottom: 12px;
    margin-bottom: 20px;
    width: 60%;
  }
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
.course__item-radio--real:checked + .course__item-radio--custom {
  border: 2px solid #02457a;
}
.course__item-radio--real {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.groups__list {
  list-style: none;
  margin-left: 25px;
  &-item label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
}
.groups__item-radio--custom {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #000000;
  border-radius: 2px;
  position: relative;
  transition: 0.2s ease-in;
}
.groups__item-radio--custom::before {
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
.groups__item-radio--real:checked + .groups__item-radio--custom::before {
  transform: translate(-50%, -50%) scale(1);
}
.groups__item-radio--real:checked + .groups__item-radio--custom {
  border: 2px solid #02457a;
}
.groups__item-radio--real {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.groups__paginate {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-right: 25px;
}
.groups__page {
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
.files {
  margin-left: 219px;
  display: flex;
  &__editor {
    background-color: #fff;
    border-radius: 12px;
    padding-top: 12px;
    padding-bottom: 20px;
    width: 70%;
  }
  &__upload {
    background-color: #fff;
    border-radius: 12px;
    padding-top: 20px;
    padding-bottom: 20px;
    margin-right: 24px;
  }
}
.editor {
  &__form {
    margin-left: 24px;
    display: flex;
    flex-direction: column;
  }
  &__input {
    border: 2px solid rgba(#000, 0.2);
    border-radius: 10px;
    padding-top: 13px;
    padding-bottom: 13px;
    padding-left: 20px;
    padding-right: 20px;
    margin-right: 24px;
    margin-bottom: 15px;
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    font-style: normal;
    &::placeholder {
      color: rgba(#000, 0.2);
      font-size: 20px;
      line-height: 30px;
      font-family: "Poppins", sans-serif;
      font-weight: 400;
      font-style: normal;
    }
  }
  &__files {
    margin-right: 24px;
    margin-bottom: 30px;
  }
  &__file {
    display: flex;
    align-items: center;
    & svg {
      margin-right: 10px;
    }
  }
  &__file-delete {
    width: 65px;
    margin-left: auto;
    font-size: 14px;
    line-height: 21px;
    color: #02457a;
  }
  &__btn {
    margin-right: 24px;
    
  }
}
.files__upload {
  display: flex;
  flex-direction: column;
  align-items: center;
}
input[type="file"] {
  position: absolute;
  z-index: -1;
  opacity: 0;
  display: block;
  width: 0;
  height: 0;
}
.upload {
  &__span {
    cursor: pointer;
    outline: none;
    position: relative;
    display: inline-block;
    border: 2px dashed #02457a;
    padding: 100px;
    margin-right: 24px;
    margin-left: 24px;
    margin-bottom: 20px;
  }
  &__selectors{
    margin-bottom: 50px;
    display: flex;
    gap: 30px;
    & label{
      display: flex;
      align-items: center;
    }
    & p{
      margin-left: 5px;
    }
  }
  &__btn {
    width: 90%;
    margin: 0 auto;
  }
}
.upload__selectors-radio--custom {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #000000;
  border-radius: 2px;
  position: relative;
  transition: 0.2s ease-in;
}
.upload__selectors-radio--custom::before {
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
.upload__selectors-radio--real:checked + .upload__selectors-radio--custom::before {
  transform: translate(-50%, -50%) scale(1);
}
.upload__selectors-radio--real:checked + .upload__selectors-radio--custom {
  border: 2px solid #02457a;
}
.upload__selectors-radio--real {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
</style>
<!-- <div class="files__upload">
  <label class="upload__label">
    <input type="file" class="upload__input" />
    <span class="upload__span"></span>
  </label>
  <button class="upload__btn">Добавить файл</button>
</div> -->
