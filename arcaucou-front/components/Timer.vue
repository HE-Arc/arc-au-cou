<template>
  <div class="flex flex-row gap-5 justify-center">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-l-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
    <div class="text-center text-2xl my-auto">
      <p v-if="!isCooldown">{{$moment('2015-01-01').startOf('day').seconds(time).format('mm:ss')}}</p>
      <p v-else>{{$moment('2015-01-01').locale('fr-ch').startOf('day').seconds(timeLeft).format('LTS')}}</p>
    </diV>
  </div>
</template>

<script>
import 'moment/locale/fr-ch';
export default {
  name:"timer",
  props:{
    isClock: Boolean,
    isCooldown: Boolean,
    isSave: Boolean,
    timeCooldown: Number,
  },
  data: function(){
    return {
      time: 0,
      timeLeft: 0,
      clock: {
        type: Function
      },
      cooldown: {
        type: Function
      }
    }
  },
  methods: {
    startClock: function(){
      this.clock = setInterval(() => {
        this.time++;
      }, 1000);
    },
    startCooldown: function(){
      this.cooldown = setInterval(() => {
        this.timeLeft--;
      }, 1000);
    },
    resetClock: function(){
      clearInterval(this.clock);
    }
  },
  watch:{
    isClock:function(){
      if(this.clock){
        this.startClock();
      }
    },
    isCooldown: function(){
      if(this.isCooldown){
        this.timeLeft = this.timeCooldown
        this.startCooldown();
      }
    },
    isSave: function(){
      if(this.isSave){
        this.$store.commit('saveTime', this.time);
        this.resetClock();
      }
    }
  },
}
</script>
