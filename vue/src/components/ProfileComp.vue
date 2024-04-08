<script setup>
import Sidebar from "./Sidebar.vue";

</script>



<template>
  <div class="container">
    <Sidebar :userId="$route.params.userId"/>
    <div class="profile__inner">
      <div class="firstcol">
      </div>
      <div class="secondcol"></div>
    </div>
  </div>
</template>

<style lang="scss">
.profile__inner{
  display: flex;
  justify-content: center;
}
.firstcol {
  margin-top: 55px;
  background-color: #fff;
  height: 600px;
  width: 291px;
  margin-left: 260px;
  border-radius: 20px;
  margin-right: 32px;
}
.secondcol {
  margin-top: 55px;
  background-color: #fff;
  height: 600px;
  width: 600px;
  border-radius: 20px;
}
</style>
