<template>
  <main class='min-h-screen bg-l-background dark:bg-d-background text-l-text dark:text-d-text w-full h-full top-0 left-0 z-0'>
    <Timer :running="this.isRunningTimer" :nextGame="this.alreadyPlay" :secondsStart="this.secondsStart" class="pt-10 mb-4"/>
    <div v-if="!this.alreadyPlay">
      <div class="mx-auto w-1/2 h-20 text-center">
        <button v-if="!this.isRunningTimer" @click="this.startGame" class="text-sm font-semibold border px-4 py-2 rounded-lg hover:border-l-10">Commencer</button>
      </diV>
      <SudokuGrid class="mb-10" :gridStart="this.grid"/>
      <NumPav @handlePavNum="this.handlePavNum"/>
    </div>
    <div v-else class="mx-auto w-1/2 text-center">
      <p class="text-3xl">Bravo ! Vous avez déjà résolu le Sudoku. Revenez demain pour une nouvelle partie !</p>
    </diV>
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
      title: 'Arc Au Cou',
      bodyAttrs: {
        class:'scrollbar-thin scrollbar-thumb-l-10 dark:scrollbar-thumb-d-60 scrollbar-track-gray overflow-y-scroll scrollbar-thumb-rounded-full scrollbar-track-rounded-full'
      }
    };
  },
  computed: mapState([
    'grid',
    'win',
    'wrong',
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
    alreadyPlay: false,
    time: 0,
    secondsStart: 0,
    }
  },
  methods: {
    handlePavNum(number) {
      this.$store.commit('changeValue', number)
    },
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
      setTimeout(()=>{this.stopConfetti()}, 2500);
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
      this.$axios.get('/sudoku/get_sudoku').then(result => {
        this.isRunningTimer = true;
        this.$store.commit('initGrid', this.setupGridObject(result.data.sudoku));
      }).catch(error => {
        this.$toasted.global.defaultError({
          msg: 'Oupss... une erreur est survenue'
        })
      })
    },
    startCooldown: function(){
      this.alreadyPlay = true;
      let today = new Date()
      let tomorrow = new Date(today)
      tomorrow.setDate(tomorrow.getDate() + 1)
      tomorrow.setHours(0)
      tomorrow.setMinutes(0)
      tomorrow.setSeconds(0)
      this.secondsStart = Math.abs(today - tomorrow) / 1000
      this.isRunningTimer = true;
    }
  },
  watch:{
    win:function(){
      this.startConfetti();
      this.alreadyPlay = true;
      this.toggleModal();
      this.startCooldown();

      let today = new Date()
      let tomorrow = new Date(today)
      tomorrow.setDate(tomorrow.getDate() + 1)
      tomorrow.setHours(0)
      tomorrow.setMinutes(0)
      tomorrow.setSeconds(0)
      const age = Math.abs(today - tomorrow) / 1000
      this.$cookies.set('sudoku-win', true, {
        path: '/',
        maxAge: age,
      })
    },
    wrong: function(){
      if(this.wrong){
        this.$toasted.global.defaultError({
            msg: "Le sudoku n'est pas correct !"
        })
      }
    },
  },
  mounted() {
    const cookieWin = this.$cookies.get('sudoku-win');
    if(!cookieWin){
      this.$store.commit('initGrid', this.setupGridObject(this.gridStart));
      window.addEventListener('keydown', (e) =>{
        switch(e.key){
          case 'ArrowUp':
            e.preventDefault();
            this.$store.commit('moveSelectCell', 'up')
            break;
          case 'ArrowDown':
            e.preventDefault();
            this.$store.commit('moveSelectCell', 'down')
            break;
          case 'ArrowLeft':
            e.preventDefault();
            this.$store.commit('moveSelectCell', 'left')
            break;
          case 'ArrowRight':
            e.preventDefault();
            this.$store.commit('moveSelectCell', 'right')
            break;
        }
      });
    }else{
      this.startCooldown();
    }

  }
}
</script>
