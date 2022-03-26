<template>
  <div class="grid grid-cols-3 gap-0 justify-center max-w-xs">
    <div class="" v-for="(cell,index) in values" :key="index">
      <Square class="p-1 mx-auto" :cell="cell" :posX="idBlock" :posY="index"/>
    </div>
  </div>
</template>

<script>
export default {
  props:{
    values: Array,
    idBlock: Number
  }
}
</script>


