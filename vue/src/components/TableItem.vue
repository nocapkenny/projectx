<script setup>
import { onMounted, ref, watch, computed } from "vue";
import axios from "axios";

const marks = ref();
const kt1 = ref();
const kt2 = ref();
const kt3 = ref();
const kt4 = ref();
const lessonsId = ref(null)
const error = ref("")
const summ = computed(() => parseInt(kt1.value) + parseInt(kt2.value) + parseInt(kt3.value) +parseInt(kt4.value))

const token = localStorage.getItem("token")

const props = defineProps({
  name: String,
  lesson: String,
  marksId: Array
});
const putMarks = async () => {
    try{
    const { data } = await axios.put(`/api/Osenki/${lessonsId.value}/`,{
        id: lessonsId.value,
        predmet_name: props.lesson,
        kt1: kt1.value,
        kt2: kt2.value,
        kt3: kt3.value,
        kt4: kt4.value
    }, {
        headers:{
            Authorization: `Token ${token}`
        }
    })
  } catch(err){
    console.log(err)
  } finally{
    alert("Готово!")
  }
}
const getMarks = async () => {
  for (let id = 0; id < props.marksId.length; id++){
    try {
      const { data } = await axios.get(`/api/Osenki/${props.marksId[id]}`, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      if(data.predmet_name == props.lesson){
        lessonsId.value = props.marksId[id]
        marks.value = data;
        kt1.value = data.kt1;
        kt2.value = data.kt2;
        kt3.value = data.kt3;
        kt4.value = data.kt4;
        summ.value = kt1.value + kt2.value + kt3.value + kt4.value;
      }
    } catch (err) {
      console.log(err);
    }
  }
};

onMounted(()=>{
    getMarks()
})
</script>

<template>
  <div class="table__item">
    <p class="table__item-name">{{ props.name }}</p>
    <input v-model="kt1" :placeholder="kt1" class="table__item-point table__item-point--first"></input>
    <input v-model="kt2" :placeholder="kt2" class="table__item-point"></input>
    <input v-model="kt3" :placeholder="kt3" class="table__item-point"></input>
    <input v-model="kt4" :placeholder="kt4" class="table__item-point table__item-point--last"></input>
    <p class="table__item-sum">{{ summ }}</p>
    <button class="table__button" @click="putMarks"><img class="table__img" src="../assets/save.svg" alt="save"></button>
  </div>
  
  
</template>

<style scoped lang="scss" >
.table__button{
    border: none;
    background-color: transparent;
    color: #000;
    font-size: 14px;
    line-height: 16px;
    padding: 0;
    padding-right: 50px;
    margin: 0;
}
.table__img{
  width: 25px;
  height: 25px;
}
</style>
