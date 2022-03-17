<template>
  <div class="font-sans bg-l-background dark:bg-d-background dark:text-d-text">
    <div class="relative min-h-screen flex flex-col sm:justify-center items-center">
        <div class="relative sm:max-w-sm w-full">
            <div class="card dark:bg-green-gemme shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
            <div class="card dark:bg-green-gemme shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
            <div class="relative w-full rounded-3xl  px-6 py-4 dark:bg-d-background-night shadow-md">
                <h1 class="block mt-3 text-xl text-gray-700 text-center font-semibold">
                    Login
                </h1>
                <form @submit.prevent="handleLogin" class="mt-10">
                    <div>
                        <input type="text" v-model="userData.username" placeholder="Username" class="mt-1 pl-3 block w-full border-none bg-gray-100 dark:bg-d-background h-11 rounded-xl shadow-lg focus:border-green-gemme">
                    </div>

                    <div class="mt-7">
                        <input type="password" v-model="userData.password" placeholder="Password" class="mt-1 pl-3 block w-full border-none bg-gray-100 dark:bg-d-background h-11 rounded-xl shadow-lg focus:border-green-gemme">
                    </div>

                    <div class="mt-7">
                        <button class="mb-4 border-green-gemme border-2 bottom-2 w-full py-3 rounded-xl shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
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
  name: 'Arc Au Cou - Login',
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
        await this.$auth.loginWith('local', {data: userData})
        await this.$auth.$storage.setUniversal('email', response.data.email)
        await this.$auth.setUserToken(response.data.accestoken, reponse.data.refresh)
        this.$toasted.global.defaultSuccess({
          msg: 'Good'
        })
      } catch (err) {
        this.$toasted.global.defaultError({
          msg: 'Error'
        })
      }
    }
  }
}
</script>
