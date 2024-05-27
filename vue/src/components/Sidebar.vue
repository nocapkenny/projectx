<script setup>
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const token = localStorage.getItem("token");

const props = defineProps({
  userId: String,
  path: String,
});



const logout = async () => {
  try {
    const { data } = await axios.get("api/logout/", {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
  } catch (err) {
    console.log(err);
  } finally {
    localStorage.removeItem("token");
    router.push("/");
  }
};
</script>

<template>
  <div class="sidebar">
    <div class="sidebar__inner">
      <h1 class="sidebar__title">BASH2.0</h1>
      <router-link
        :to="
          $route.path == `/profprofile/${props.userId}` ||
          $route.path == `/makecourse/${props.userId}` ||
          $route.path == `/table/${props.userId}`
            ? `/profprofile/${props.userId}`
            : $route.path == `/studprofile/${props.userId}` ||
                $route.path == `/marks/${props.userId}` ||
                $route.path == `/courses/${props.userId}`
              ? `/studprofile/${props.userId}`
              : `/404`
        "
        :class="
          $route.path == `/studprofile/${props.userId}` ||
          $route.path == `/profprofile/${props.userId}`
            ? 'sidebar__link sidebar__link--first sidebar__link--active'
            : 'sidebar__link sidebar__link--first'
        "
        >Профиль</router-link
      >
      <router-link
        v-if="
          $route.path == `/profprofile/${props.userId}` ||
          $route.path == `/makecourse/${props.userId}` ||
          $route.path == `/table/${props.userId}`
        "
        :to="`/table/${props.userId}`"
        :class="
          $route.path == `/table/${props.userId}`
            ? 'sidebar__link sidebar__link--second sidebar__link--active'
            : 'sidebar__link sidebar__link--second'
        "
        >Зачетная таблица</router-link
      >
      <router-link
        v-if="
          $route.path == `/profprofile/${props.userId}` ||
          $route.path == `/makecourse/${props.userId}` ||
          $route.path == `/table/${props.userId}`
        "
        :to="`/makecourse/${props.userId}`"
        :class="
          $route.path == `/makecourse/${props.userId}`
            ? 'sidebar__link sidebar__link--third sidebar__link--active'
            : 'sidebar__link sidebar__link--third'
        "
        >Редактор курса</router-link
      >
      <router-link
        v-if="
          $route.path == `/studprofile/${props.userId}` ||
          $route.path == `/marks/${props.userId}` ||
          $route.path == `/courses/${props.userId}`
        "
        :to="`/courses/${props.userId}`"
        :class="
          $route.path == `/courses/${props.userId}`
            ? 'sidebar__link sidebar__link--fourth sidebar__link--active'
            : 'sidebar__link sidebar__link--fourth'
        "
        >Курсы</router-link
      >
      <router-link
        v-if="
          $route.path == `/studprofile/${props.userId}` ||
          $route.path == `/marks/${props.userId}` ||
          $route.path == `/courses/${props.userId}`
        "
        :to="`/marks/${props.userId}`"
        :class="
          $route.path == `/marks/${props.userId}`
            ? 'sidebar__link sidebar__link--fifth sidebar__link--active'
            : 'sidebar__link sidebar__link--fifth'
        "
        >Мои оценки</router-link
      >
      <p @click="logout" class="sidebar__logout">Выйти</p>
      <a href="mailto:zxsage@yandex.ru" class="sidebar__email">Написать нам: zxsage@yandex.ru</a>
      
    </div>
  </div>
</template>

<style scoped lang="scss">
.sidebar {
  background: linear-gradient(330.44deg, #97cadb 1.3%, #02457a 76.94%);
  width: 280px;
  height: 100vh;
  position: fixed;
  border-top-right-radius: 40px;
  border-bottom-right-radius: 40px;
  left: 0;
  &__email{
    font-size: 14px;
    line-height: 24px;
    color: #fff;
    color: rgba(#fff, 0.7);
    &:hover {
      color: #fff;
    }
  }
  &__inner {
    display: flex;
    flex-direction: column;
    gap: 30px;
    margin-left: 20px;
    margin-top: 50px;
  }
  &__title {
    font-family: "Oswald", sans-serif;
    font-optical-sizing: auto;
    font-weight: 700;
    font-style: normal;
    font-size: 36px;
    line-height: 53px;
    color: #fff;
    margin-bottom: 50px;
  }
  &__link {
    font-size: 20px;
    line-height: 30px;
    color: rgba(#fff, 0.7);
    width: 220px;
    padding-top: 20px;
    padding-bottom: 20px;
    padding-left: 45px;
    position: relative;
    &--active {
      color: #fff;
      border-radius: 10px;
      background-color: rgba(#fff, 0.05);
    }
    &:hover {
      color: #fff;
      border-radius: 10px;
      background-color: rgba(#fff, 0.05);
    }
    &--first::after {
      content: "";
      position: absolute;
      left: 10px;
      top: 22px;
      background-image: url(../assets/user.svg);
      background-repeat: no-repeat;
      background-size: cover;
      width: 24px;
      height: 24px;
    }
    &--second::after {
      content: "";
      position: absolute;
      left: 10px;
      top: 22px;
      background-image: url(../assets/tableprof.svg);
      background-repeat: no-repeat;
      background-size: cover;
      width: 24px;
      height: 24px;
    }
    &--third::after {
      content: "";
      position: absolute;
      left: 10px;
      top: 22px;
      background-image: url(../assets/makecourse.svg);
      background-repeat: no-repeat;
      background-size: cover;
      width: 24px;
      height: 24px;
    }
    &--fourth::after {
      content: "";
      position: absolute;
      left: 10px;
      top: 22px;
      background-image: url(../assets/makecourse.svg);
      background-repeat: no-repeat;
      background-size: cover;
      width: 24px;
      height: 24px;
    }
    &--fifth::after {
      content: "";
      position: absolute;
      left: 10px;
      top: 22px;
      background-image: url(../assets/marks.svg);
      background-repeat: no-repeat;
      background-size: cover;
      width: 24px;
      height: 24px;
    }
  }
  &__logout {
    cursor: pointer;
    font-size: 20px;
    line-height: 30px;
    color: rgba(#fff, 0.7);
    width: 220px;
    padding-top: 20px;
    padding-bottom: 20px;
    position: relative;
    padding-left: 45px;
    &:hover {
      color: #fff;
      border-radius: 10px;
      background-color: rgba(#fff, 0.05);
    }
    &::after {
      content: "";
      position: absolute;
      left: 10px;
      top: 26px;
      background-image: url(../assets/log-out.svg);
      transform: rotate(180deg);
      background-repeat: no-repeat;
      background-size: cover;
      width: 20px;
      height: 20px;
    }
  }
}
</style>
