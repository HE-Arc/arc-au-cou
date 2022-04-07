<template>
  <div class="pt-52 sm:pt-0 dark:text-d-text">
    <div class="relative min-h-screen mx-auto w-10/12 flex flex-col sm:justify-center items-center">
        <div class="relative sm:max-w-sm w-full">
            <div class="card bg-l-10 dark:bg-d-10 shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
            <div class="card bg-l-10 dark:bg-d-10 shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
            <div class="relative rounded-3xl  px-6 py-4 bg-l-60 dark:bg-d-60 shadow-md">
                <h1 class="block mt-3 text-xl text-center font-semibold">
                    Se connecter
                </h1>
                <form @submit.prevent="handleLogin" class="mt-10">
                    <div>
                        <input type="text" v-model="userData.username" placeholder="Pseudo" class="mt-1 pl-3 block w-full border-none bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
                    </div>

                    <div class="mt-7">
                        <input type="password" v-model="userData.password" placeholder="Mot de passe" class="mt-1 pl-3 block w-full border-none bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
                    </div>

                    <div class="mt-7">
                        <button class="mb-4 bg-l-60 text-d-text dark:bg-d-30 font-semibold border-l-background dark:border-d-10 border-2 bottom-2 w-full py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                            Connexion
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

  </div>
</template>

<script>
export default {
  layout: 'main',
  name: 'login',
  head() {
    return {
      title: 'Arc Au Cou - Connexion',
      bodyAttrs: {
        class:'bg-l-background dark:bg-d-background scrollbar-thin scrollbar-thumb-l-10 dark:scrollbar-thumb-d-60 scrollbar-track-gray overflow-y-scroll scrollbar-thumb-rounded-full scrollbar-track-rounded-full'
      }
    };
  },
  data: function(){
    return {
      userData: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async handleLogin(){
      await this.$axios.post('/login', {'username': this.userData.username, 'password': this.userData.password}).then(result =>{
        try {
          this.$auth.loginWith('local', {
            data: this.userData
          })
          this.$toasted.global.defaultSuccess({
            msg: "Bienvenu " + this.userData.username
          })
        } catch (error) {
          this.$toasted.global.defaultError({
            msg: "Oupss... une erreur est survenue"
          })
        }
      }).catch(error => {
        this.$toasted.global.defaultError({
          msg: "Nom d'utilisateur ou mot de passe incorrect"
        })
      })
    }
  }
}
</script>
