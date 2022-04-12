<template>
  <div @click="$emit('close-modal')" class="fixed w-full h-full top-0 left-0 z-0 flex items-center justify-center">
    <diV class="modal-overlay absolute w-full h-full bg-d-background opacity-50"></div>
      <div class="modal-container bg-l-60 dark:bg-d-60 p-10 w-10/12 sm:w-8/12 lg:w-1/2 xl:w-1/3 mx-auto border-2 rounded border-l-10 shadow-lg z-50 overflow-y-auto">
        <h1 class="mb-9 text-3xl w-1/2 text-center mx-auto text-d-text">Bravo !</h1>
        <p class="text-xl text-d-text">Vous avez résolu le sudoku en {{$moment('2015-01-01').startOf('day').seconds(time).format('mm:ss')}} !</p><br>
        <!--
          If the user is connected
        -->
        <div v-if="this.$auth.loggedIn">
          <p class="text-xl text-d-text">Votre score a été sauvegardé dans le classement.</p>
          <p class="text-xl text-d-text">Revenez demain pour un prochain Sudoku !</p>
          <button @click="$emit('close-modal')" class="text-sm font-semibold mt-5 border px-4 py-2 rounded-lg hover:border-d-10">Ok</button>
        </div>
        <!--
          If the user is not coneected, we display a button to connect
        -->
        <div v-else>
          <p class="text-xl text-d-text">Pour sauvegarder votre score, connectez-vous.</p>
          <div class="w-full sm:w-1/3 mx-auto mt-5">
            <NuxtLink to="/login" class="mx-auto">
              <button class="mb-4 font-semibold text-d-text bg-l-60 dark:bg-d-30 border-l-text dark:border-d-10 p-3 hover:border-d-10 focus:border-d-10 dark:hover:border-d-text dark:focus:border-d-text border-2 bottom-2 w-full py-3 rounded-xl">
                Se connecter
              </button>
            </NuxtLink>
            <NuxtLink to="/register" class="mx-auto">
              <button class="mb-4 font-semibold text-d-text bg-l-60 dark:bg-d-30 border-l-text dark:border-d-10 p-3 hover:border-d-10 focus:border-d-10 dark:hover:border-d-text dark:focus:border-d-text border-2 bottom-2 w-full py-3 rounded-xl">
                S'inscrire
              </button>
            </NuxtLink>
          </div>
        </div>
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
