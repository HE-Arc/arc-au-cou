<template>
  <div class="grid grid-cols-3 gap-2 justify-center mx-auto w-10/12 sm:w-8/12 md:w-1/2 lg:w-1/4 xl:w-1/6">
    <div class="mx-auto w-full h-full" v-for="index in 9" :key="index" >
      <button @click="handleClic(index)" class="mb-4 w-full h-full text-2xl bg-l-background dark:bg-d-30 border-l-10 dark:border-d-10 border-2 bottom-2 py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
        {{index}}
      </button>
    </div>
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
