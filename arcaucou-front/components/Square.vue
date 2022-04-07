<template>
  <div class="text-lg md:text-3xl">
    <div @click="handleSelect" v-if="cell.value != 0"
    class="mx-auto dark:bg-d-30 border-2 dark:border-d-background text-center h-8 md:h-10 w-8 md:w-10"
    :class="[!this.cell.isSelected ? 'border-d-text' : 'dark:border-d-10', this.cell.isLocked ? 'dark:text-d-10 text-l-text' : 'text-d-text']">
      {{cell.value}}
    </div>
    <div @click="handleSelect" v-if="cell.value === 0"
    class="mx-auto dark:bg-d-30 border-2 dark:border-d-background text-center h-8 md:h-10 w-8 md:w-10"
    :class="[!this.cell.isSelected ? 'border-d-text' : 'dark:border-d-10', this.cell.isLocked ? 'dark:text-d-10 text-l-text' : 'text-d-text']">

    </div>
  </diV>
</template>

<script>
export default {
  props: {
    cell: Object,
    posX: Number,
    posY: Number
  },
  methods:{
    changeValue: function(e){
      if (this.cell.isSelected){
        let typed = parseInt(String.fromCharCode(e.keyCode),10);
        if(!typed) return;
        this.$store.commit('changeValue', typed)
      }
    },
    handleSelect: function(){
      if(!this.cell.isLocked) this.$store.commit('selectCell', {x:this.posX, y:this.posY});
    }
  },
  mounted() {
    if(!this.cell.isLocked) window.addEventListener('keypress', this.changeValue);
  },
  unmounted() {
    if(!this.cell.isLocked) window.removeEventListener('keypress', this.changeValue);
  }
}
</script>
