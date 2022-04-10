<template>
  <div>
    <NavBar :rules="true" />
    <main class='text-l-text dark:text-d-text mx-auto w-full sm:w-10/12 md:w-1/2 lg:1/3 p-2'>
      <section class="mb-20">
        <h1 class="text-3xl mb-5 font-semibold">Arc Au Cou</h1>
        <p class="text-2xl">Chaque jour Arc Au Cou vous propose de résoudre un sudoku. Vous êtes chronomètré et le but est de finir le sudoku le plus rapidement possible.</p>
        <p class="text-2xl">Si vous créez un compte votre temps est enregistré et vous pouvez vous mesurer au autres joueurs d’Arc Au Cou !</p>
      </section>
      <section class="mb-20">
        <h1 class="text-3xl mb-5 font-semibold">Comment jouer ?</h1>
        <p class="text-2xl">Sur la page principale se trouve le sudoku, quand vous êtes prêt vous pouvez appuyer sur "Commencer" pour démarrer le chronomètre.</p>
        <p class="text-2xl">Vous pouvez remplir les cases du sudoku en cliquant sur l'une des cases et en appuyant soit sur votre clavier ou via le pavé numérique en dessous du sudoku.</p>
        <p class="text-2xl">Si vous avez fait une erreur, vous pouvez l'effacer avec la touche "Backspace" ou le bouton "Effacer" sur le pavé numérique.</p>
      </section>
      <section class="mb-20">
        <h1 class="text-3xl mb-5 font-semibold">Le classement</h1>
        <p class="text-2xl">Un classement général vous permet de vous mesurer aux autres joueurs d’Arc Au Cou.</p>
        <p class="text-2xl">Si vous avez rejoint un groupe vous pouvez visualiser un classement avec seulement les membres du groupe.</p>
      </section>
      <section class="mb-20">
        <h1 class="text-3xl mb-5 font-semibold">Les groupes</h1>
        <p class="text-2xl">Vous pouvez créer et rejoindre un groupe avec un nom et un mot de passe qui n'est pas obligatoire. Sur la page du classement, vous pouvez sélectionner votre groupe et voir seulement le score de vos amis.</p>
      </section>
    </main>
  </div>
</template>


<script>
export default {
  name: 'index',
  head() {
    return {
      title: 'Arc Au Cou - Règles',
      bodyAttrs: {
        class:'pb-5 bg-l-background dark:bg-d-background scrollbar-thin scrollbar-thumb-l-10 dark:scrollbar-thumb-d-60 scrollbar-track-gray overflow-y-scroll scrollbar-thumb-rounded-full scrollbar-track-rounded-full'
      }
    };
  },
}
</script>
