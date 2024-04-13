<script setup>
import Sidebar from "@/components/Sidebar.vue";
import Header from "../components/Header.vue";
</script>

<template>
  <Header />
  <div class="container">
    <Sidebar :userId="$route.params.userId" :path="$route.path"/>
    <div class="course__inner">
      <div class="firstcol">
        <h3 class="course__title">Выберите курс</h3>
        <div class="course__box">
          <div class="course__box-item">
            <input name="course" value="1" type="radio" />
            <p class="course__box-text">Матан</p>
          </div>
          <div class="course__box-item">
            <input name="course" value="2" type="radio" />
            <p class="course__box-text">Дискра</p>
          </div>
          <div class="course__box-item">
            <input name="course" value="3" type="radio" />
            <p class="course__box-text">Ангем</p>
          </div>
        </div>
      </div>
      <div class="secondcol">
        <h3 class="course__subtitle">Название курса</h3>
        <div class="course__info">
          <div class="course__info-item">
            <h4 class="course__subsubtitle">Название лекции</h4>
            <div class="course__files">
              <div class="course__files-item">
                <p class="course__files-text">Теория</p>
                <svg
                  width="18"
                  height="22"
                  viewBox="0 0 18 22"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12 1H3C2.46957 1 1.96086 1.21071 1.58579 1.58579C1.21071 1.96086 1 2.46957 1 3V19C1 19.5304 1.21071 20.0391 1.58579 20.4142C1.96086 20.7893 2.46957 21 3 21H15C15.5304 21 16.0391 20.7893 16.4142 20.4142C16.7893 20.0391 17 19.5304 17 19V6L12 1Z"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
                <a href="#" class="course__files-download">file.doc</a>
              </div>
              <div class="course__files-item">
                <p class="course__files-text">Задание</p>
                <svg
                  width="18"
                  height="22"
                  viewBox="0 0 18 22"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12 1H3C2.46957 1 1.96086 1.21071 1.58579 1.58579C1.21071 1.96086 1 2.46957 1 3V19C1 19.5304 1.21071 20.0391 1.58579 20.4142C1.96086 20.7893 2.46957 21 3 21H15C15.5304 21 16.0391 20.7893 16.4142 20.4142C16.7893 20.0391 17 19.5304 17 19V6L12 1Z"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
                <a href="#" class="course__files-download">file.txt</a>
              </div>
            </div>
          </div>
          <div class="course__info-item">
            <h4 class="course__subsubtitle">Название лекции</h4>
            <div class="course__files">
              <div class="course__files-item">
                <p class="course__files-text">Теория</p>
                <svg
                  width="18"
                  height="22"
                  viewBox="0 0 18 22"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12 1H3C2.46957 1 1.96086 1.21071 1.58579 1.58579C1.21071 1.96086 1 2.46957 1 3V19C1 19.5304 1.21071 20.0391 1.58579 20.4142C1.96086 20.7893 2.46957 21 3 21H15C15.5304 21 16.0391 20.7893 16.4142 20.4142C16.7893 20.0391 17 19.5304 17 19V6L12 1Z"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
                <a href="#" class="course__files-download">file.doc</a>
              </div>
              <div class="course__files-item">
                <p class="course__files-text">Задание</p>
                <svg
                  width="18"
                  height="22"
                  viewBox="0 0 18 22"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12 1H3C2.46957 1 1.96086 1.21071 1.58579 1.58579C1.21071 1.96086 1 2.46957 1 3V19C1 19.5304 1.21071 20.0391 1.58579 20.4142C1.96086 20.7893 2.46957 21 3 21H15C15.5304 21 16.0391 20.7893 16.4142 20.4142C16.7893 20.0391 17 19.5304 17 19V6L12 1Z"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
                <a href="#" class="course__files-download">file.txt</a>
              </div>
            </div>
          </div>
          <div class="course__info-item">
            <h4 class="course__subsubtitle">Название лекции</h4>
            <div class="course__files">
              <div class="course__files-item">
                <p class="course__files-text">Теория</p>
                <svg
                  width="18"
                  height="22"
                  viewBox="0 0 18 22"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12 1H3C2.46957 1 1.96086 1.21071 1.58579 1.58579C1.21071 1.96086 1 2.46957 1 3V19C1 19.5304 1.21071 20.0391 1.58579 20.4142C1.96086 20.7893 2.46957 21 3 21H15C15.5304 21 16.0391 20.7893 16.4142 20.4142C16.7893 20.0391 17 19.5304 17 19V6L12 1Z"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
                <a href="#" class="course__files-download">file.doc</a>
              </div>
              <div class="course__files-item">
                <p class="course__files-text">Задание</p>
                <svg
                  width="18"
                  height="22"
                  viewBox="0 0 18 22"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12 1H3C2.46957 1 1.96086 1.21071 1.58579 1.58579C1.21071 1.96086 1 2.46957 1 3V19C1 19.5304 1.21071 20.0391 1.58579 20.4142C1.96086 20.7893 2.46957 21 3 21H15C15.5304 21 16.0391 20.7893 16.4142 20.4142C16.7893 20.0391 17 19.5304 17 19V6L12 1Z"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
                <a href="#" class="course__files-download">file.txt</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.course__inner {
  display: flex;
  justify-content: center;
}
.course__title {
  font-size: 32px;
  line-height: 47px;
  font-weight: 400;
  margin-left: 30px;
  margin-top: 20px;
  margin-bottom: 20px;
}
.course__box {
  margin-left: 30px;
  &-item {
    align-items: center;
    display: flex;
    margin-bottom: 20px;
  }
  &-text {
    font-size: 20px;
    line-height: 30px;
    margin-left: 10px;
  }
}

.course__subtitle {
  margin-top: 30px;
  font-size: 32px;
  line-height: 47px;
  text-align: center;
  font-weight: 400;
  margin-bottom: 25px;
}
.course__subsubtitle {
  font-weight: 400;
  margin-bottom: 25px;
  font-size: 24px;
  line-height: 36px;
  text-align: center;
}
.course__files {
  display: flex;
  justify-content: center;
  gap: 20px;
  &-item {
    display: flex;
    gap: 10px;
    align-items: center;
    margin-right: 20px;
  }
  &-text {
    font-size: 24px;
    line-height: 47px;
  }
  &-download {
    color: #abababcc;
    opacity: 0.8;
    text-decoration: none;
    font-size: 16px;
    line-height: 24px;
  }
}
.course__info-item + .course__info-item {
  margin-top: 20px;
}
</style>
