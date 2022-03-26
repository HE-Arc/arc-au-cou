<template>
  <main class='mt-16 bg-l-background min-h-screen dark:bg-d-background text-l-text dark:text-d-text fixed w-full h-full top-0 left-0 z-0'>
    <div class="pt-20 sm:pt-6 mx-auto sm:w-1/2">
      <div class="grid grid-cols-4 mt-10 mx-auto mb-5">
        <div class="text-center col-span-4 mb-5">
          <h2 class="text-2xl">Classement général</h2>
        </div>
        <div class="text-center">
          <p>#</p>
        </div>
        <div class="text-center">
          <p>Pseudo</p>
        </div>
        <div class="text-center">
          <p>Temps</p>
        </div>
        <div class="text-center">
          <p>Team</p>
        </div>
      </div>
      <div class="grid grid-cols-4  mx-auto mb-2" v-for="(row,index) in dataLeaderboard" :key="index">
        <div class="text-center">
          <p>{{index+1}}</p>
        </div>
        <div class="text-center">
          <p>{{row[0]}}</p>
        </div>
        <div class="text-center">
          <p>{{$moment('2015-01-01').startOf('day').seconds(row[1]).format('mm:ss')}}</p>
        </div>
        <div class="text-center">
          <p>{{row[2]}}</p>
        </div>
      </div>
    </diV>

    <div v-if="hasGroup" class="mt-20 px-3 mx-auto sm:w-1/2">
      <div class="grid grid-cols-4  mx-auto mb-5">
        <div class="text-center col-span-4 mb-5">
          <h2 class="text-2xl">Classement team</h2>
        </div>
        <div class="text-center">
          <p>#</p>
        </div>
        <div class="text-center">
          <p>Pseudo</p>
        </div>
        <div class="text-center">
          <p>Temps</p>
        </div>
        <div class="text-center">
          <p>Team</p>
        </div>
      </div>
      <div class="grid grid-cols-4  mx-auto mb-2" v-for="(row,index) in dataLeaderboard" :key="index">
        <div class="text-center">
          <p>{{index+1}}</p>
        </div>
        <div class="text-center">
          <p>{{row[0]}}</p>
        </div>
        <div class="text-center">
          <p>{{$moment('2015-01-01').startOf('day').seconds(100000).format('mm:ss')}}</p>
        </div>
        <div class="text-center">
          <p>{{row[2]}}</p>
        </div>
      </div>
    </div>

    <div v-if="!hasGroup" class="flex flex-col items-center mt-20 px-3 mx-auto sm:w-1/2">
      <h2 class="text-2xl text-center mb-5">Classement team</h2>
      <p>Pour vous mesurer à vos amis, rejoinger ou créer un groupe via le menu des groupes.</p>
      <NuxtLink to="/groups" class="mx-auto">
        <button class="mt-5 w-72 bg-l-background dark:bg-d-30 border-l-10 dark:border-d-10 border-2 bottom-2 py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
          Direction les groupes
        </button>
      </NuxtLink>


    </diV>
  </main>
</template>

<script>
export default {
  layout:'main',
  name: 'leaderboard',
  head() {
    return {
      title: 'Arc Au Cou - Leaderboard'
    };
  },
  data: function() {
    return {
    dataLeaderboard :[["Bob", 1000 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"]],
      hasGroup : false,
    }
  }
}
</script>
