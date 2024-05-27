<script setup>
import Sidebar from "@/components/Sidebar.vue";
import Lessons from "@/components/LessonsStud.vue";
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
const token = localStorage.getItem("token");
const lessonsId = ref();
const router = useRoute();
const lesson = ref();
const lessonId = ref()
const marks = ref([])
const summ = ref(0)
const kt1 = ref(0)
const kt2 = ref(0)
const kt3 = ref(0)
const kt4 = ref(0)

const getData = async () => {
  try {
    const { data } = await axios.get(`/api/User/${router.params.userId}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    lessonsId.value = data.mark_table;
  } catch (err) {
    console.log(err);
  } 
};

const onClickLesson = (event) => {
  lesson.value = event.target.value;
  let sub = lesson.value.split(",")
  lessonId.value = sub[1]
  getMarks()
};
 
const getMarks = async () => {
  try{
    const { data } = await axios.get(`/api/Osenki/${lessonId.value}`, {
      headers:{
        Authorization: `Token ${token}`
      }
    })
    marks.value = data
    kt1.value = data.kt1
    kt2.value = data.kt2
    kt3.value = data.kt3
    kt4.value = data.kt4
    summ.value = kt1.value + kt2.value + kt3.value + kt4.value
  } catch(err){
    console.log(err)
  }
}

onMounted(() => {
  getData();
});
</script>

<template>
  <div class="container">
    <Sidebar :userId="$route.params.userId" :path="$route.path" />
    <div class="marks__inner">
      <div class="firstcol marks">
        <h3 class="marks__title">Выберите предмет</h3>
        <ul v-auto-animate class="marks__list">
          <Lessons
            v-for="lessonId in lessonsId"
            :id="lessonId"
            :on-click-lesson="onClickLesson"
          />
        </ul>
      </div>
      <div class="secondcol">
        <div class="marks__table">
          <div class="marks__table-headers">
            <p class="marks__table-header">КТ</p>
            <p class="marks__table-header">Проходной</p>
            <p class="marks__table-header">Оценка</p>
            <p class="marks__table-header">Максимум</p>
            <p class="marks__table-header">Дата</p>
          </div>
          <div class="marks__table-inner">
            <div class="marks__table-control">
              <p class="marks__table-text marks__table-text--firstunderline">
                КТ1
              </p>
              <p class="marks__table-text">КТ2</p>
              <p class="marks__table-text">КТ3</p>
              <p class="marks__table-text">КТ4</p>
              <p class="marks__table-text">Итог</p>
            </div>
            <div class="marks__table-minpoints">
              <p class="marks__table-text marks__table-text--secondunderline">
                13
              </p>
              <p class="marks__table-text">13</p>
              <p class="marks__table-text">5</p>
              <p class="marks__table-text">17</p>
              <p class="marks__table-text">41</p>
            </div>
            <div v-auto-animate  class="marks__table-points">
              <p class="marks__table-text marks__table-text--thirdunderline">
                {{ kt1 }}
              </p>
              <p class="marks__table-text">{{ kt2 }}</p>
              <p class="marks__table-text">{{ kt3 }}</p>
              <p class="marks__table-text">{{ kt4 }}</p>
              <p class="marks__table-text">{{ summ }}</p>
            </div>
            <div class="marks__table-maxpoints">
              <p class="marks__table-text marks__table-text--fourthunderline">
                30
              </p>
              <p class="marks__table-text">20</p>
              <p class="marks__table-text">10</p>
              <p class="marks__table-text">40</p>
              <p class="marks__table-text">100</p>
            </div>
            <div class="marks__table-date">
              <p class="marks__table-text marks__table-text--fifthtunderline">
                01.04.2024
              </p>
              <p class="marks__table-text">01.04.2024</p>
              <p class="marks__table-text">01.04.2024</p>
              <p class="marks__table-text">01.04.2024</p>
              <p class="marks__table-text">01.04.2024</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.firstcol.marks {
  height: auto;
  padding-bottom: 15px;
}
.marks__inner {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 210px;
}
.marks__title {
  font-size: 24px;
  line-height: 36px;
  margin-left: 25px;
  font-weight: 400;
  margin-top: 15px;
  margin-bottom: 20px;
}
.marks__list {
  margin-left: 24px;
  list-style: none;
  &-item label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
}
.marks__item-text {
  font-size: 20px;
  line-height: 30px;
}
.marks__item-radio--custom {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #000000;
  border-radius: 2px;
  position: relative;
  transition: 0.2s ease-in;
}
.marks__item-radio--custom::before {
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
.marks__item-radio--real:checked + .marks__item-radio--custom::before {
  transform: translate(-50%, -50%) scale(1);
}
.marks__item-radio--real:checked + .marks__item-radio--custom {
  border: 2px solid #02457a;
}
.marks__item-radio--real {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.marks__paginate {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-right: 25px;
}
.marks__page {
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
.marks__table {
  padding-bottom: 30px;
  &-headers {
    display: flex;
    gap: 50px;
    padding: 16px 24px;
    background-color: #02457a;
    border-radius: 12px;
    margin-top: 24px;
    margin-right: 20px;
    margin-left: 20px;
    justify-content: space-between;
  }
  &-header {
    color: #fff;
    font-size: 20px;
    line-height: 24px;
    font-weight: 600;
  }
  &-inner {
    display: flex;
  }
  &-text {
    font-size: 20px;
    line-height: 24px;
    padding-top: 12px;
    padding-bottom: 12px;
    &--firstunderline {
      position: relative;
      &::before {
        content: "";
        position: absolute;
        bottom: 0;
        left: -25px;
        height: 1px;
        width: 992px;
        background-color: rgba(#000, 0.1);
      }
    }
    &--secondunderline {
      position: relative;
      &::before {
        content: "";
        position: absolute;
        bottom: -48px;
        left: -235px;
        height: 1px;
        width: 992px;
        background-color: rgba(#000, 0.1);
      }
    }
    &--thirdunderline {
      position: relative;
      &::before {
        content: "";
        position: absolute;
        bottom: -96px;
        left: -475px;
        height: 1px;
        width: 992px;
        background-color: rgba(#000, 0.1);
      }
    }
    &--fourthunderline {
      position: relative;
      &::before {
        content: "";
        position: absolute;
        bottom: -144px;
        left: -700px;
        height: 1px;
        width: 992px;
        background-color: rgba(#000, 0.1);
      }
    }
    &--fifthtunderline {
      position: relative;
      &::before {
        content: "";
        position: absolute;
        bottom: -192px;
        left: -860px;
        height: 1px;
        width: 992px;
        background-color: rgba(#000, 0.1);
      }
    }
  }
}
.marks__table-minpoints {
  margin-left: 170px !important;
}
.marks__table-points {
  margin-left: 220px !important;
}
.marks__table-maxpoints {
  margin-left: 200px !important;
}
.marks__table-date {
  margin-left: 130px !important;
}
.marks__table-control,
.marks__table-minpoints,
.marks__table-points,
.marks__table-maxpoints,
.marks__table-date {
  margin-left: 48px;
}
</style>
