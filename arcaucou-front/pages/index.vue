<template>

  <main class='bg-l-background min-h-screen dark:bg-d-background text-l-text dark:text-d-text'>
    <SudokuGrid :gridStart="gridStart"/>
  </main>
</template>

<script>
export default {
  layout:'main',
  name: 'Arc',
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
              [2,5,0,0,7,4,3,0,0]]
    }
  },
}
</script>
