<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from '@/components/HelloWorld.vue'
</script>

<template>
   <div class="container mx-auto max-w-3xl px-4 sm:px-6 xl:max-w-5xl xl:px-0">
    <div class="flex flex-col justify-between h-screen">
      <header class="flex flex-row items-center justify-between py-10">
        <div class="nav-logo text-2xl font-bold">
          <router-link to="/">Django Vue Starter Blog</router-link>
        </div>
        <div class="nav-links hidden sm:block">
          <router-link
            to="/"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Home</router-link
          >
          <router-link
            to="/categories"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Category</router-link
          >
          <router-link
            to="/tags"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Tag</router-link
          >
        </div>
      </header>

      <router-view />

      <footer class="flex flex-col place-items-center mt-5 py-5 border-t-2">
        <div class="mb-3 flex space-x-4">
          <i
            class="fa-brands fa-linkedin text-3xl text-gray-700 hover:text-teal-700"
          ></i>
        </div>
        <div class="mb-3 flex space-x-1 text-sm text-gray-700">
          <div>
            <a
              href="https://www.ericsdevblog.com"
              class="hover:underline hover:text-teal-700"
              >Eric Hu</a
            >
          </div>
          <div>•</div>
          <div>© 2022</div>
          <div>•</div>
          <a href="/" class="hover:underline hover:text-teal-700"
            >Vue.js Starter Blog</a
          >
        </div>
      </footer>
    </div>
  </div>
  <RouterView />
</template>

<style>

</style>
