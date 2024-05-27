<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();

const toId = ref(0);
const token = ref("");
const userName = ref("");
const userEmail = ref("");
const userPassword = ref("");
const studentGroup = ref(null);
const userGroup = ref()
const isProfessor = ref(false);
const isStudent = ref(false);
const userFac = ref(null);
const error = ref("");
const facilitiesList = ref([]);
const groupsList = ref([])

const getFac = async () => {
  try {
    const { data: facilities } = await axios.get("/api/Faa/");
    facilitiesList.value = facilities;
  } catch (err) {
    console.log(err);
  }
};
const getGroup = async () => {
  try {
    const { data: groups } = await axios.get("/api/Gro/");
    groupsList.value = groups;
  } catch (err) {
    console.log(err);
  }
};
// fields = ['email','first_name','type','faculty','fiGroup','password']

const postData = async () => {
  
  const formData = {
    first_name: `${userName.value}`,
    email: `${userEmail.value}`,
    type: `${isProfessor.value ? "Professor" : "Student"}`,
    password: `${userPassword.value}`,
    faculty: parseInt(userFac.value),
    fiGroup: studentGroup.value ? parseInt(studentGroup.value) : null
  };
  try {
    const { data } = await axios.post("api/register/", formData, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (err) {
    console.log(err);
  } finally {
    
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
      error.value = "Данный email уже занят :(";
    } finally {
      try {
        const { data } = await axios.get(
          `api/Usere/?email=${userEmail.value}`,
          {
            headers: {
              Authorization: `Token ${token.value}`,
              "Content-Type": "application/json",
            },
          }
        );
        toId.value = data[0].id;
      } catch (err) {
        console.log(err);
      } finally {
        if (error.value == "") {
          if (isProfessor.value) {
            router.push(`/profprofile/${toId.value}`);
          }
          if (isStudent.value) {
            router.push(`/studprofile/${toId.value}`);
          }
          localStorage.setItem("token", token.value);
        }
      }
    }
  }
};

onMounted(async () => {
  getFac();
  getGroup();
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
const onChangeGroup = (event) => {
  studentGroup.value = event.target.value;
  let sub = studentGroup.value.split(',')
  userGroup.value = sub[0]
  userFac.value = sub[1]
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
  } else if (isStudent.value && !studentGroup.value) {
    error.value = "Вы не ввели группу";
    return;
  } else if (isProfessor.value && !userFac.value) {
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
        <select
          @change="onChangeGroup"
          v-if="isStudent"
          class="registration__selector"
        >
          <option selected disabled value="1">Выберите группу</option>
          <option
            v-for="group in groupsList"
            :key="group.id"
            :value="[group.id,group.faculty]"
          >
            {{ group.name }}
          </option>
        </select>
        <select
          @change="onChangeFac"
          v-if="isProfessor"
          class="registration__selector"
        >
          <option selected disabled value="1">Выберите факультет</option>
          <option
            v-for="facil in facilitiesList"
            :key="facil.id"
            :value="facil.id"
          >
            {{ facil.name }}
          </option>
        </select>
        <!-- попробовать через онбефорроут, запрос по почте, вытаскиваем айди и роутим по айди -->
        <button @click="onClickSend()" class="registration__btn">
          Создать аккаунт
        </button>
        <router-link to="/login" class="registration__link"
          >Уже есть аккаунт? Войти</router-link
        >
        <p v-if="error.length > 0" class="registration__error">{{ error }}</p>
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
    color: #000;
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
