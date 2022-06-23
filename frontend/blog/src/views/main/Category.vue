<template>
  <div>
    <h1 class="text-5xl font-extrabold mb-2">Category Name</h1>
    <p class="text-gray-500 text-lg mb-5">
      A blog created with Django, Vue.js and TailwindCSS
    </p>

    <post-list></post-list>
  </div>
</template>

<script>
// @ is an alias to /src
import PostList from "@/components/PostList.vue";

export default {
  components: { PostList },
  name: "CategoryView",
};
</script>