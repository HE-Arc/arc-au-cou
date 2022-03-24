<template>
  <div class="grid grid-cols-3 gap-4 justify-center mx-auto w-1/4 max-w-screen-sm dark:bg-d-60">
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

