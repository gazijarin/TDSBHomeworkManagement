import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
// Bootstrap imports.
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);
// Import fontawesome icons here.
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus, faUserCircle, faSearch } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


import store from '@/store/store'
import { sync } from 'vuex-router-sync'
sync(store, router);


// import GAuth from 'vue-google-oauth2'
import VueGoogleApi from 'vue-google-api'

Vue.use(VueGoogleApi, { clientId: '341686581297-255pa5934vd7ip80ubq5lhn56bhkb640.apps.googleusercontent.com', scope: 'email https://www.googleapis.com/auth/calendar.readonly', prompt: 'select_account', fetch_basic_profile: true });

// Make sure to add the icons to the library like this.
library.add(faPlus);
library.add(faUserCircle);
library.add(faSearch);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
