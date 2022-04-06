<template>
  <div>
    <NavBar :leaderboard="true" />
    <main class='text-l-text dark:text-d-text'>
      <div class="pt-20 sm:pt-6 mx-auto sm:w-1/2">
        <div class="grid grid-cols-3 mt-10 mx-auto mb-5">
          <div class="text-center col-span-3 mb-5">
            <h2 class="text-3xl">Classement général</h2>
          </div>
          <div class="text-center text-2xl">
            <p>#</p>
          </div>
          <div class="text-center text-2xl">
            <p>Pseudo</p>
          </div>
          <div class="text-center text-2xl">
            <p>Temps</p>
          </div>
        </div>
        <div class="grid grid-cols-3  mx-auto mb-2" v-for="(row,index) in dataLeaderboard" :key="index">
          <div class="text-center text-2xl">
            <p>{{index+1}}</p>
          </div>
          <div class="text-center text-2xl">
            <p>{{row[0]}}</p>
          </div>
          <div class="text-center text-2xl">
            <p>{{$moment('2015-01-01').startOf('day').seconds(row[1]).format('mm:ss')}}</p>
          </div>
        </div>
      </diV>

      <div v-if="hasGroup" class="mt-20 px-3 mx-auto sm:w-1/2">
        <div class="grid grid-cols-3  mx-auto mb-5">
          <div class="text-center col-span-3 mb-5">
            <h2 class="text-3xl">Classement de groupe</h2>
          </div>
          <div class="text-center col-span-3 mb-5">
            <select name="groups" @change="getLeaderboardGroup" v-model="selectedGroup" class="w-1/2 bg-l-60 dark:bg-d-30 text-d-text border-2 rounded">
              <option disabled value="">Sélectionner un groupe</option>
              <option v-for="group in groupsList" :key="group">
                  {{group}}
              </option>
          </select>
          </div>
          <div class="text-center text-2xl">
            <p>#</p>
          </div>
          <div class="text-center text-2xl">
            <p>Pseudo</p>
          </div>
          <div class="text-center text-2xl">
            <p>Temps</p>
          </div>
        </div>
        <div class="grid grid-cols-3  mx-auto mb-2" v-for="(row,index) in dataLeaderboardGroup" :key="index">
          <div class="text-center text-2xl">
            <p>{{index+1}}</p>
          </div>
          <div class="text-center text-2xl">
            <p>{{row[0]}}</p>
          </div>
          <div class="text-center text-2xl">
            <p>{{$moment('2015-01-01').startOf('day').seconds(row[1]).format('mm:ss')}}</p>
          </div>
        </div>
      </div>

      <div v-else class="flex flex-col items-center mt-20 px-3 mx-auto sm:w-1/2 mb-10">
        <h2 class="text-3xl text-center mb-5">Classement group</h2>
        <p class="text-2xl">Pour vous mesurer à vos amis, rejoignez ou créez un groupe via le menu des groupes.</p>
        <NuxtLink to="/groups" class="mx-auto">
          <button class="mt-5 w-72 bg-l-background dark:bg-d-30 border-l-10 dark:border-d-10 border-2 bottom-2 py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
            Direction les groupes
          </button>
        </NuxtLink>


      </diV>
    </main>
  </div>
</template>

<script>
export default {
  name: 'leaderboard',
  head() {
    return {
      title: 'Arc Au Cou - Classement',
      bodyAttrs: {
        class:'bg-l-background dark:bg-d-background scrollbar-thin scrollbar-thumb-l-10 dark:scrollbar-thumb-d-60 scrollbar-track-gray overflow-y-scroll scrollbar-thumb-rounded-full scrollbar-track-rounded-full'
      }
    };
  },
  data: function() {
    return {
      dataLeaderboard :[],
      dataLeaderboardGroup: [],
      groupsList:[],
      selectedGroup: '',
      hasGroup : false,
    }
  },
  methods:{
    getLeaderboardMain(){
      this.$axios.get('/leaderboard/').then(result => {
        this.dataLeaderboard = []
        result.data.forEach(element => {
          let newUser = []
          Object.keys(element).forEach((key) => {
            newUser.push(element[key])
          })
          this.dataLeaderboard.push(newUser)
        })
      }).catch(error => {
        this.$toasted.global.defaultError({
          msg: 'Oupss... une erreur est survenue'
        })
      })
    },
    getLeaderboardGroup(){
      this.$axios.post('/leaderboard/list_group/', {'name': this.selectedGroup}).then(result => {
        this.dataLeaderboardGroup = []
        result.data.forEach(element => {
          let newUser = []
          Object.keys(element).forEach((key) => {
            newUser.push(element[key])
          })
          this.dataLeaderboardGroup.push(newUser)
        })
      }).catch(error => {
        this.$toasted.global.defaultError({
          msg: 'Oupss... une erreur est survenue'
        })
      })
    },
    getGroups: function(){
      if(this.$auth.loggedIn){
        this.groupsList = []
        this.$axios.get("/group/").then(result => {
          if(result.data.length > 0){
            result.data.forEach(name => {
              this.groupsList.push(name);
            });
            this.hasGroup = true;
          }
        }).catch(error => {
          this.$toasted.global.defaultError({
              msg: "Oupss... problème serveur"
          })
        })
      }
    },
  },
  mounted() {
    this.getLeaderboardMain();
    this.getGroups();
  }
}
</script>
