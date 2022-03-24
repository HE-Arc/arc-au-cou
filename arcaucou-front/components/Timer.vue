<template>
  <div class="flex flex-row gap-5 justify-center">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-green-gemme" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
    <div class="text-center my-auto">
      <p>{{$moment('2015-01-01').startOf('day').seconds(time).format('mm:ss')}}</p>
    </diV>
  </div>
</template>

<script>
export default {
  name:"timer",
  props:{
    running: {
      type: Boolean,
      default: true
    }
  },
  data: function(){
    return {
      time: 0,
      timer: Function
    }
  },
  methods: {
    startTimer: function(){
      this.timer = setInterval(() => {
        this.time++;
      }, 1000);
    },
    reset: function(){
      clearInterval(this.timer);
      this.time = 0;
    }
  },
  watch:{
    running:function(){
      if(this.running){
        this.startTimer();
      }else{
        this.$store.commit('saveTime', this.time);
        this.reset();
      }
    }
  },
}
</script>
