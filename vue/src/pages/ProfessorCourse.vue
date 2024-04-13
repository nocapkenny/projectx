<script setup>
import Header from "../components/Header.vue";
import Sidebar from "../components/Sidebar.vue";
</script>

<template>
  <Header />
  <div class="container">
    <Sidebar :userId="$route.params.userId" :path="$route.path"/>
    <div class="course__inner">
      <div class="firstcol">
        <h3 class="course__title">Выберите группу</h3>
        <div class="course__groups">
          <div class="course__item">
            <p class="course__group">ИТХ-12-23</p>
            <input type="checkbox" />
          </div>
          <div class="course__item">
            <p class="course__group">ИТХ-12-23</p>
            <input type="checkbox" />
          </div>
          <div class="course__item">
            <p class="course__group">ИТХ-12-23</p>
            <input type="checkbox" />
          </div>
          <div class="course__item">
            <p class="course__group">ИТХ-12-23</p>
            <input type="checkbox" />
          </div>
        </div>
      </div>
      <div class="secondcol">
        <div class="course__box">
          <h3 class="course__title">Редактор</h3>
          <select class="course__select">
            <option selected disabled value="Выберите название курса">
              Выберите название курса
            </option>
            <option value="Дискретная математика">Дискретная математика</option>
            <option value="Матан">Матан</option>
          </select>
          <input
            class="course__input"
            type="text"
            placeholder="Введите название лекции"
          />
          <div class="course__files">
            <div class="course__files-item">
              <p class="course__text">Теория</p>
              <label class="course__label">
                Загрузить файл
                <input type="file" />
              </label>
            </div>
            <div class="course__files-item">
              <p class="course__text">Задание</p>
              <label class="course__label">
                Загрузить файл
                <input type="file" />
              </label>
            </div>
          </div>
          <button class="course__btn">
            Готово
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
input[type="file"]{
  display: none;
}
.course__files{
  display: flex;
  width: 360px;
  justify-content: space-between;
  margin-top: 30px;
  &__item{
    display: flex;
  }
}
.course__text{
  font-size: 24px;
}
.course__label{
  color: #ABABABCC;
  opacity: .8;
  cursor: pointer;
}
.course__inner {
  display: flex;
  justify-content: center;
}
.course__box {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.course__title {
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 32px;
  line-height: 47px;
  font-weight: 400;
  text-align: center;
}
.course__item {
  display: flex;
  justify-content: center;
}
.course__group {
  margin-right: 10px;
  font-size: 20px;
  line-height: 30px;
}
.course__select {
  margin-bottom: 20px;
  width: 360px;
  font-family: "Oswald", sans-serif;
  font-optical-sizing: auto;
  font-weight: 400;
  background-color: rgba(231, 231, 231, 0.83);
  outline: none;
  border: none;
  margin-top: 20px;
  font-size: 24px;
  line-height: 36;
  border-radius: 20px;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 10px;
}
.course__input {
  width: 360px;
  background-color: rgba(231, 231, 231, 0.83);
  outline: none;
  border: none;
  padding-left: 15px;
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
.course__btn{
    background-color: #4B5873;
    color: #fff;
    padding: 10px 27px;
    font-size: 24px;
    line-height: 36px;
    border-radius: 20px;
    border: none;
    cursor: pointer;
    transition: transform .3s;
    margin-top: 20px;
    &:active{
      transform: translateY(8px);
    }
  }
</style>
