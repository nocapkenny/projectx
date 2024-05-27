<script setup>
const props = defineProps({
  onClickGroup: Function,
  name: String,
  id: Number
});


</script>

<template>
  <li class="groups__list-item">
    <label @click="onClickGroup">
      <input
        type="radio"
        name="group-course"
        class="groups__item-radio--real"
        :value="[props.name,props.id]"
      />
      <span class="groups__item-radio--custom"></span>
      <p class="groups__item-text">{{ props.name }}</p>
    </label>
  </li>
</template>
