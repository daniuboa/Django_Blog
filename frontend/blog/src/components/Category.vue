<script>
// @ is an alias to /src
import PostList from "@/components/PostList.vue";
import { POSTS_BY_CATEGORY } from "@/queries";

export default {
  components: {
    PostList,
  },
  name: "CategoryView",

  data() {
    return {
      postsByCategory: null,
    };
  },

  async created() {
    const postsByCategory = await this.$apollo.query({
      query: POSTS_BY_CATEGORY,
      variables: {
        category: this.$route.params.slug,
      },
    });
    this.postsByCategory = postsByCategory.data.postsByCategory;
  },
};
</script>