import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./main.css";
import { apolloClient } from "@/apollo-config";

createApp(App)
  .use(router)
  .use(apolloClient)
  .mount("#app");

const app = createApp(App);

app.use(router);

app.mount("#app");
