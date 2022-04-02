<template>
  <main class='min-h-screen bg-l-background dark:bg-d-background text-l-text dark:text-d-text w-full h-full top-0 left-0 z-0'>
    <Timer :isClock="this.isClock" :isCooldown="this.isCooldown" :timeCooldown="this.timeCooldown" :isSave="this.isSave" class="pt-10 mb-4"/>
    <div v-if="!this.alreadyPlay">
      <div class="mx-auto w-1/2 h-20 text-center">
        <button v-if="!this.isClock && !this.alreadyPlay " @click="this.startGame" class="text-sm font-semibold border px-4 py-2 rounded-lg hover:border-l-10">Commencer</button>
      </diV>
      <SudokuGrid class="mb-10" :gridStart="this.grid"/>
      <NumPav @handlePavNum="this.handlePavNum"/>
    </div>
    <div v-else class="mx-auto w-1/2 text-center">
      <p class="text-3xl">Revenez demain pour une nouvelle partie !</p>
    </diV>
    <Modal v-show="isModal" @close-modal="isModal = false"/>
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
    'time',
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
    isClock: false,
    isCooldown: false,
    isSave: false,
    timeSave: false,
    timeCooldown: 0,
    alreadyPlay: false,
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
        this.isClock = true;
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
      this.timeCooldown = Math.abs(today - tomorrow) / 1000
      this.isClock = false;
      this.isCooldown = true;
    },
    saveToLeaderBoard: function(){
      this.$axios.post('/leaderboard/', {'time': this.time})
      this.timeSave = true;
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
    }
  },
  watch:{
    win:function(){
      this.startConfetti();
      this.alreadyPlay = true;
      this.toggleModal();
      this.isSave = true;
      this.startCooldown();
    },
    wrong: function(){
      if(this.wrong){
        this.$toasted.global.defaultError({
            msg: "Le sudoku n'est pas correct !"
        })
      }
    },
    time: function(){
      this.saveToLeaderBoard();
    }
  },
  updated(){
    if(this.$auth.loggedIn && this.time > 0 && !this.timeSave){
      this.saveToLeaderBoard()
    }
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
