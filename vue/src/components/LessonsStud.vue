<script setup>
import axios from "axios";
import { onMounted, ref, watch } from "vue";
const token = localStorage.getItem("token");
const lessonName = ref("");

const props = defineProps({
  id: Number,
  onClickLesson: Function,
});

const getLessons = async () => {
  try {
    const { data } = await axios.get(`/api/Osenki/${props.id}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    lessonName.value = data.predmet_name;
  } catch (err) {
    console.log(err);
  }
};
onMounted(()=>{
    getLessons()
})
</script>
<template>
  <li class="course__list-item stud">
    <label @change="onClickLesson">
      <input
        type="radio"
        name="lesson"
        class="course__item-radio--real stud"
        :value="[lessonName,props.id]"
      />
      <span class="course__item-radio--custom stud"></span>
      <p class="course__item-text stud">{{ lessonName }}</p>
    </label>
  </li>
</template>
