<template>
  <main class='bg-l-background min-h-screen dark:bg-d-background text-l-text dark:text-d-text'>
    <Timer :running="this.isRunningTimer" class="pt-10 mb-4"/>
    <div class="mx-auto w-1/2 h-20 text-center mb-4">
      <button v-if="!this.isRunningTimer" @click="this.startGame" class="text-gray-800 text-sm font-semibold border px-4 py-2 rounded-lg hover:border-green-gemme">Commencer</button>
    </diV>
    <SudokuGrid class="mb-10" :gridStart="this.grid"/>
    <Rules/>
    <Modal v-show="isModal" @close-modal="isModal = false" :time="this.time"/>
  </main>
</template>

<script>
import { mapState } from 'vuex';

export default {
  layout:'main',
  name: 'index',
  computed: mapState([
    'grid',
    'win'
  ]),
  data: function() {
    return {
    gridStart :[[3,0,6,5,2,0,0,8,7],
              [5,0,8,0,0,0,0,0,0],
              [4,0,0,0,0,0,0,3,1],
              [0,0,3,9,0,0,0,5,0],
              [0,1,8,6,3,0,0,9,0],
              [0,8,0,0,5,6,0,0,0],
              [1,3,0,0,0,0,0,0,5],
              [0,0,0,0,0,0,2,0,6],
              [2,5,0,0,7,4,3,0,0]],
    started: false,
    isModal: false,
    isRunningTimer: false,
    time: 0,
    }
  },
  methods: {
      startConfetti() {
        this.$confetti.start({
          particles: [
            {
              type: 'heart',
            },
            {
              type: 'rect',
            },
            {
              type: 'circle',
            },
          ],
          windSpeedMax: 0,
          dropRate: 5
        });
        setTimeout(()=>{this.stopConfetti()}, 2000);
      },

      stopConfetti() {
        this.$confetti.stop();
      },
      setupGridObject(){
        return this.gridStart.map((row) => {
          return row.map((element) => {
            return {value: element, isLocked: element != 0, isSelected: false}
          })
        })
      },
      toggleModal: function(){
        this.isModal = !this.isModal
      },
      startGame: function(){
        this.isRunningTimer = true
      }
    },
    watch:{
    win:function(){
      this.startConfetti();
      this.isRunningTimer = false;
      this.toggleModal();
    }
  },
    mounted() {
      this.$store.commit('initGrid', this.setupGridObject());
    }
}
</script>
