<script setup>
import Sidebar from "./Sidebar.vue";

import { onMounted, ref } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

const router = useRoute();
const group = ref("")
const user = ref([]);

const token = localStorage.getItem("token");

const getData = async () => {
  try {
    const { data } = await axios.get(`/api/User/${router.params.userId}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    
    user.value = data;
  } catch (err) {
    console.log(err);
  } finally{
    getGroup()
  }
};
const getGroup = async () => {
  try{
    const { data } = await axios.get(`/api/Gro/${user.value.fiGroup}`)
    group.value = data.name
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
    <div class="profile__inner">
      <div class="firstcol">
        <div class="box">
          <img class="img" src="../assets/userpic.png" alt="" />
          <div class="info">
            <p class="info__name">{{ user.first_name }}</p>
            <p class="info__mail">Email: {{ user.email }}</p>
            <p
              v-if="$route.path == `/studprofile/${$route.params.userId}`"
              class="info__group"
            >
              Группа: {{ group }}
            </p>
            <p class="info__type">
              Тип:
              {{
                user.type == "Student"
                  ? "Студент"
                  : user.type == "Professor"
                    ? "Преподаватель"
                    : ""
              }}
            </p>
          </div>
        </div>
      </div>
      <div class="secondcol">
        <p class="text">
          🚧🔨 <br />
          Раздел находится в разработке
        </p>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.profile__inner {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 210px;
}
.firstcol {
  margin-top: 50px;
  background-color: #fff;
  width: 1032px;
  height: 308px;
  border-radius: 20px;
}
.secondcol {
  margin-top: 25px;
  background-color: #fff;
  width: 1032px;
  min-height: 308px;
  border-radius: 20px;
}
.box {
  display: flex;
  gap: 20px;
  margin-left: 25px;
  margin-top: 54px;
}
.img {
  width: 200px;
  height: 200px;
}
.info__name {
  font-weight: 600;
  font-size: 24px;
  line-height: 36px;
  margin-bottom: 51px;
}
.info__mail,
.info__type,
.info__group {
  font-size: 20px;
  line-height: 30px;
}
.info__mail,
.info__group {
  margin-bottom: 10px;
}
.text {
  text-align: center;
  font-size: 30px;
  margin-top: 89px;
}
</style>
