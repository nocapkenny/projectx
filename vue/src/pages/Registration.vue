<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();

const userName = ref("");
const userEmail = ref("");
const userPassword = ref("");
const studentGroup = ref("");
const isProfessor = ref(false);
const isStudent = ref(false);
const userFac = ref("1");
const error = ref("");
const facilitiesList = ref([]);
const toId = ref(0);

const getFac = async () => {
  try {
    const { data: facilities } = await axios.get("/api/Faa/");
    facilitiesList.value = facilities;
  } catch (err) {
    console.log(err);
  }
};
const postData = async () => {
  const objPrep = {
    name: userName.value,
    mail: userEmail.value,
    password: userPassword.value,
    type: "Professor",
    faculty: userFac.value,
  };
  const objStud = {
    name: userName.value,
    mail: userEmail.value,
    password: userPassword.value,
    type: "Student",
    group: studentGroup.value,
  };
  try {
    if (isProfessor.value) {
      const { data } = await axios.post("/api/Prepod/", objPrep);
    }
    if (isStudent.value) {
      const { data } = await axios.post("/api/Stud/", objStud);
    }
  } catch (err) {
    console.log(err);
  } finally {
    try {
      if (isProfessor.value) {
        const { data } = await axios.get(
          `/api/Prepode/?mail=${userEmail.value}`
        );
        toId.value = data[0].id;
      }
      if (isStudent.value) {
        const { data } = await axios.get(`/api/Stude/?mail=${userEmail.value}`);
        toId.value = data[0].id;
      }
      console.log(toId.value);
    } catch (err) {
      console.log(err);
    } finally {
      if (isProfessor.value) {
        router.push(`/profprofile/${toId.value}`);
      }
      if (isStudent.value) {
        router.push(`/studprofile/${toId.value}`);
      }
    }
  }
};

onMounted(async () => {
  getFac();
});

const onClickProfessor = () => {
  isProfessor.value = true;
  isStudent.value = false;
};
const onClickStudent = () => {
  isStudent.value = true;
  isProfessor.value = false;
};
const onChangeFac = (event) => {
  userFac.value = event.target.value;
};
const onClickSend = async () => {
  if (userName.value.length === 0) {
    error.value = "Вы не ввели имя";
    return;
  } else if (userEmail.value.length === 0) {
    error.value = "Вы не ввели почту";
    return;
  } else if (userPassword.value.length === 0) {
    error.value = "Вы не ввели пароль";
    return;
  } else if (!isProfessor.value && !isStudent.value) {
    error.value = "Вы не выбрали статус";
    return;
  } else if (isStudent.value && studentGroup.value.length == 0) {
    error.value = "Вы не ввели группу";
    return;
  } else if (isProfessor.value && userFac.value == "1") {
    error.value = "Вы не выбрали факультет";
    return;
  }
  error.value = "";
  postData();
};
</script>

<template>
  <div class="registration">
    <input
      v-model="userName"
      class="registration__input"
      type="name"
      placeholder="Фамилия Имя"
    />
    <input
      v-model="userEmail"
      class="registration__input"
      type="email"
      placeholder="Email"
    />
    <input
      v-model="userPassword"
      class="registration__input"
      type="password"
      placeholder="Пароль"
    />
    <div class="registration__btns">
      <button
        @click="onClickStudent"
        :class="
          isStudent
            ? 'registration__select registration__select--active'
            : 'registration__select'
        "
      >
        Студент
      </button>
      <button
        @click="onClickProfessor"
        :class="
          isProfessor
            ? 'registration__select registration__select--active'
            : 'registration__select'
        "
      >
        Преподаватель
      </button>
    </div>
    <input
      v-model="studentGroup"
      v-if="isStudent"
      class="registration__input"
      type="text"
      placeholder="Группа"
    />
    <select
      @change="onChangeFac"
      v-if="isProfessor"
      class="registration__selector"
    >
      <option selected disabled value="1">Выберите факультет</option>
      <option
        v-for="facil in facilitiesList"
        :key="facil.id"
        :value="facil.name"
      >
        {{ facil.name }}
      </option>
    </select>
    <!-- попробовать через онбефорроут, запрос по почте, вытаскиваем айди и роутим по айди -->
    <button @click="onClickSend()" class="registration__btn">Отправить</button>

    <p class="registration__error">{{ error }}</p>
  </div>
</template>

<style lang="scss" scoped>
.registration {
  padding: 39px 93px;
  background-color: #fff;
  max-width: 546px;
  border-radius: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 17px;

  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  &__input {
    background-color: rgba(231, 231, 231, 0.83);
    outline: none;
    border: none;
    width: 360px;
    padding-left: 40px;
    border-radius: 20px;
    color: #000;
    font-size: 24px;
    padding-top: 10px;
    padding-bottom: 10px;
    line-height: 36px;
    font-family: "Oswald", sans-serif;
    font-optical-sizing: auto;
    font-weight: 400;
    &::placeholder {
      color: #000;
      font-family: "Oswald", sans-serif;
      font-optical-sizing: auto;
      font-weight: 400;
    }
  }
  &__btns {
    display: flex;
    width: 360px;
    justify-content: space-between;
  }
  &__select {
    background-color: rgba(231, 231, 231, 0.83);
    outline: none;
    border: none;
    border-radius: 20px;
    font-size: 24px;
    line-height: 36px;
    padding: 10px 0;
    width: 46%;
    cursor: pointer;
    &--active {
      background-color: #4b5873;
      color: #fff;
    }
  }
  &__selector {
    font-family: "Oswald", sans-serif;
    font-optical-sizing: auto;
    font-weight: 400;
    background-color: rgba(231, 231, 231, 0.83);
    outline: none;
    border: none;
    width: 360px;
    font-size: 24px;
    line-height: 36;
    border-radius: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 10px;
  }

  &__btn {
    background-color: #4b5873;
    color: #fff;
    padding: 10px 27px;
    font-size: 24px;
    line-height: 36px;
    border-radius: 20px;
    border: none;
    cursor: pointer;
    transition: transform 0.3s;
    &:active {
      transform: translateY(8px);
    }
  }
  &__error {
    color: rgb(236, 83, 83);
  }
}
</style>
