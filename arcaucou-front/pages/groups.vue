<template>
  <main class='mt-16 bg-l-background min-h-screen dark:bg-d-background text-l-text dark:text-d-text fixed w-full h-full top-0 left-0 z-0'>
    <div v-if="hasGroup" class="mx-auto px-3 pt-20 sm:pt-6 sm:px-6 md:w-1/2 2xl:w-1/4">
      <div class="grid grid-cols-2 mx-auto mt-10 gap-y-8">
        <div class="text-center col-span-2">
          <h2 class="text-2xl">Vos groupes</h2>
        </div>
        <div class="">
          <p>Nom</p>
        </div>
        <div class="text-center">
          <p>Quitter</p>
        </div>
      </div>
      <div class="grid grid-cols-2 mx-auto" v-for="name in groupsList" :key="name">
        <p class="my-auto text-xl">{{name}}</p>
        <div  class="w-full">
          <svg @click="handleQuit(name)" xmlns="http://www.w3.org/2000/svg" class="mx-auto h-10 w-10 cursor-pointer hover:text-red dark:hover:text-red dark:text-d-10" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
          </svg>
        </div>
      </div>
    </div>
    <div class="mt-20 mx-auto px-3 md:w-1/2 2xl:w-1/4">
      <h1 class="text-2xl">Rejoindre ou créer un groupe</h1>
      <br>
      <p>Rejoindre un groupe, vous permet de vous ... avec vos amis. Un classement spécial est reservé aux groupes en dessous du classement général.</p>
      <br>
      <div class="mt-4">
          <input type="text" v-model="groupData.name" placeholder="Nom du groupe" class="mt-1 pl-3 block w-full border-l-10 border-2 bg-l-background dark:border-d-30 dark:bg-d-30 h-11 rounded-xl shadow-lg dark:focus:border-d-10 focus:border-d-10">
      </div>

      <div class="mt-7">
          <input type="password" v-model="groupData.password" placeholder="Mot de passe" class="mt-1 pl-3 block w-full border-l-10 border-2 dark:border-d-30 bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
      </div>

      <div class="mt-7 flex">
          <button @click="handleCreate" class="w-1/2 bg-l-background dark:bg-d-30 border-l-10 dark:border-d-10 border-2 bottom-2 py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
              Créer
          </button>
          <button @click="handleJoin" class="w-full ml-5 bg-l-background dark:bg-d-30 border-l-10 dark:border-d-10 border-2 bottom-2 py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
              Rejoindre
          </button>
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
      groupsList: ['Les arbres', 'Les boufs'],
      groupData: {
        name: '',
        password: ''
      },
      hasGroup: true,
    }
  },
  methods:{
    handleCreate: function(){
      this.$axios.post('/group/', {'name': this.groupData.name, 'password': this.groupData.name}, {headers: {'Authorization': this.$store.state.token}}).then(result => {
        this.$toasted.global.defaultSuccess({
            msg: this.groupData.name + " a été créé !"
        })
        //.name
      }).catch(error => {
        this.$toasted.global.defaultError({
            msg: "Oupss... le groupe n'a pas été créé !"
        })
      })
    },
    handleJoin: function(){
      console.log("Join");
    },
    handleQuit: function(name){
      console.log(name);
    }
  },
  mounted() {
    this.$axios.get("/group/", {headers: {'Authorization': this.$store.state.token}}).then(result => {
        console.log(result.data);
      }).catch(error => {
        this.$toasted.global.defaultError({
            msg: "Oupss... problème serveur"
        })
      })
  }
}
</script>
