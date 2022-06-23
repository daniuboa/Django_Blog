<template>
  <div class="flex flex-col place-content-center place-items-center">
    <div class="py-8 border-b-2">
      <h1 class="text-5xl font-extrabold">All Categories</h1>
    </div>
    <div class="flex flex-wrap py-8">
      <router-link
        class="my-2 mr-5 text-sm font-medium uppercase text-teal-500 hover:underline hover:text-teal-700"
        to="/category"
        >Category Name</router-link
      >
      <router-link
        class="my-2 mr-5 text-sm font-medium uppercase text-teal-500 hover:underline hover:text-teal-700"
        to="/category"
        >Category Name</router-link
      >
      ...
    </div>
  </div>
</template>

<script>
export default {
  name: "CategoriesView",
};
</script>