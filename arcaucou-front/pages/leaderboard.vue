<template>
  <main class='pt-10 bg-l-background min-h-screen dark:bg-d-background text-l-text dark:text-d-text'>
    <div>
      <div class="grid grid-cols-4  mx-auto w-1/2 mb-5">
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
      <div class="grid grid-cols-4  mx-auto w-1/2 mb-2" v-for="(row,index) in dataLeaderboard" :key="index">
        <div class="text-center">
          <p>{{index+1}}</p>
        </div>
        <div class="text-center">
          <p>{{row[0]}}</p>
        </div>
        <div class="text-center">
          <p>{{row[1]}}</p>
        </div>
        <div class="text-center">
          <p>{{row[2]}}</p>
        </div>
        <div class="text-center">
          <p>{{row[3]}}</p>
        </div>
      </div>
    </diV>

    <div class="mt-20">
      <div class="grid grid-cols-4  mx-auto w-1/2 mb-5">
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
      <div class="grid grid-cols-4  mx-auto w-1/2 mb-2" v-for="(row,index) in dataLeaderboard" :key="index">
        <div class="text-center">
          <p>{{index+1}}</p>
        </div>
        <div class="text-center">
          <p>{{row[0]}}</p>
        </div>
        <div class="text-center">
          <p>{{row[1]}}</p>
        </div>
        <div class="text-center">
          <p>{{row[2]}}</p>
        </div>
        <div class="text-center">
          <p>{{row[3]}}</p>
        </div>
      </div>
    </div>

    <div>

    </diV>

  </main>
</template>

<script>
export default {
  layout:'main',
  name: 'leaderboard',
  data: function() {
    return {
    dataLeaderboard :[["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"],
                      ["Bob", 500 , "Les arbres"]],
    }
  },
}
</script>
