<template>
  <main class='pt-10 bg-l-background min-h-screen dark:bg-d-background text-l-text dark:text-d-text'>
    <div class="flex">
      <div class="mt-7">
        <input type="text" placeholder="Nom du group" class="mt-1 pl-3 block w-full border-none bg-gray-100 dark:bg-d-background h-11 rounded-xl shadow-lg focus:border-green-gemme">
      </div>

      <div class="mt-7">
        <input type="password" placeholder="Mot de passe" class="mt-1 pl-3 block w-full border-none bg-gray-100 dark:bg-d-background h-11 rounded-xl shadow-lg focus:border-green-gemme">
      </div>
    </diV>
  </main>
</template>

<script>
export default {
  layout:'main',
  name: 'groups',
  head() {
    return {
      title: 'Arc Au Cou - Groups'
    };
  },
  data: function() {
    return {
    }
  },
}
</script>
