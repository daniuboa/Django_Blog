<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import gql from "graphql-tag";
import { SITE_INFO } from "@/queries";

export default {
  data() {
    return {
      mySite: null,
    };
  },

  async created() {
    const siteInfo = await this.$apollo.query({
      query: gql`
        query {
          site {
            name
          }
        }
      `,
    });
    this.mySite = siteInfo.data.site;
  },

  async created() {
    const siteInfo = await this.$apollo.query({
      query: SITE_INFO,
    });
    this.mySite = siteInfo.data.site;
  },
};
</script>

<template>
  <div class="container mx-auto max-w-3xl px-4 sm:px-6 xl:max-w-5xl xl:px-0">
    <div class="flex flex-col justify-between h-screen">
      <header class="flex flex-row items-center justify-between py-10">
        <div class="nav-logo text-2xl font-bold">
          <router-link to="/">{{ mySite.name }}</router-link>
        </div>
      </header>
    </div>
  </div>
  <header>
    <img
      alt="Vue logo"
      class="logo"
      src="@/assets/logo.svg"
      width="125"
      height="125"
    />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
      <h1 class="text-3xl font-bold underlone">Hello World!</h1>

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>
</style>
