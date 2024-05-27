<script setup>

const props = defineProps({
  name: String,
  onClickFac: Function,
});


</script>

<template>
  <li class="fac__list-item">
    <label @click="onClickFac">
      <input :value="props.name" type="radio" name="fac-course" class="fac__item-radio--real" />
      <span class="fac__item-radio--custom"></span>
      <p class="fac__item-text">{{ props.name }}</p>
    </label>
  </li>
</template>
