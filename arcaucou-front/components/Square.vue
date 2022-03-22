<template>
  <div>
    <div @click="handleSelect" v-if="number != 0" class="text-center h-10 w-10" :class="[!isSelected ? 'dark:bg-d-border' : 'dark:background-darker']">
      {{number}}
    </div>
    <div @click="handleSelect" v-if="number === 0" class="text-center h-10 w-10" :class="[!isSelected ? 'dark:bg-d-border' : 'dark:background-darker']">

    </div>
  </diV>
</template>

<script>
export default {
  props: {
    value: Number,
    posX: Number,
    posY: Number
  },
  data:function() {
    return {
      number: this.value,
      isSelected: false
    }
  },
  methods:{
    changeValue: function(e){
      if (this.isSelected){
        let typed = parseInt(String.fromCharCode(e.keyCode),10);
        // if it was NaN, split out
        if(!typed) return;
        console.log(typed);
        this.number = typed;
        this.isSelected = false;
        this.$store.commit('changeValue', {x:this.posX, y:this.posY, number:this.number})
      }
    },
    handleSelect: function(){
      this.isSelected = !this.isSelected;
    }
  },
  mounted() {
    window.addEventListener('keypress', this.changeValue);
  },
  destroyed() {
    window.removeEventListener('keypress', this.changeValue);
  }
}
</script>
