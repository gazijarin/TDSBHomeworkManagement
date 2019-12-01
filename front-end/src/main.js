import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
// Bootstrap imports.
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

Vue.use(BootstrapVue);
// Import fontawesome icons here.
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus, faUserCircle, faSearch, faEdit, faTrash, faSync } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


import store from '@/store/store'

if (
  process.env.NODE_ENV &&
  process.env.NODE_ENV == "production"
) {
  store.dispatch("setPrefix", "");
} else {
  store.dispatch("setPrefix", "http://localhost:5000");
}

import { sync } from 'vuex-router-sync'
sync(store, router);


// import GAuth from 'vue-google-oauth2'
import VueGoogleApi from 'vue-google-api'

Vue.use(VueGoogleApi, { clientId: '341686581297-255pa5934vd7ip80ubq5lhn56bhkb640.apps.googleusercontent.com', scope: 'email https://www.googleapis.com/auth/calendar.readonly https://www.googleapis.com/auth/classroom.courses.readonly',
prompt: 'select_account', fetch_basic_profile: false });
Vue.prototype.$axios = axios
// Make sure to add the icons to the library like this.
library.add(faPlus);
library.add(faUserCircle);
library.add(faSearch);
library.add(faEdit);
library.add(faTrash);
library.add(faSync);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
