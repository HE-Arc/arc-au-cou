<template>
  <div class="grid grid-cols-3 gap-1 content-center max-w-xs">
    <div class="" v-for="index in 9" :key="index">
      <Square class="p-1" :value="values[index]"/>
    </div>
  </div>
</template>

<script>
export default {
  props:{
    values: Array,
  }
}
</script>


