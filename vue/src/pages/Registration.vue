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
  <div class="wrapper">
    <div class="registration">
      <div class="registration__box">
        <h1 class="registration__title">Регистрация</h1>
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
        <button @click="onClickSend()" class="registration__btn">
          Создать аккаунт
        </button>

        <p class="registration__error">{{ error }}</p>
      </div>
      <div class="registration__aside"></div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrapper {
  background-image: url(../assets/bg.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
.registration {
  max-width: 996px;
  display: flex;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  &__aside {
    background: linear-gradient(322.19deg, #97cadb 0%, #02457a 91.3%);
    width: 384px;
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
  }
  &__box {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding-left: 60px;
    padding-right: 60px;
    padding-top: 52px;
    padding-bottom: 52px;
  }
  &__title {
    font-weight: 700;
    font-size: 40px;
    line-height: 60px;
    color: #02457a;
  }
  &__input {
    border: 2px solid rgba(#00000033, 0.2);
    border-radius: 10px;
    padding-left: 20px;
    padding-top: 13px;
    padding-bottom: 13px;
    font-family: "Poppins", sans-serif;
    width: 492px;
    font-weight: 400;
    font-size: 20px;
    line-height: 30px;
    outline: none;
    transition: all ease 0.3s;
    &::placeholder {
      color: rgba(#00000033, 0.2);
      font-family: "Poppins", sans-serif;
      font-weight: 400;
      font-size: 20px;
      line-height: 30px;
    }
    &:focus {
      border: 2px solid #02457a;
    }
    &:focus::placeholder {
      color: #02457a;
    }
  }
  &__btns {
    display: flex;
    width: 492px;
    justify-content: space-between;
  }
  &__select {
    background-color: transparent;
    outline: none;
    border: none;
    border-radius: 10px;
    font-size: 20px;
    line-height: 30px;
    padding: 10px 0;
    width: 46%;
    cursor: pointer;
    transition: all ease 0.3s;
    &--active {
      background-color: #02457a;
      color: #fff;
    }
    &--active:hover {
      background-color: #02457a !important;
      color: #fff !important;
    }
    &:hover {
      background-color: rgba(#00000033, 0.2);
      color: black;
    }
  }
  &__selector {
    font-family: "Poppins", sans-serif;
    font-weight: 400;
    border: 2px solid rgba(#00000033, 0.2);
    color: rgba(#00000033, 0.2);
    cursor: pointer;
    outline: none;
    width: 492px;
    font-size: 20px;
    line-height: 30px;
    border-radius: 10px;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 10px;
    transition: all ease 0.3s;
    &:focus {
      border: 2px solid #02457a;
      color: #02457a;
    }
  }

  &__btn {
    background-color: #02457a;
    color: #fff;
    padding: 10px 27px;
    font-size: 20px;
    line-height: 30px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: all ease 0.3s;
    border: 2px solid #02457a;
    &:active {
      transform: translateY(8px);
    }
    &:hover {
      background-color: #fff;

      color: #02457a;
    }
  }
  &__error {
    color: rgb(236, 83, 83);
    text-align: center;
  }
}
</style>
