<template>
  <div>
    <navbar></navbar>
    <h1>Progress</h1>
    <p>This is the progress page</p>
  </div>
</template>

<script>
import navbar from '../navbar/navbar';

export default {
  name: 'Progress', //this is the name of the component
  components: {
    'navbar': navbar
  }
}
</script>
<style>
</style>