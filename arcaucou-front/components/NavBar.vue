<template>
  <div class="z-10 bg-l-60 dark:bg-d-30 text-l-text dark:text-d-text font-sans w-full">
	<div class="bg-white shadow">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between py-4">
        <div class="hidden md:block flex-1">
          <!-- Icones -->
          <div class="flex items-start">
            <NuxtLink to="/leaderboard">
              <div v-if="$colorMode.preference == 'dark' || $colorMode.preference == 'system'" >
                <svg v-if="!this.leaderboard" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              </div>
              <div v-else>
                <svg v-if="this.leaderboard" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              </div>
            </NuxtLink>
            <NuxtLink to="/groups" class="ml-5">
              <div v-if="$colorMode.preference == 'dark' || $colorMode.preference == 'system'" >
                <svg v-if="!this.group" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <div v-else>
                <svg v-if="this.group" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
            </NuxtLink>
            <NuxtLink to="/rules" class="ml-5">
              <div v-if="$colorMode.preference == 'dark' || $colorMode.preference == 'system'" >
                <svg v-if="!this.rules" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path stroke-linecap="round" stroke-linejoin="round" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div v-else>
                <svg v-if="this.rules" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path stroke-linecap="round" stroke-linejoin="round" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
            </NuxtLink>
          </div>
        </div>

        <!-- Title -->
        <div class="flex-0">
          <h1 class="text-4xl text-d-text mr-4 font-bold"><NuxtLink to="/">Arc Au Cou</NuxtLink></h1>
        </div>

        <!-- User and theme -->
        <div class="flex-1">
          <div class="flex justify-end items-center mr-5">
            <div v-if="$auth.loggedIn" class="hidden md:flex">
              <p class="text-xl font-semibold text-d-text">{{ this.$auth.user.username }}</p>
              <button @click="this.handleLogout" class="text-d-text dark:text-d-text dark:hover:text-d-10 hover:text-d-10 text-xl font-semibold ml-5 mr-4">Déconnexion</button>
            </div>
            <div v-else class="hidden md:block">
              <NuxtLink to="/login" class="text-d-text dark:text-d-text hover:text-l-10 dark:hover:text-d-10 text-xl font-semibold mr-4">Connexion</NuxtLink>
              <NuxtLink to="/register" class="text-d-text dark:text-d-text hover:text-d-10 dark:hover:text-d-10 text-xl font-semibold border px-4 py-2 rounded-lg hover:border-l-10 dark:hover:border-d-10 mr-4">S'inscrire</NuxtLink>
            </div>

            <button v-if="$colorMode.preference == 'dark' || $colorMode.preference == 'system'"
            @click="$colorMode.preference = 'light'">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd" />
            </svg>
            </button>
            <button v-if="$colorMode.preference == 'light'"
              @click="$colorMode.preference = 'dark'">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
              </svg>
            </button>
            <button @click="isHamburger = !isHamburger" class="ml-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="block md:hidden h-10 w-10 dark:text-d-10 text-l-background" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- Hamburger menu -->
    <div>
      <ul v-if="isHamburger" class="flex flex-col ml-5 p-3 font-semibold gap-3">
        <li><NuxtLink to="/leaderboard" :class="this.leaderboard ? 'text-d-10 dark:text-d-10' : 'text-d-text  dark:text-d-text'">Classement</NuxtLink></li>
        <li><NuxtLink to="/groups" :class="this.group ? 'text-d-10 dark:text-d-10' : 'text-d-text  dark:text-d-text'">Groupe</NuxtLink></li>
        <li><NuxtLink to="/rules" :class="this.rules ? 'text-d-10 dark:text-d-10' : 'text-d-text  dark:text-d-text'">Règles</NuxtLink></li>
        <div v-if="!$auth.loggedIn" class="flex flex-col gap-3">
          <li><NuxtLink to="/login" class="text-d-text  dark:text-d-text font-semibold">Connexion</NuxtLink></li>
          <li><NuxtLink to="/register" class="text-d-text  dark:text-d-text font-semibold">S'inscrire</NuxtLink></li>
        </div>
        <li v-else><button @click="this.handleLogout" class="text-d-text dark:text-d-text font-semibold">Déconnexion</button></li>
      </ul>
    </div>
  </div>
</div>
</template>

<script>
export default {
  colorMode: 'dark',
  props: {
    leaderboard: {
      type: Boolean,
      required: false,
    },
    group: {
      type: Boolean,
      required: false,
    },
    rules: {
      type: Boolean,
      required: false,
    }
  },
  data: function() {
    return {
      isHamburger: false,
    }
  },
  methods:{
    /**
     * Handle logout
     */
    handleLogout: function() {
      this.$auth.logout();
    }
  }
}
</script>

