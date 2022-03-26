<template>
  <div class="z-10 fixed bg-l-60 dark:bg-d-30 text-l-text dark:text-d-text font-sans w-full">
	<div class="bg-white shadow">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between py-4">
        <div class="flex-1">
          <div class="flex items-start">
            <NuxtLink to="/leaderboard">
              <svg v-if="$colorMode.preference == 'dark' || $colorMode.preference == 'system'" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" viewBox="0 0 20 20" fill="currentColor">
                <path d="M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z" />
              </svg>
              <svg v-if="$colorMode.preference == 'light'" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </NuxtLink>
            <NuxtLink to="/groups" class="ml-5">
              <svg v-if="$colorMode.preference == 'dark' || $colorMode.preference == 'system'" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 dark:text-d-10" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
              </svg>

              <svg v-if="$colorMode.preference == 'light'" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-l-background" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
            </NuxtLink>
          </div>
        </div>

        <div class="flex-0">
          <h1 class="text-4xl mr-4"><NuxtLink to="/">Arc Au Cou</NuxtLink></h1>
        </div>

        <div class="flex-1">
          <div class="flex justify-end items-center mr-5">
            <div v-if="$auth.loggedIn">
              <p>{{ $auth.user.username }}</p>
            </div>
            <div v-else>
              <NuxtLink to="/login" class="text-gray-800 text-sm font-semibold mr-4">Sign in</NuxtLink>
              <NuxtLink to="/register" class="text-gray-800 text-sm font-semibold border px-4 py-2 rounded-lg hover:border-l-background dark:hover:border-d-10 mr-4">Sign up</NuxtLink>
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

