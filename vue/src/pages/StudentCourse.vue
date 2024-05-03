<script setup>
import Sidebar from "@/components/Sidebar.vue";
import StudCourseFiles from "@/components/StudCourseFiles.vue";
import axios from "axios";
import { onMounted, ref, watch, computed } from "vue";
import { useRoute } from "vue-router";

const router = useRoute();
const currentPage = ref(1);
const currentPageLessons = ref(1)
const perPage = ref(2);
const file = ref();
const displayedFiles = ref();
const lesson = ref();
const stud = ref();
const topic = ref("");
const isFetched = ref(false);
const isPending = ref(false);

// const onClickHandler = (page) => {
//   console.log(page);
// };

const getFiles = async () => {
  try {
    isPending.value = true;
    const { data } = await axios.get(
      `/api/Teoriae/?predmet=${lesson.value}&group=${stud.value.group}`
    );
    file.value = data;
  } catch (err) {
    console.log(err);
  } finally {
    isPending.value = false;
    if (file.value.length != 0) {
      isFetched.value = true;
    }
    currentPage.value = 1;
    displayedFiles.value = file.value.slice(0, 2)
  }
};
const clickPage = () =>{
  let startIndex = currentPage.value * perPage.value - perPage.value;
  let endIndex = startIndex + perPage.value;
  displayedFiles.value = file.value.slice(startIndex, endIndex);
  console.log(displayedFiles.value)
}

const onClickLesson = async (event) => {
  lesson.value = event.target.value;
  try {
    const { data } = await axios.get(`/api/Stud/${router.params.userId}`);
    stud.value = data;
  } catch (err) {
    console.log(err);
  } finally {
    getFiles();
  }
};
const clearFiles = () => {
  isFetched.value = false;
};

watch(lesson, clearFiles);
</script>

<template>
  <div class="container">
    <Sidebar :userId="$route.params.userId" :path="$route.path" />
    <div class="course__inner stud">
      <div class="firstcol">
        <h3 class="course__title stud">Выберите предмет</h3>
        <ul class="course__list stud">
          <li class="course__list-item stud">
            <label @change="onClickLesson">
              <input
                type="radio"
                name="lesson"
                class="course__item-radio--real stud"
                value="Языки программирования"
              />
              <span class="course__item-radio--custom stud"></span>
              <p class="course__item-text stud">Языки программирования</p>
            </label>
          </li>
          <li class="course__list-item stud">
            <label @change="onClickLesson">
              <input
                type="radio"
                name="lesson"
                class="course__item-radio--real stud"
                value="Аналитическая геометрия"
              />
              <span class="course__item-radio--custom stud"></span>
              <p class="course__item-text stud">Аналитическая геометрия</p>
            </label>
          </li>
          <li class="course__list-item stud">
            <label @change="onClickLesson">
              <input
                type="radio"
                name="lesson"
                class="course__item-radio--real stud"
                value="Алгоритмы и структуры данных"
              />
              <span class="course__item-radio--custom stud"></span>
              <p class="course__item-text stud">Алгоритмы и структуры данных</p>
            </label>
          </li>
        </ul>
        
        <vue-awesome-paginate
          :total-items="12"
          v-model="currentPageLessons"
          :items-per-page="4"
          :max-pages-shown="6"
          pagination-container-class="course__lessons-list"
        />
      </div>
      <div v-if="isFetched" class="secondcol">
        <StudCourseFiles
          v-for="item in displayedFiles"
          :key="file.tema"
          :id="item.id"
          :type="item.type"
          :topic="item.tema"
        />
        <vue-awesome-paginate
          :total-items="file.length"
          v-model="currentPage"
          :items-per-page="perPage"
          :max-pages-shown="6"
          :on-click="clickPage"
        />
      </div>

      <div v-if="!isFetched && !isPending" class="notfound">
        <p class="notfound__text">Ничего не найдено 😔</p>
      </div>
      <div v-if="isPending" class="notfound">
        <p class="notfound__text">Загрузка 👀</p>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.course__lessons-list{
  display: flex !important;
  justify-content: flex-end;
  gap: 10px;
  margin-right: 25px;
}
.notfound {
  margin-top: 30px;
  background-color: #fff;
  width: 1032px;
  height: 308px;
  border-radius: 20px;
  &__text {
    text-align: center;
    font-size: 24px;
    margin-top: 120px;
  }
}
.secondcol {
  margin-bottom: 30px;
}
.course__inner.stud {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 219px;
}
.course__title.stud {
  margin-left: 25px;
  margin-top: 15px;
  font-size: 24px;
  line-height: 36px;
  margin-bottom: 20px;
  font-weight: 400;
}
.course__list.stud {
  list-style: none;
  margin-left: 25px;
  // &-item label {
  //   display: flex;
  //   align-items: center;
  //   gap: 10px;
  //   margin-bottom: 10px;
  // }
}
.course__list-item.stud label {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
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
.course__item-text.stud {
  font-size: 20px;
  line-height: 30px;
}
.pagination-container {
  display: flex !important;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}
.paginate-buttons {
  font-size: 14px;
  line-height: 17px;
  color: rgba(#000, 0.2);
  background-color: transparent;
  border: none;
  padding-top: 5px;
  padding-bottom: 5px;
  padding-left: 10px;
  padding-right: 10px;
}
.paginate-buttons:hover {
  border-radius: 4px;
  color: rgba(#000, 0.2);
  background-color: rgba(#0000000d, 0.05);
  border: none;
}
.active-page {
  background-color: #02457a;
  color: #fff;
  border-radius: 4px;
  &:hover {
    background-color: #02457a;
    color: #fff;
    border-radius: 4px;
  }
}
</style>
