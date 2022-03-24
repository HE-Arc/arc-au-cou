<template>
  <div class="font-sans bg-l-background dark:bg-d-background text-l-text dark:text-d-text fixed w-full h-full top-0 left-0 z-0">
    <div class="relative min-h-screen flex flex-col sm:justify-center items-center">
        <div class="relative sm:max-w-sm w-full">
            <div class="card bg-l-10 dark:bg-d-10 shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
            <div class="card bg-l-10 dark:bg-d-10 shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
            <div class="relative w-full rounded-3xl  px-6 py-4 bg-l-60 dark:bg-d-60 shadow-md">
                <h1 class="block mt-3 text-xl text-center font-semibold">
                    Login
                </h1>
                <form @submit.prevent="handleLogin" class="mt-10">
                    <div>
                        <input type="text" v-model="userData.username" placeholder="Username" class="mt-1 pl-3 block w-full border-none bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
                    </div>

                    <div class="mt-7">
                        <input type="password" v-model="userData.password" placeholder="Password" class="mt-1 pl-3 block w-full border-none bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
                    </div>

                    <div class="mt-7">
                        <button class="mb-4 bg-l-background dark:bg-d-30 border-l-10 dark:border-d-10 border-2 bottom-2 w-full py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                            Login
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
      title: 'Arc Au Cou - Login'
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
      try {
        await this.$auth.loginWith('local', {"user":{"username": this.userData.username, "password": this.userData.password}})
        //await this.$auth.$storage.setUniversal('email', response.data.email)
        //await this.$auth.setUserToken(response.data.accestoken, reponse.data.refresh)
        this.$toasted.global.defaultSuccess({
          msg: 'Bienvenu ' + this.userData.username
        })
      } catch (err) {
        this.$toasted.global.defaultError({
          msg: 'Oupsss... erreur lors de la connection'
        })
      }
    }
  }
}
</script>
