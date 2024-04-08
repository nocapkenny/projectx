<script setup>
import Header from "../components/Header.vue";
import Sidebar from "../components/Sidebar.vue";
</script>

<template>
  <Header />
  <div class="container">
    <Sidebar class="aside" />
    <div class="results">
      <h3 class="results__title">Выберите факультет</h3>
      <div class="results__facs">
        <button class="results__fac results__fac--active">ИКНТ</button>
        <button class="results__fac">МЕХМАТ</button>
        <button class="results__fac">ЭКОНОМ</button>
      </div>
      <div class="results__groups">
        <button class="results__group results__group--active">ИТХ-12</button>
        <button class="results__group">ПМИ-34</button>
        <button class="results__group">ИТХ-34</button>
      </div>
      <div class="results__header">
        <h4 class="results__header-title">Студент</h4>
        <h4 class="results__header-title">КТ1</h4>
        <h4 class="results__header-title">КТ2</h4>
        <h4 class="results__header-title">КТ3</h4>
        <h4 class="results__header-title">КТ4</h4>
        <h4 class="results__header-title">ИТОГ</h4>
      </div>
      <div class="results__table">
        <div class="results__table-item">
          <p class="results__table-name">Иванов Иван</p>
          <input class="results__mark" placeholder="0" type="number" min="0" max="100"/>
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <p class="results__table-point">100</p>
        </div>  
        <div class="results__table-item">
          <p class="results__table-name">Иванов Иван</p>
          <input class="results__mark" placeholder="0" type="number" min="0" max="100"/>
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <p class="results__table-point">100</p>
        </div>  
        <div class="results__table-item">
          <p class="results__table-name">Иванов Иван</p>
          <input class="results__mark" placeholder="0" type="number" min="0" max="100"/>
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <p class="results__table-point">100</p>
        </div>  
        <div class="results__table-item">
          <p class="results__table-name">Иванов Иван</p>
          <input class="results__mark" placeholder="0" type="number" min="0" max="100"/>
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <input class="results__mark" placeholder="0" type="number" min="0" />
          <p class="results__table-point">100</p>
        </div>  
      </div>
      <div class="results__paginate">
        <a href="#" class="results__page">1</a>
        <a href="#" class="results__page">2</a>
        <a href="#" class="results__page">3</a>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.results__table-item{
  display: flex;
  justify-content: space-between;
}
.aside {
  margin-top: 15px;
}
.inner {
  position: relative;
}
.results {
  margin-left: 260px;
  background-color: #fff;
  border-radius: 20px;
  padding-top: 12px;
  margin-top: 55px;
  padding-bottom: 40px;
  &__table-name{
    margin-left: 60px;
  }
  &__table-point{
    margin-right: 60px;
  }
  &__title {
    margin-left: 30px;
    font-size: 32px;
    line-height: 47px;
    margin-bottom: 5px;
    font-weight: 400;
  }
  &__facs {
    text-align: center;
  }
  &__fac {
    background-color: transparent;
    border: none;
    font-size: 20px;
    color: #000;
    opacity: 0.4;
    transition: all 0.3s ease;
    cursor: pointer;
    &:hover {
      color: rgba(0, 18, 53, 1);
      opacity: 1;
    }
    &--active {
      color: rgba(0, 18, 53, 1);
      opacity: 1;
    }
  }
  &__fac + .results__fac {
    margin-left: 16px;
  }
  &__groups {
    margin-left: 30px;
    margin-bottom: 5px;
  }
  &__group {
    font-size: 15px;
    line-height: 22px;
    background-color: transparent;
    border: none;
    color: #000;
    opacity: 0.4;
    cursor: pointer;
    &:hover {
      color: rgba(0, 18, 53, 1);
      opacity: 1;
    }
    &--active {
      color: rgba(0, 18, 53, 1);
      opacity: 1;
    }
  }
  &__group + .results__group {
    margin-left: 30px;
  }
  &__paginate {
    display: flex;
    justify-content: center;
    gap: 30px;
    font-size: 25px;
  }
  &__page {
    color: #000000;
    opacity: 0.5;
    transition: all 0.3s ease;
    &:hover {
      color: rgba(0, 18, 53, 1);
      opacity: 1;
    }
  }
  
  &__header {
    display: flex;
    justify-content: space-around;
    text-align: center;
    margin-bottom: 25px;
    background-color: #e6f8ff;
    border-radius: 25px;
    padding: 10px 0;
  }
  &__header-title {
    font-size: 25px;
    color: #005a8d;
    font-weight: 400;
  }
  &__name {
    margin-bottom: 50px;
    font-size: 18px;
    padding-left: 15px;
  }
  &__mark {
    margin-bottom: 50px;
    font-size: 18px;
    border: none;
    width: 39px;
    outline: none;
    font-family: "Oswald", sans-serif;
    font-optical-sizing: auto;
    font-weight: 400;
    &::placeholder{
      color: #000;
    }
  }
}
</style>
