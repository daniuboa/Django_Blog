<template>
  <div class="home">
    <div class="flex flex-col place-items-center border-b-2">
      <!-- Featured Image and title -->
      <img src="..." class="w-full my-5" />
      <h1 class="text-center text-5xl font-extrabold mb-5">Post Title</h1>
      <p class="text-gray-500 text-lg mb-2">March 3, 2022 - By Eric Hu</p>
    </div>

    <!-- Tags -->
    <div class="flex flex-wrap my-4">
      <div class="mr-5 text-sm font-medium">Tags:</div>
      <router-link
        class="
          mr-5
          text-sm
          font-medium
          uppercase
          text-teal-500
          hover:underline hover:text-teal-700
        "
        to="/tag"
        >Tag Name</router-link
      >
      ...
    </div>

    <!-- Main content -->
    <div class="py-5 font-serif space-y-4">Lorem Lipsum ...</div>

    <!-- Like, Comment and Share -->
    ...

    <!-- Comment Section -->
    ...
  </div>
</template>

<script></script>