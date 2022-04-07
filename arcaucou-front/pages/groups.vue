<template>
  <div>
    <NavBar :group="true"/>
    <main class='text-l-text dark:text-d-text'>
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
        <p>Rejoindre un groupe, vous permet de vous mesurer à vos amis. Un classement spécial est reservé aux groupes en dessous du classement général.</p>
        <br>
        <div class="mt-4">
            <input type="text" v-model="groupData.name" placeholder="Nom du groupe" class="mt-1 pl-3 block w-full border-l-10 border-2 bg-l-background dark:border-d-30 dark:bg-d-30 h-11 rounded-xl shadow-lg dark:focus:border-d-10 focus:border-d-10">
        </div>

        <div class="mt-7">
            <input type="password" v-model="groupData.password" placeholder="Mot de passe" class="mt-1 pl-3 block w-full border-l-10 border-2 dark:border-d-30 bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
        </div>

        <div class="mt-7 flex mb-10">
            <button @click="handleCreate" class="w-1/2 mb-4 font-semibold text-d-text bg-l-60 dark:bg-d-30 border-l-text dark:border-d-10 p-3 hover:border-d-10 focus:border-d-10 dark:hover:border-d-text dark:focus:border-d-text border-2 bottom-2 py-3 rounded-xl">
                Créer
            </button>
            <button @click="handleJoin" class="w-full ml-5 mb-4 font-semibold text-d-text bg-l-60 dark:bg-d-30 border-l-text dark:border-d-10 p-3 hover:border-d-10 focus:border-d-10 dark:hover:border-d-text dark:focus:border-d-text border-2 bottom-2 py-3 rounded-xl">
                Rejoindre
            </button>
        </div>
      </diV>
    </main>
  </div>
</template>

<script>
export default {
  name: 'groups',
  middleware: 'auth',
  head() {
    return {
      title: 'Arc Au Cou - Groupe',
      bodyAttrs: {
        class:'bg-l-background dark:bg-d-background scrollbar-thin scrollbar-thumb-l-10 dark:scrollbar-thumb-d-60 scrollbar-track-gray overflow-y-scroll scrollbar-thumb-rounded-full scrollbar-track-rounded-full'
      }
    };
  },
  data: function() {
    return {
      groupsList: [],
      groupData: {
        name: '',
        password: ''
      },
      hasGroup: false,
    }
  },
  methods:{
    getGroups: function(){
      this.groupsList = []
      this.$axios.get("/group/").then(result => {
        result.data.forEach(name => {
          this.groupsList.push(name);
        });
        this.hasGroup = true;
      }).catch(error => {
        this.$toasted.global.defaultError({
            msg: "Oupss... une erreur est survenue"
        })
      })
    },
    handleCreate: function(){
      this.$axios.post('/group/',
        {'name': this.groupData.name, 'password': this.groupData.name},
        ).then(result => {
        this.$toasted.global.defaultSuccess({
            msg: this.groupData.name + " a été créé !"
        })
        this.hasGroup = true;
        this.resetForm();
        this.getGroups();
      }).catch(error => {
        this.$toasted.global.defaultError({
            msg: "Oupss... le nom du groupe existe déjà !"
        })
      })
    },
    handleJoin: function(){
      this.$axios.post('/group/joingroup/',
        {'name': this.groupData.name, 'password': this.groupData.name},
        ).then(result => {
        this.$toasted.global.defaultSuccess({
            msg: "Vous avez rejoind " + this.groupData.name
        })
        this.hasGroup = true;
        this.resetForm();
        this.getGroups();
      }).catch(error => {
        this.$toasted.global.defaultError({
            msg: error.response.data.failed
        })
      })
    },
    handleQuit: function(name){
      this.$axios.post('/group/leavegroup/',
        {'name': name},
        ).then(result => {
        this.$toasted.global.defaultSuccess({
            msg: "Vous avez quitté " + name
        })
        this.resetForm();
        this.getGroups();
      }).catch(error => {
        this.$toasted.global.defaultError({
            msg: error.response.data.failed
        })
      })
    },
    resetForm: function(){
      this.groupData.name = '';
      this.groupData.password = '';
    }
  },
  mounted() {
    this.getGroups();
  }
}
</script>
