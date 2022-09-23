import { createApp } from 'vue'
import { apolloClient } from '@/apollo-config'
import App from './App.vue'
import "./index.css"
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.use(router)

app.use(apolloClient)

app.use(createPinia())

app.mount('#app')
