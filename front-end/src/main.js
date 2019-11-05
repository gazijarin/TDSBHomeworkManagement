import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
// Bootstrap imports.
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'fullcalendar/dist/fullcalendar.css'
Vue.use(BootstrapVue)
// Import fontawesome icons here.
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus, faUserCircle, faSearch } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import FullCalendar from 'vue-full-calendar'

// Make sure to add the icons to the library like this.
library.add(faPlus)
library.add(faUserCircle)
library.add(faSearch)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(FullCalendar)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
