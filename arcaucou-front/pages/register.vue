<template>
  <div class="font-sans pt-52 sm:pt-0 bg-l-background dark:bg-d-background dark:text-d-text w-full h-full top-0 left-0 z-0">
    <div class="relative min-h-screen mx-auto w-10/12 flex flex-col sm:justify-center items-center">
        <div class="relative sm:max-w-sm w-full">
            <div class="card bg-l-10 dark:bg-d-10 shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
            <div class="card bg-l-10 dark:bg-d-10 shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
            <div class="relative w-full rounded-3xl  px-6 py-4 bg-l-60 dark:bg-d-60 shadow-md">
                <h1 class="block mt-3 text-xl text-center font-semibold">
                    S'inscrire
                </h1>
                <form @submit.prevent="handleRegister" class="mt-10">
                    <div>
                        <input type="text" placeholder="Pseudo" v-model="userData.username" class="mt-1 pl-3 block w-full border-none bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
                    </div>
                    <br>
                    <div>
                        <input type="email" placeholder="Email" v-model="userData.email" class="mt-1 pl-3 block w-full border-none bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
                    </div>
                    <br>
                    <div>
                        <input type="password" placeholder="Mot de passe" v-model="userData.password" class="mt-1 pl-3 block w-full border-none bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
                    </div>
                    <br>
                    <div>
                        <input type="password" placeholder="Confirmer le mot de passe" v-model="userData.password2" class="mt-1 pl-3 block w-full border-none bg-l-background dark:bg-d-30 h-11 rounded-xl shadow-lg focus:border-d-10">
                    </div>

                    <div class="mt-7">
                        <button class="mb-4 font-semibold text-d-text bg-l-60 dark:bg-d-30 border-l-text dark:border-d-10 p-3 hover:border-d-10 focus:border-d-10 dark:hover:border-d-text dark:focus:border-d-text border-2 bottom-2 w-full py-3 rounded-xl">
                            Création du compte
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
  name: 'register',
  head() {
    return {
      title: 'Arc Au Cou - Inscription',
      bodyAttrs: {
        class:'scrollbar-thin scrollbar-thumb-l-10 dark:scrollbar-thumb-d-60 scrollbar-track-gray overflow-y-scroll scrollbar-thumb-rounded-full scrollbar-track-rounded-full'
      }
    };
  },
  data: function(){
    return {
      userData:{
        username: "",
        email: "",
        password: "",
        password2: ""
      },
    }
  },
  methods:{
    /**
     * Handle register
     */
    handleRegister: async function(){
      await this.$axios.post('/register', {"username": this.userData.username, "email": this.userData.email, "password": this.userData.password, "password2": this.userData.password2}).then((result) => {
        this.$toasted.global.defaultSuccess({
          msg: 'Votre compté à été créé'
        });

        try {
          this.$auth.loginWith('local', {
            data: this.userData
          })
          this.$auth.setUser(this.userData);
          this.$toasted.global.defaultSuccess({
            msg: "Bienvenu " + this.userData.username
          })
        } catch (error) {
          this.$toasted.global.defaultError({
            msg: "Oupss... une erreur est survenue"
          })
        }

      }).catch((error) => {
        Object.keys(error.response.data).forEach((key) => {
          this.$toasted.global.defaultError({
          msg: error.response.data[key]
          })
        });
      });
    },
  }
}
</script>
