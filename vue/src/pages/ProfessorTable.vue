<script setup>
import Sidebar from "../components/Sidebar.vue";
</script>

<template>
  <div class="container">
    <Sidebar class="aside" :userId="$route.params.userId" :path="$route.path" />
    <div class="fac">
      <p class="fac__title title">Выберите факультет</p>
      <ul class="fac__list">
        <li class="fac__list-item">
          <label>
            <input type="radio" name="fac" class="fac__item-radio--real" />
            <span class="fac__item-radio--custom"></span>
            <p class="fac__item-text">
              Институт компьютерных наук и технологий
            </p>
          </label>
        </li>
        <li class="fac__list-item">
          <label>
            <input type="radio" name="fac" class="fac__item-radio--real" />
            <span class="fac__item-radio--custom"></span>
            <p class="fac__item-text">Физико-Математический факультет</p>
          </label>
        </li>
      </ul>
    </div>
    <div class="selectors">
      <div class="selectors__course">
        <p class="course__title title">Выберите курс</p>
        <ul class="course__list">
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="course"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">1 курс</p>
            </label>
          </li>
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="course"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">2 курс</p>
            </label>
          </li>
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="course"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">3 курс</p>
            </label>
          </li>
          <li class="course__list-item">
            <label>
              <input
                type="radio"
                name="course"
                class="course__item-radio--real"
              />
              <span class="course__item-radio--custom"></span>
              <p class="course__item-text">4 курс</p>
            </label>
          </li>
        </ul>
      </div>
      <div class="selectors__groups">
        <p class="groups__title title">Выберите группу</p>
        <ul class="groups__list">
          <li class="groups__list-item">
            <label>
              <input
                type="radio"
                name="group"
                class="groups__item-radio--real"
              />
              <span class="groups__item-radio--custom"></span>
              <p class="groups__item-text">ФИТ-12-23</p>
            </label>
          </li>
          <li class="groups__list-item">
            <label>
              <input
                type="radio"
                name="group"
                class="groups__item-radio--real"
              />
              <span class="groups__item-radio--custom"></span>
              <p class="groups__item-text">ПМИ-12-23</p>
            </label>
          </li>
          <li class="groups__list-item">
            <label>
              <input
                type="radio"
                name="group"
                class="groups__item-radio--real"
              />
              <span class="groups__item-radio--custom"></span>
              <p class="groups__item-text">ПМИ-34-23</p>
            </label>
          </li>
          <li class="groups__list-item">
            <label>
              <input
                type="radio"
                name="group"
                class="groups__item-radio--real"
              />
              <span class="groups__item-radio--custom"></span>
              <p class="groups__item-text">ИТХ-12-23</p>
            </label>
          </li>
        </ul>
        <div class="groups__paginate">
          <a href="#" class="groups__page groups__page--active">1</a>
          <a href="#" class="groups__page">2</a>
          <a href="#" class="groups__page">3</a>
        </div>
      </div>
    </div>
    <div class="table">
      <div class="table__headers">
        <p class="table__header table__header--name">Фамилия/Имя</p>
        <p class="table__header">КТ1</p>
        <p class="table__header">КТ2</p>
        <p class="table__header">КТ3</p>
        <p class="table__header">КТ4</p>
        <p class="table__header">ИТОГ</p>
      </div>
      <div class="table__inner">
        <div class="table__item">
          <p class="table__item-name">Лукьянов Никита</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-sum">100</p>
        </div>
        <div class="table__item">
          <p class="table__item-name">Безродный Егор</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-sum">100</p>
        </div>
        <div class="table__item">
          <p class="table__item-name">Патракова София</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-sum">100</p>
        </div>
        <div class="table__item">
          <p class="table__item-name">Сагиев Артур</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-sum">100</p>
        </div>
        <div class="table__item">
          <p class="table__item-name">Солдатов Роман</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-sum">100</p>
        </div>
        <div class="table__item">
          <p class="table__item-name">Сорокин Вадим</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-point">20</p>
          <p class="table__item-sum">100</p>
        </div>
      </div>
      <div class="table__paginate">
        <a href="#" class="table__page table__page--active">1</a>
        <a href="#" class="table__page">2</a>
        <a href="#" class="table__page">3</a>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.aside {
  top: 0;
}
.table {
  margin-left: 219px;
  padding-left: 25px;
  padding-right: 25px;
  padding-top: 25px;
  padding-bottom: 20px;
  background-color: #fff;
  border-radius: 12px;
  &__headers {
    display: flex;
    justify-content: space-between;
    padding-top: 16px;
    padding-left: 24px;
    padding-bottom: 16px;
    padding-right: 24px;
    color: #fff;
    background-color: #02457a;
    border-radius: 12px;
  }
  &__inner {
    display: grid;
    grid-template-rows: repeat(6, 1fr);
  }
  &__item {
    display: flex;
    justify-content: space-between;
    padding-top: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(#000000, 0.1);
  }
  &__item-name {
    width: 200px;
    padding-left: 24px;
  }
  &__item-sum {
    padding-right: 40px;
  }
  &__item-point {
    margin-left: 20px;
  }
}
.table__header--name {
  width: 200px;
}
.table__paginate {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}
.table__page {
  font-size: 14px;
  line-height: 17px;
  color: rgba(#000, 0.2);
  padding-top: 5px;
  padding-bottom: 5px;
  padding-left: 10px;
  padding-right: 10px;
  &:hover {
    border-radius: 4px;
    background-color: rgba(#0000000d, 0.05);
  }
  &--active {
    background-color: #02457a;
    color: #fff;
    border-radius: 4px;
    &:hover {
      background-color: #02457a;
      color: #fff;
      border-radius: 4px;
    }
  }
}
.title {
  font-size: 24px;
  line-height: 36px;
  margin-bottom: 12px;
  margin-left: 24px;
}
.fac {
  margin-top: 20px;
  padding-bottom: 12px;
  margin-bottom: 20px;
  padding-top: 12px;
  margin-left: 219px;
  background-color: #fff;
  border-radius: 12px;

  &__item-text {
    font-size: 16px;
    line-height: 24px;
  }
}
.fac__list {
  list-style: none;
  margin-left: 25px;
  &-item label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
}
.fac__item-radio--custom {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #000000;
  border-radius: 2px;
  position: relative;
  transition: 0.2s ease-in;
}
.fac__item-radio--custom::before {
  content: "";
  display: inline-block;
  width: 10px;
  height: 10px;
  background-image: url(../assets/checked.svg);
  background-repeat: no-repeat;
  background-size: contain;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0);
  margin-top: 1px;
  transition: 0.2s ease-in;
}
.fac__item-radio--real:checked + .fac__item-radio--custom::before {
  transform: translate(-50%, -50%) scale(1);
}
.fac__item-radio--real:checked + .fac__item-radio--custom {
  border: 2px solid #02457a;
}
.fac__item-radio--real {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.selectors {
  display: flex;
  &__course {
    margin-left: 219px;
    background-color: #fff;
    border-radius: 12px;
    padding-top: 12px;
    padding-bottom: 12px;
    padding-right: 25px;
    margin-bottom: 20px;
  }
  &__groups {
    margin-left: auto;
    background-color: #fff;
    border-radius: 12px;
    padding-top: 12px;
    padding-bottom: 12px;
    margin-bottom: 20px;
    width: 60%;
  }
}
.course__list {
  list-style: none;
  margin-left: 25px;
  &-item label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
}
.course__item-radio--custom {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #000000;
  border-radius: 2px;
  position: relative;
  transition: 0.2s ease-in;
}
.course__item-radio--custom::before {
  content: "";
  display: inline-block;
  width: 10px;
  height: 10px;
  background-image: url(../assets/checked.svg);
  background-repeat: no-repeat;
  background-size: contain;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0);
  margin-top: 1px;
  transition: 0.2s ease-in;
}
.course__item-radio--real:checked + .course__item-radio--custom::before {
  transform: translate(-50%, -50%) scale(1);
}
.course__item-radio--real:checked + .course__item-radio--custom {
  border: 2px solid #02457a;
}
.course__item-radio--real {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.groups__list {
  list-style: none;
  margin-left: 25px;
  &-item label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
}
.groups__item-radio--custom {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid #000000;
  border-radius: 2px;
  position: relative;
  transition: 0.2s ease-in;
}
.groups__item-radio--custom::before {
  content: "";
  display: inline-block;
  width: 10px;
  height: 10px;
  background-image: url(../assets/checked.svg);
  background-repeat: no-repeat;
  background-size: contain;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0);
  margin-top: 1px;
  transition: 0.2s ease-in;
}
.groups__item-radio--real:checked + .groups__item-radio--custom::before {
  transform: translate(-50%, -50%) scale(1);
}
.groups__item-radio--real:checked + .groups__item-radio--custom {
  border: 2px solid #02457a;
}
.groups__item-radio--real {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}
.groups__paginate {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-right: 25px;
}
.groups__page {
  font-size: 14px;
  line-height: 17px;
  color: rgba(#000, 0.2);
  padding-top: 5px;
  padding-bottom: 5px;
  padding-left: 10px;
  padding-right: 10px;
  &:hover {
    border-radius: 4px;
    background-color: rgba(#0000000d, 0.05);
  }
  &--active {
    background-color: #02457a;
    color: #fff;
    border-radius: 4px;
    &:hover {
      background-color: #02457a;
      color: #fff;
      border-radius: 4px;
    }
  }
}
</style>
