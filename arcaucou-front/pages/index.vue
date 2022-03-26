<template>
  <main class='min-h-screen mt-16 bg-l-background dark:bg-d-background text-l-text dark:text-d-text fixed w-full h-full top-0 left-0 z-0'>
    <Timer :running="this.isRunningTimer" class="pt-10 mb-4"/>
    <div class="mx-auto w-1/2 h-20 text-center mb-4">
      <button v-if="!this.isRunningTimer" @click="this.startGame" class="text-sm font-semibold border px-4 py-2 rounded-lg hover:border-l-10">Commencer</button>
    </diV>
    <SudokuGrid class="mb-10" :gridStart="this.grid"/>
    <Modal v-show="isModal" @close-modal="isModal = false" :time="this.time"/>
  </main>
</template>

<script>
import { mapState } from 'vuex';

export default {
  layout:'main',
  name: 'index',
  head() {
    return {
      title: 'Arc Au Cou'
    };
  },
  computed: mapState([
    'grid',
    'win',
  ]),
  data: function() {
    return {
    gridStart :[[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]],
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
      setupGridObject(grid){
        return grid.map((row) => {
          return row.map((element) => {
            return {value: element, isLocked: element != 0, isSelected: false}
          })
        })
      },
      toggleModal: function(){
        this.isModal = !this.isModal
      },
      startGame: function(){
        this.isRunningTimer = true;

        this.$axios.get('/sudoku/get_sudoku').then(result => {
          console.log(result.data.sudoku);
          this.$store.commit('initGrid', this.setupGridObject(result.data.sudoku));
        }).catch(error => {
          this.$toasted.global.defaultError({
            msg: 'Oupss... problème serveur'
          })
        })
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
    this.$store.commit('initGrid', this.setupGridObject(this.gridStart));
  }
}
</script>
