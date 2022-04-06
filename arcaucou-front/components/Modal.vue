<template>
  <div @click="$emit('close-modal')" class="fixed w-full h-full top-0 left-0 z-0 flex items-center justify-center">
    <diV class="modal-overlay absolute w-full h-full bg-d-background opacity-50"></div>
      <div class="modal-container bg-l-60 dark:bg-d-60 p-10 w-11/12 md:max-w-md mx-auto border-2 rounded border-l-10 shadow-lg z-50 overflow-y-auto">
        <h1 class="mb-9 text-3xl w-1/2 text-center mx-auto">Bravo !</h1>
        <p class="text-xl">Vous avez résolu le sudoku en {{$moment('2015-01-01').startOf('day').seconds(time).format('mm:ss')}} !</p><br>
        <div v-if="this.$auth.loggedIn">
          <p class="text-xl">Votre score a été sauvegardé dans le classement.</p>
          <p class="text-xl">Revenez demain pour un prochain Sudoku !</p>
          <button @click="$emit('close-modal')" class="text-sm font-semibold mt-5 border px-4 py-2 rounded-lg hover:border-d-10">Ok</button>
        </div>
        <div v-else>
          <p class="text-xl">Pour sauvegarder votre score, connectez-vous</p>
          <div class="w-1/2 mx-auto">
            <NuxtLink to="/login" class="mx-auto">
              <button class="mt-5 w-full bg-l-background dark:bg-d-30 border-l-10 dark:border-d-10 border-2 bottom-2 py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                Se connecter
              </button>
            </NuxtLink>
            <NuxtLink to="/register" class="mx-auto">
              <button class="mt-5 w-full bg-l-background dark:bg-d-30 border-l-10 dark:border-d-10 border-2 bottom-2 py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
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
