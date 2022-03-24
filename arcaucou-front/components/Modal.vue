<template>
  <div @click="$emit('close-modal')" class="fixed w-full h-full top-0 left-0 flex items-center justify-center">
    <diV class="modal-overlay absolute w-full h-full bg-d-background-darker opacity-50"></div>
      <div class="modal-container dark:bg-d-background-night p-10 w-11/12 md:max-w-md mx-auto border-2 rounded border-green-gemme shadow-lg z-50 overflow-y-auto">
        <h1 class="mb-9">Bravo !</h1>
        <p>Vous avez résolu le sudoku en {{$moment('2015-01-01').startOf('day').seconds(time).format('mm:ss')}} !</p>
        <p>Votre score a été sauveagrder dans le classement général.</p>
        <p>Revenez demain pour un prochain Sudoku !</p>
        <button @click="$emit('close-modal')" class="text-gray-800 text-sm font-semibold mt-5 border px-4 py-2 rounded-lg hover:border-green-gemme">Ok</button>
      </diV>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: mapState([
    'time'
  ]),
}
</script>
