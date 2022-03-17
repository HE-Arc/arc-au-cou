<template>
  <div class="flex flex-row gap-5 justify-center">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-green-gemme" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
    <div class="text-center my-auto">
      <p>{{ time | secondsInMinutes }}</p>
    </diV>
  </div>
</template>

<script>
import moment from "moment";

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
      time: 0
    }
  },
  mounted() {
    if(this.running) this.startTimer();
  },
  methods: {
    startTimer: function(){
      this.time = setInterval(() => {
        this.time++;
      }, 1000);
    },
    reset: function(){
      this.time = 0;
    }
  },
  filters: {
    secondsInMinutes: function(seconds) {
      return moment("2015-01-01")
        .startOf("day")
        .seconds(seconds)
        .format("mm:ss");
    }
  }
}
</script>
