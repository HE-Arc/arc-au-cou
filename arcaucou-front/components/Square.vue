<template>
  <div>
    <div @click="handleSelect" v-if="cell.value != 0" class="text-center h-10 w-10" :class="[!this.cell.isSelected ? 'dark:bg-d-border' : 'dark:background-darker']">
      {{cell.value}}
    </div>
    <div @click="handleSelect" v-if="cell.value === 0" class="text-center h-10 w-10" :class="[!this.cell.isSelected ? 'dark:bg-d-border' : 'dark:background-darker']">

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
        this.$store.commit('changeValue', {x:this.posX, y:this.posY, number:typed})
      }
    },
    handleSelect: function(){
      if(!this.cell.isLocked) this.$store.commit('selectCell', {x:this.posX, y:this.posY});
    }
  },
  mounted() {
    if(!this.cell.isLocked) window.addEventListener('keypress', this.changeValue);
  },
  destroyed() {
    if(!this.cell.isLocked) window.removeEventListener('keypress', this.changeValue);
  }
}
</script>
