<template>
  <div class="post-list">
    <ul v-if="publishedPosts" class="divide-y divide-gray-200">
      <li class="py-12">
        <article>
          <div
            class="
              space-y-2
              xl:grid xl:grid-cols-4 xl:items-baseline xl:space-y-0
            "
          >
            <dl>
              <dt class="sr-only">Published on</dt>
              <dd
                class="
                  text-base
                  font-medium
                  leading-6
                  text-gray-500
                  dark:text-gray-400
                "
              >
                <time>March 3, 2022</time>
              </dd>
            </dl>
            <div class="space-y-5 xl:col-span-3">
              <div class="space-y-6">
                <div>
                  <h2 class="text-2xl font-bold leading-8 tracking-tight">
                    <router-link class="text-gray-900" to="/post"
                      >This is a post title</router-link
                    >
                  </h2>
                  <router-link
                    class="
                      text-sm
                      font-medium
                      uppercase
                      text-teal-500
                      hover:underline hover:text-teal-700
                    "
                    to="/category"
                    >Category</router-link
                  >
                </div>
                <div class="prose max-w-none text-gray-500">
                  Lorem Lipsum ...
                </div>
              </div>
              <div class="text-base font-medium leading-6">
                <router-link
                  class="text-teal-500 hover:underline hover:text-teal-700"
                  to="/post"
                  >Read more →</router-link
                >
              </div>
            </div>
          </div>
        </article>
      </li>
      ...
    </ul>
  </div>
</template>

<script>
export default {
  name: "PostListComponent",
};
</script>