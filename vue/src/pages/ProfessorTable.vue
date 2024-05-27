<script setup>
import { onMounted, ref, watch } from "vue";
import Sidebar from "../components/Sidebar.vue";
import Faculties from "@/components/Faculties.vue";
import Groups from "@/components/GroupsStud.vue";
import TableItem from "@/components/TableItem.vue";
import axios from "axios";
const facs = ref();
const fac = ref();
const facId = ref();
const isPending = ref(false);
const groups = ref();
const group = ref();
const groupId = ref();
const isGroupsLoad = ref(false);
const currentPage = ref(1);
const perPage = ref(4);
const displayedGroups = ref();
const students = ref();
const lesson = ref("");
const isGroupAdded = ref(false);
const isDone = ref(false);
const error = ref("");
const lessons = ref([
  "Математический анализ",
  "Дискретная математика",
  "Аналитическая геометрия",
  "Языки программирования",
  "Линейная лгебра",
  "Алгоритмы и структуры данных",
  "История России",
]);

const token = localStorage.getItem("token");

const getFacs = async () => {
  try {
    const { data } = await axios.get(`/api/Faa/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    facs.value = data;
  } catch (err) {
    console.log(err);
  }
};

const clickPage = () => {
  let startIndex = currentPage.value * perPage.value - perPage.value;
  let endIndex = startIndex + perPage.value;
  displayedGroups.value = groups.value.slice(startIndex, endIndex);
};

const getGroups = async () => {
  try {
    const { data } = await axios.get(`/api/Faae/?name=${fac.value}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    facId.value = data[0].id;
    isPending.value = true;
  } catch (err) {
    console.log(err);
  } finally {
    try {
      const { data } = await axios.get(`/api/Groe/?faculty=${facId.value}`, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      groups.value = data;
    } catch (err) {
      console.log(err);
    } finally {
      isPending.value = false;
      isGroupsLoad.value = true;
      clickPage();
    }
  }
};


const getStudents = async () => {
  try {
    const { data } = await axios.get(`/api/Usere/?fiGroup=${groupId.value}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    students.value = data;
  } catch (err) {
    console.log(err);
  } finally {
    isDone.value = true;
  }
};

const onClickFac = (event) => {
  fac.value = event.target.value;
};
const onClickGroup = (event) => {
  group.value = event.target.value;
  if (group.value) {
    let sub = group.value.split(",");
    groupId.value = sub[1];
    isGroupAdded.value = true;
  }
};

watch(fac, getGroups);
watch(lesson, getStudents)
onMounted(() => {
  getFacs();
});
</script>

<template>
  <div class="container">
    <Sidebar class="aside" :userId="$route.params.userId" :path="$route.path" />
    <div class="fac">
      <p class="fac__title title">Выберите факультет</p>
      <ul v-auto-animate class="fac__list">
        <Faculties
          v-for="fac in facs"
          :on-click-fac="onClickFac"
          :name="fac.name"
        />
      </ul>
    </div>
    <div class="selectors">
      <div v-auto-animate class="selectors__groups">
        <p v-if="isGroupsLoad" class="groups__title title">Выберите группу</p>
        <ul v-if="isGroupsLoad" class="groups__list">
          <div v-auto-animate>
            <Groups
              v-for="item in displayedGroups"
              :id="item.id"
              :name="item.name"
              :on-click-group="onClickGroup"
            />
          </div>
          <vue-awesome-paginate
            :total-items="isGroupsLoad ? groups.length : 0"
            v-model="currentPage"
            :items-per-page="perPage"
            :max-pages-shown="6"
            :on-click="clickPage"
          />
        </ul>
        <div v-if="!isGroupsLoad && !isPending" class="groups__notfound">
          <p class="groups__notfound-text">Ничего не найдено 😔</p>
        </div>
        <div v-if="isPending" class="groups__notfound">
          <p class="groups__notfound-text">Загрузка 👀</p>
        </div>
      </div>
    </div>
    <div v-auto-animate class="lesson">
      <p v-if="isGroupAdded" class="lesson__title title">Выберите курс</p>
      <!-- <input
        v-if="isGroupAdded"
        v-model="lesson"
        type="text"
        class="lesson__input"
      /> -->
      <select
        v-model="lesson"
        v-if="isGroupAdded"
        class="lesson__input"
        name="lessons"
      >
        <option selected disabled value="1">Выберите курс</option>
        <option v-for="item in lessons" :value="item">{{ item }}</option>
      </select>
      <p class="lesson__error">{{ error }}</p>
      <div v-if="!isGroupAdded" class="groups__notfound">
        <p class="groups__notfound-text">Ничего не найдено 😔</p>
      </div>
    </div>
    <div class="table">
      <div v-if="isDone" class="table__headers">
        <p class="table__header table__header--name">Фамилия/Имя</p>
        <p class="table__header">КТ1</p>
        <p class="table__header">КТ2</p>
        <p class="table__header">КТ3</p>
        <p class="table__header">КТ4</p>
        <p class="table__header">ИТОГ</p>
        <p class="table__header">Сохранить</p>
      </div>
      <div v-auto-animate class="table__inner">
        <TableItem
          v-for="student in students"
          :lesson="lesson"
          :marksId="student.mark_table"
          :name="student.first_name"
        />
      </div>
      <div v-if="!isDone" class="groups__notfound">
        <p class="groups__notfound-text">Ничего не найдено 😔</p>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.container {
  padding-bottom: 30px;
}
.aside {
  top: 0;
}
.lesson {
  margin-left: 219px;
  background-color: #fff;
  border-radius: 12px;
  padding-bottom: 15px;
  padding-top: 10px;
  margin-bottom: 25px;
  text-align: center;
  &__input {
    margin-left: 25px;
    border: 2px solid rgba(#00000033, 0.2);
    border-radius: 10px;
    padding-left: 20px;
    padding-top: 13px;
    padding-bottom: 13px;
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    font-size: 20px;
    line-height: 30px;
    outline: none;
    transition: all ease 0.3s;
    color: rgba(#00000033, 0.2);
    width: 500px;
    margin-bottom: 10px;
    &:focus {
      border: 2px solid #02457a;
      color: #02457a;
    }
  }
  &__btn {
    display: block;
    width: 150px;
    font-size: 16px;
    padding-top: 5px;
    padding-bottom: 5px;
    margin: 0 auto;
  }
  &__error {
    color: rgb(236, 83, 83);
    text-align: center;
    margin-top: 10px;
  }
}
.table {
  margin-left: 219px;
  padding-left: 25px;
  padding-right: 25px;
  padding-top: 25px;
  padding-bottom: 20px;
  background-color: #fff;
  border-radius: 12px;
  padding-bottom: 30px;
  &__headers {
    display: flex;
    justify-content: space-between;
    padding-top: 16px;
    padding-left: 24px;
    padding-bottom: 16px;
    padding-right: 24px;
    color: #fff;
    background-color: #02457a;
    border-radius: 12px;
  }
  &__inner {
    display: grid;
    grid-template-rows: repeat(auto, 1fr);
  }
  &__item {
    display: flex;
    justify-content: space-between;
    padding-top: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(#000000, 0.1);
  }
  &__item-name {
    width: 200px;
    padding-left: 24px;
  }
  &__item-sum {
    padding-right: 60px;
    font-size: 18px;
    line-height: 20px;
    padding-top: 4px;
  }
  &__item-point {
    border: none;
    color: #000;
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    font-size: 18px;
    line-height: 20px;
    width: 30px;
    outline: none;
    margin-left: 15px;
    padding: 0;
    &::placeholder {
      color: #000;
      font-family: "Poppins", sans-serif;
      font-weight: 400;
    }
    &--first {
      margin-left: 40px;
    }
    &--last {
      margin-right: 15px;
    }
  }
}
.table__header--name {
  width: 200px;
}
.table__paginate {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}
.table__page {
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
  &__groups {
    margin-left: auto;
    background-color: #fff;
    border-radius: 12px;
    padding-top: 12px;
    padding-bottom: 12px;
    margin-bottom: 20px;
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
</style>
