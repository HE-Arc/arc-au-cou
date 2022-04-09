<template>
  <div class="grid grid-cols-3 gap-2 justify-center mx-auto w-10/12 sm:w-8/12 md:w-1/2 lg:w-1/4 xl:w-1/6">
    <div class="mx-auto w-full h-full" v-for="index in 9" :key="index" >
      <button @click="handleClic(index)" class="mb-4 w-full h-full text-3xl font-semibold text-d-text bg-l-60 dark:bg-d-60 border-l-text dark:border-d-60 border-2 bottom-2 py-3 rounded-xl hover:border-d-10 dark:hover:border-d-10">
        {{index}}
      </button>
    </div>
    <button @click="handleClic(0)" class="mb-4 col-span-3 w-full h-full text-3xl font-semibold text-d-text bg-l-60 dark:bg-d-60 border-l-text dark:border-d-60 border-2 bottom-2 py-3 rounded-xl hover:border-d-10 dark:hover:border-d-10">
      Effacer
    </button>
  </diV>
</template>

<script>
export default {
  methods:{
    handleClic: function (number){
      this.$emit('handlePavNum',number)
    }
  }
}
</script>
