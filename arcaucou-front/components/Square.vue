<template>
  <div class="text-lg md:text-3xl">
    <!-- If the square contains a number -->
    <div @click="handleSelect" v-if="cell.value != 0"
    class="mx-auto border-2 text-center dark:bg-d-60 h-8 md:h-10 w-8 md:w-10"
    :class="[!this.cell.isSelected ? 'border-l-text dark:border-d-30' : 'border-l-10 dark:border-d-10', this.cell.isLocked ? 'dark:text-d-10 text-l-10' : 'text-l-text dark:text-d-text']">
      {{cell.value}}
    </div>
    <!-- If the square contains a number -->
    <div @click="handleSelect" v-if="cell.value === 0"
    class="mx-auto border-2 text-center dark:bg-d-60 h-8 md:h-10 w-8 md:w-10"
    :class="[!this.cell.isSelected ? 'border-l-text dark:border-d-30' : 'border-l-10 dark:border-d-10', this.cell.isLocked ? 'dark:text-d-10 text-l-10' : 'text-l-text dark:text-d-text']">

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
    /**
     * Handle the listener event on the square
     */
    changeValue: function(e){
      if (this.cell.isSelected){
        if(e.keyCode === 8){ //Bckspace
          this.$store.commit('changeValue', 0);
        }else{
          let number = 0;
          if(e.keyCode >= 97 && e.keyCode <= 105){ //Numbers pav. num.
            number = parseInt(String.fromCharCode(e.keyCode-48),10);

          }else{ //Numbers
            number = parseInt(String.fromCharCode(e.keyCode),10);
          }
          if(!number) return;
          this.$store.commit('changeValue', number);
        }
      }
    },
    /**
     * Handle the clic select
     */
    handleSelect: function(){
      if(!this.cell.isLocked) this.$store.commit('selectCell', {x:this.posX, y:this.posY});
    }
  },
  beforeMount(){
    //Remove all listeners
    if(!this.cell.isLocked) window.removeEventListener('keydown', this.changeValue);
  },
  mounted() {
    //Add keypress listener
    if(!this.cell.isLocked) window.addEventListener('keydown', this.changeValue);
  },
}
</script>
