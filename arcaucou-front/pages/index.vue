<template>
  <main class='text-l-text dark:text-d-text focus:outline-none' tabindex="0" @keydown="moveCell">
    <Timer :isClock="this.isClock" :isCooldown="this.isCooldown" :timeCooldown="this.timeCooldown" :isSave="this.isSave" class="pt-10 mb-4"/>
    <div v-if="!this.alreadyPlay">
      <div class="mx-auto h-20 w-1/2 text-center">
        <button v-if="!this.isClock && !this.alreadyPlay " @click="this.startGame" class="text-xl text-d-text bg-l-60 dark:bg-d-30 border-l-text dark:border-d-10 border-2 bottom-2 p-3 rounded-xl hover:border-d-10 focus:border-d-10 dark:hover:border-d-text dark:focus:border-d-text">Commencer</button>
      </diV>
      <SudokuGrid class="mb-10 mt-2" :gridStart="this.grid"/>
      <NumPav @handlePavNum="this.handlePavNum"/>
    </div>
    <div v-else class="mx-auto w-full p-2 text-center">
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
        class:'pb-5 bg-l-background dark:bg-d-background scrollbar-thin scrollbar-thumb-l-10 dark:scrollbar-thumb-d-60 scrollbar-track-gray overflow-y-scroll scrollbar-thumb-rounded-full scrollbar-track-rounded-full'
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
      setTimeout(()=>{this.stopConfetti()}, 3000);
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
      if(this.$auth.loggedIn && this.time > 0 && !this.timeSave){
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
    moveCell: function(event){
      switch(event.key){
        case 'ArrowUp':
          event.preventDefault();
          this.$store.commit('moveSelectCell', 'up')
          break;
        case 'ArrowDown':
          event.preventDefault();
          this.$store.commit('moveSelectCell', 'down')
          break;
        case 'ArrowLeft':
          event.preventDefault();
          this.$store.commit('moveSelectCell', 'left')
          break;
        case 'ArrowRight':
          event.preventDefault();
          this.$store.commit('moveSelectCell', 'right')
          break;
      }
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
    this.saveToLeaderBoard()
  },
  mounted() {
    const cookieWin = this.$cookies.get('sudoku-win');
    if(!cookieWin){
      this.$store.commit('initGrid', this.setupGridObject(this.gridStart));
    }else{
      this.startCooldown();
    }

  }
}
</script>
