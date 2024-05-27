<script setup>
import { ref } from "vue";
import axios from 'axios'
import { useRouter } from "vue-router";

const router = useRouter();

const userEmail = ref("");
const userPassword = ref("");
const error = ref("");
const token = ref("")
const isProfessor = ref(false)
const isStudent = ref(false)
const toId = ref(0)

const login = async () => {
  const loginData = {
    username: `${userEmail.value}`,
    password: `${userPassword.value}`,
  };
  try {
    const { data } = await axios.post("api/login/", loginData, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    token.value = data.token;
  } catch (err) {
    console.log(err);
    error.value = "Неверный email или пароль :("
  } finally {
    try {
      const { data } = await axios.get(`api/Usere/?email=${userEmail.value}`, {
        headers: {
          Authorization: `Token ${token.value}`,
          "Content-Type": "application/json",
        },
      });
      toId.value = data[0].id;
      if (data[0].type == "Student"){
        isStudent.value = true
      }
      if (data[0].type == "Professor"){
        isProfessor.value = true
      }
    } catch (err) {
      console.log(err);
    } finally {
      if (isProfessor.value) {
        router.push(`/profprofile/${toId.value}`);
      }
      if (isStudent.value) {
        router.push(`/studprofile/${toId.value}`);
      }
      localStorage.setItem("token", token.value);
    }
  }
};

const onClickSend = () => {
  if (userEmail.value.length < 3) {
    error.value = "Вы не ввели почту";
    return;
  } else if (userPassword.value.length == 0) {
    error.value = "Вы не ввели пароль";
    return;
  }

  error.value = "";

  login();
};
</script>

<template>
  <div class="wrapper">
    <div class="login">
      <div class="login__box">
        <h1 class="login__title">Вход</h1>
        <input
          v-model="userEmail"
          class="login__input"
          type="email"
          placeholder="Email"
        />
        <input
          v-model="userPassword"
          class="login__input"
          type="password"
          placeholder="Пароль"
        />
        <button @click="onClickSend()" class="login__btn">Войти</button>
        <router-link to="/" class="login__link"
          >Ещё нет аккаунта? Регистрация</router-link
        >
        <p v-if="error.length > 0" class="login__error">{{ error }}</p>
      </div>
      <div class="login__aside"></div>
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
.login {
  max-width: 996px;
  display: flex;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  &__link {
    padding: 0;
    margin: 0;
    text-align: center;
    color: #02457a;
  }
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
