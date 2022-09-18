import { createApp } from 'vue'
import timeago from 'vue-timeago3'
import BootstrapVue3 from 'bootstrap-vue-3'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faPlus } from '@fortawesome/free-solid-svg-icons'
library.add(faPlus)

import App from './App.vue'

import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import 'bootswatch/dist/darkly/bootstrap.css'

const app = createApp(App)
app.use(timeago)
app.use(BootstrapVue3)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
