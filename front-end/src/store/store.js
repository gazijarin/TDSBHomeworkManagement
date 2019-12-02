import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'
import Cookies from 'js-cookie'

Vue.use(Vuex);

const vuexCookie = new VuexPersistence({
  restoreState: (key) => Cookies.getJSON(key),
  saveState: (key, state) =>
    Cookies.set(key, state, {
      expires: 3
    }),
    
})


export default new Vuex.Store({
    state: {
      token: null,
      user: null,
      isUserLoggedIn: false
    },
    plugins: [vuexCookie.plugin],
    mutations: {
      setToken (state, token) {
        state.token = token;
        state.isUserLoggedIn = !!(token)
      },
      setUser (state, user) {
        state.user = user
      },
      setPrefix (state, prefix) {
        state.prefix = prefix
      }
    },
    actions: {
      setToken ({commit}, token) {
        commit('setToken', token)
      },
      
      setUser ({commit}, user) {
        commit('setUser', user)
      },

      setPrefix ({commit}, prefix) {
        commit('setPrefix', prefix)
      }
    }
  })