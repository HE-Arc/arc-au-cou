<template>
  <div class="grid grid-cols-3 gap-2 sm:gap-4 justify-center sm:w-full md:w-50 lg:w-1/2 mx-auto max-w-lg">
    <div v-for="index in 9" :key="index" >
      <Block :values=gridStart[index-1] :idBlock=index-1 />
    </div>
  </diV>
</template>

<script>

export default {
  props: {
    gridStart: Array,
  },
}
</script>

