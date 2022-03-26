<template>
  <div class="grid grid-cols-3 gap-4 justify-center sm:w-full md:w-50 lg:w-1/2 mx-auto max-w-screen-sm bg-l-60 dark:bg-d-60">
    <div v-for="index in 9" :key="index" >
      <Block :values=gridStart[index-1] :idBlock=index-1 :class="[{ 'mx-px': index === 2}, { 'm-px': index === 5 }, { 'my-px': index === 4 }, { 'my-px': index === 6 }, { 'mx-px': index === 8 }]"/>
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

