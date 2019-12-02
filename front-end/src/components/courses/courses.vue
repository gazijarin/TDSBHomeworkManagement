<template>
  <div>
    <navbar></navbar>
    <h1>Courses</h1>
    <div id="tiles-container">
      <div class="class-tile" v-for="course in courseList" :key="course">
        <b-card
          :title=course.name
          :sub-title=course.instructor
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from '../navbar/navbar';

export default {
  name: 'Courses', //this is the name of the component
  components: {
    'navbar': navbar
  },
  data() {
    return {
      courseList: [{name: "CSC301", instructor: "Mike Davison"}, {name: "CSC373", instructor: "Karan Singh"}]
    };
  }
}
</script>
<style>
#tiles-container {
  text-align: left;
  margin: 40px;
}
.class-tile {
  margin: 10px;
  max-width: 20rem;
  display: inline-block;
  text-align: left;
}
</style>
