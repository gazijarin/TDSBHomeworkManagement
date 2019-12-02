<template>
  <div>
    <navbar></navbar>
    <h1>Courses</h1>
    <div id="tiles-container">
      <div class="class-tile" v-for="course in courseList" :key="course" v-b-modal="'tasks_popup'" v-on:click="loadTasks(course._id, course.name)">
        <b-card
          :title=course.name
          :sub-title=course.instructor
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top>
        </b-card>
      </div>
    </div>

    <b-modal id="tasks_popup" size="xl" :title=curr_course hide-footer="true">
      <div id="tasks_popup_text">Here are your tasks for this course:</div>
      <div class="task-tile" v-for="task in tasks" :key="task">
        <b-card
          :title=task.title
          :sub-title=task.deadline>
          <b-card-text>
            {{task.description}}
          </b-card-text>
        </b-card>
      </div>
    </b-modal>
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
      courseList: this.$store.state.user.courses,
      tasks: [],
      curr_course: ""
    };
  },
  methods: {
    loadTasks: function(id_of_course, name_of_course) {
      var self = this;

      this.$axios
        .get(
          this.$store.state.prefix + "/api/task/student/course?student=" +
            this.$store.state.user._id + "&course=" + name_of_course
        )
        .then(response => {
          self.$data.tasks = [];
          response.data.forEach(function(item) {
            let deadline = new Date(item.deadline);

            self.$data.tasks.push({
              id: item._id,
              title: item.title,
              deadline_date_string: item.deadline,
              deadline: self.formatDate(deadline),
              course: item.course_id,
              description: item.description
            });
          });
          self.$data.tasks.sort(self.compareDates);
          self.$data.curr_course = name_of_course;
        });
    },
    formatDate: function(date) {
      var hours = date.getHours();
      var minutes = date.getMinutes();
      var ampm = hours >= 12 ? 'pm' : 'am';
      hours = hours % 12;
      hours = hours ? hours : 12; // the hour '0' should be '12'
      minutes = minutes < 10 ? '0'+minutes : minutes;
      var strTime = hours + ':' + minutes + ' ' + ampm;
      return date.getMonth()+1 + "/" + date.getDate() + "/" + date.getFullYear() + "  " + strTime;
    },
    compareDates: function(a, b) {
      let a_date = new Date(a.deadline_date_string);
      let b_date = new Date(b.deadline_date_string);

      if (a_date.getTime() < b_date.getTime()){
        return -1;
      }
      if (a_date.getTime() > b_date.getTime()){
        return 1;
      }
      return 0;
    }
  },
  beforeMount() {
  }
}
</script>
<style>
#tasks_popup_text {
  margin-bottom: 10px;
  font-size: 110%;
}

#tiles-container {
  text-align: left;
  margin: 40px;
}
.class-tile {
  overflow: hidden;
  margin: 10px;
  max-width: 20rem;
  display: inline-block;
  text-align: left;
  cursor: pointer;
}
.task-tile {
  max-width: 22%;
  margin: 10px;
  display: inline-block;
  text-align: left;
}
</style>
