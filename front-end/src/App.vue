<template>
  <div id="app">
    <navbar></navbar>
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
import navbar from './components/navbar/navbar'
export default {
  name: 'app',
  components: {
    'navbar': navbar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  background-image: url('./assets/background.jpg');
}
</style>