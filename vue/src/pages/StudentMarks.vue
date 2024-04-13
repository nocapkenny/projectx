<script setup>
import Sidebar from "@/components/Sidebar.vue";
import Header from "../components/Header.vue";
</script>

<template>
  <Header />
  <div class="container">
    <Sidebar class="aside" :userId="$route.params.userId" :path="$route.path"/>
    <div class="marks">
      <div class="marks__courses">
        <button class="marks__courses-btn marks__courses-btn--active">
          Алгоритмы и структуры данных
        </button>
        <button class="marks__courses-btn">Аналитическая геометрия</button>
        <button class="marks__courses-btn">Дискретная математика</button>
      </div>
      <div class="marks__header">
        <p class="marks__header-text">Name</p>
        <p class="marks__header-text">Проходной</p>
        <p class="marks__header-text">Оценка</p>
        <p class="marks__header-text">Максимальный балл</p>
        <p class="marks__header-text">Дата</p>
      </div>
      <div class="marks__table">
        <div class="marks__table-item">
          <p class="marks__table-control">КТ1</p>
          <p class="marks__table-minpoint">15</p>
          <p class="marks__table-point">50</p>
          <p class="marks__table-maxpoint">100</p>
          <p class="marks__table-date">01.04.2024</p>
        </div>
        <div class="marks__table-item">
          <p class="marks__table-control">КТ2</p>
          <p class="marks__table-minpoint">15</p>
          <p class="marks__table-point">50</p>
          <p class="marks__table-maxpoint">100</p>
          <p class="marks__table-date">01.04.2024</p>
        </div>
        <div class="marks__table-item">
          <p class="marks__table-control">КТ3</p>
          <p class="marks__table-minpoint">15</p>
          <p class="marks__table-point">50</p>
          <p class="marks__table-maxpoint">100</p>
          <p class="marks__table-date">01.04.2024</p>
        </div>
        <div class="marks__table-item">
          <p class="marks__table-control">КТ4</p>
          <p class="marks__table-minpoint">15</p>
          <p class="marks__table-point">50</p>
          <p class="marks__table-maxpoint">100</p>
          <p class="marks__table-date">01.04.2024</p>
        </div>
      </div>
      <p class="marks__result">ИТОГ:</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.aside{
  margin-top: 15px;
}
.marks {
  margin-top: 55px;
  margin-left: 260px;
  background-color: #fff;
  border-radius: 20px;
  padding-bottom: 30px;
  &__courses {
    text-align: center;
    padding-top: 25px;
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-bottom: 25px;
    &-btn {
      background-color: transparent;
      border: none;
      font-size: 20px;
      line-height: 30px;
      color: #1e1e1e80;
      opacity: 0.5;
      transition: all ease 0.3s;
      cursor: pointer;
      &--active {
        opacity: 1;
        color: #001235eb;
      }
      &:hover {
        opacity: 1;
        color: #001235eb;
      }
    }
  }
  &__header {
    display: flex;
    justify-content: space-evenly;
    background-color: #e6f8ff;
    border-radius: 25px;
    padding-top: 14px;
    padding-bottom: 14px;
    color: #005a8d;
    font-size: 25px;
    margin-bottom: 30px;
  }
  &__table {
    
    margin-left: 80px;
    grid-gap: 130px;
    font-size: 20px;
    &-item{
      display: flex;
      justify-content: space-between;
      margin-bottom: 50px;
    }
    &-date{
      margin-right: 60px;
    }
    &-point{
      margin-right: 30px;
    }
  }
  &__result {
    font-size: 25px;
    display: flex;
    justify-content: flex-end;
    margin-right: 100px;
  }
}
</style>
