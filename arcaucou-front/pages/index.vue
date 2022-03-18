<template>
  <main class='bg-l-background min-h-screen dark:bg-d-background text-l-text dark:text-d-text'>
    <Timer :running=true class="pt-10 mb-4"/>
    <div class="mx-auto w-1/2 text-center mb-4">
      <button class="text-gray-800 text-sm font-semibold border px-4 py-2 rounded-lg hover:text-purple-600 hover:border-green-gemme">Commencer</button>
    </diV>
    <div class="mx-auto w-1/2 text-center mb-4">
      <button @click="start" class="text-gray-800 text-sm font-semibold border px-4 py-2 rounded-lg hover:text-purple-600 hover:border-green-gemme">Start</button>
    </diV>
    <div class="mx-auto w-1/2 text-center mb-4">
      <button @click="stop" class="text-gray-800 text-sm font-semibold border px-4 py-2 rounded-lg hover:text-purple-600 hover:border-green-gemme">Stop</button>
    </diV>
    <SudokuGrid class="mb-10" :gridStart="gridStart"/>
    <Rules/>
  </main>
</template>

<script>
export default {
  layout:'main',
  name: 'index',
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
    started: false
    }
  },
  methods: {
      start() {
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
      },

      stop() {
        this.$confetti.stop();
      },
    }
}
</script>
