<template>
  <div class="bg-gray-100 dark:bg-d-background-darker text-l-text dark:text-d-text font-sans w-full">
	<div class="bg-white shadow">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between py-4">
        <div class="flex-1">
          <NuxtLink to="/leaderboard">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-green-gemme" viewBox="0 0 20 20" fill="currentColor">
              <path d="M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z" />
            </svg>
          </NuxtLink>
        </div>

        <div class="flex-0">
          <h1 class="text-4xl mr-4"><NuxtLink to="/">Arc Au Cou</NuxtLink></h1>
        </div>

        <div class="flex-1">
          <div class="flex justify-end items-center mr-5">
            <NuxtLink to="/login" class="text-gray-800 text-sm font-semibold mr-4">Sign in</NuxtLink>
            <NuxtLink to="/register" class="text-gray-800 text-sm font-semibold border px-4 py-2 rounded-lg hover:border-green-gemme mr-4">Sign up</NuxtLink>
            <button v-if="$colorMode.preference == 'dark' || $colorMode.preference == 'system'"
            @click="$colorMode.preference = 'light'">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-green-gemme" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd" />
            </svg>
          </button>
          <button v-if="$colorMode.preference == 'light'"
            @click="$colorMode.preference = 'dark'">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-green-gemme" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
            </svg>

          </button>
          </div>


        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  colorMode: 'dark',
}
</script>

