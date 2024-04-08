<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
const props = defineProps({
  userId: String,
});

const user = ref([]);

const getData = async () => {
  const { data } = await axios.get(`/api/Prepod/${props.userId}`);
  user.value = data;
};

onMounted(() => {
  getData();
});
</script>

<template>
  <div class="sidebar">
    <div class="sidebar__info">
      <div class="sidebar__info-pic"></div>
      <p class="sidebar__info-name">
        {{ user.name }}
      </p>
    </div>
    <router-link
      :to="
        $route.path == `/profprofile/${props.userId}` ||
        $route.path == `/makecourse` ||
        $route.path == `/table`
          ? `/profprofile/${props.userId}`
          : $route.path == `/studprofile/${props.userId}` ||
              $route.path == `/marks` ||
              $route.path == `/courses`
            ? `/studprofile/${props.userId}`
            : `/404`
      "
      :class="
        $route.path == `/studprofile/${props.userId}` ||
        $route.path == `/profprofile/${props.userId}`
          ? 'sidebar__link sidebar__link--active'
          : 'sidebar__link'
      "
      >Профиль</router-link
    >
    <router-link
      v-if="
        $route.path == `/profprofile/${props.userId}` ||
        $route.path == `/makecourse` ||
        $route.path == `/table`
      "
      to="/table"
      :class="
        $route.path == '/table'
          ? 'sidebar__link sidebar__link--active'
          : 'sidebar__link'
      "
      >Зачетная таблица</router-link
    >
    <router-link
      v-if="
        $route.path == `/profprofile/${props.userId}` ||
        $route.path == `/makecourse` ||
        $route.path == `/table`
      "
      to="/makecourse"
      :class="
        $route.path == '/makecourse'
          ? 'sidebar__link sidebar__link--active'
          : 'sidebar__link'
      "
      >Редактор курса</router-link
    >
    <router-link
      v-if="
        $route.path == `/studprofile/${props.userId}` ||
        $route.path == `/marks` ||
        $route.path == `/courses`
      "
      to="/courses"
      :class="
        $route.path == '/courses'
          ? 'sidebar__link sidebar__link--active'
          : 'sidebar__link'
      "
      >Курсы</router-link
    >
    <router-link
      v-if="
        $route.path == `/studprofile/${props.userId}` ||
        $route.path == `/marks` ||
        $route.path == `/courses`
      "
      to="/marks"
      :class="
        $route.path == '/marks'
          ? 'sidebar__link sidebar__link--active'
          : 'sidebar__link'
      "
      >Мои оценки</router-link
    >
  </div>
</template>

<style scoped lang="scss">
.sidebar {
  margin-top: 70px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 300px;
  position: fixed;
  &__info {
    margin-bottom: 50px;
    display: flex;
    gap: 10px;
    align-items: center;
  }
  &__info-pic {
    width: 100px;
    height: 100px;
    border-radius: 100px;
    background-color: #fff;
  }
  &__info-name {
    font-size: 24px;
    line-height: 36px;
    color: #fff;
  }
  &__link {
    font-size: 24px;
    line-height: 47px;
    color: #fff;
    &--active {
      color: #000;
      font-size: 24px;
      line-height: 47px;
      background-color: #fff;
      padding: 10px 40px;
      border-radius: 50px;
    }
  }
}
</style>
