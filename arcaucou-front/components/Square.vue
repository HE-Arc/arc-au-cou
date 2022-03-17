<template>
  <div>
    <div v-if="value != 0" class="text-center h-10 w-10 bg-d-border">
      {{value}}
    </div>
    <div v-if="value === 0" class="text-center h-10 w-10 bg-d-border">

    </div>
  </diV>
</template>

<script>
export default {
  props: {
    value: Number,
  }
}
</script>
