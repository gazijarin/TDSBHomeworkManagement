<template>
  <div>
    <navbar></navbar>
    <h1>Courses</h1>
    <p>This is the courses page</p>
  </div>
</template>

<script>
import navbar from '../navbar/navbar';

export default {
  name: 'Courses', //this is the name of the component
  components: {
    'navbar': navbar
  }
}
</script>
<style>
</style>
