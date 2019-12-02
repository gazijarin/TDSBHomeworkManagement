<template>
  <div>
    <navbar></navbar>
    <h1>Courses</h1>
    <div id="tiles-container">
      <div class="class-tile" v-for="course in courseList" :key="course" v-on:click="loadTasks(course._id, course.name)">
        <b-card
          :title=course.name
          :sub-title=course.instructor
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top>
        </b-card>
      </div>
    </div>


    <div id="tasks_popup" v-if="show_popup">
      <a class="boxclose" id="boxclose" v-on:click="close_popup()"></a>
      <b-card
        :title=curr_course
        sub-title="Here are your tasks for this course:"
        >
          <div class="class-tile" v-for="task in tasks" :key="task">
            <b-card
              :title=task.title
              :sub-title=task.deadline>
              <b-card-text>
                {{task.description}}
              </b-card-text>
            </b-card>
          </div>
      </b-card>

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
      courseList: this.$store.state.user.courses,
      tasks: [],
      show_popup: false,
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
          self.$data.show_popup = true;
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
    },
    close_popup: function() {
      this.$data.show_popup = false;
    }
  },
  beforeMount() {
  }
}
</script>
<style>
#tasks_popup {
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  position: fixed;
  margin: 0;
  padding-left: 10%;
  padding-right: 10%;
  padding-bottom: 10%;
  padding-top: 100px;
  background-color: rgba(0, 0, 0, 0.5);
  overflow: auto;
}
a.boxclose{
    float: right;
    margin-top:-30px;
    margin-right: -30px;
    cursor: pointer;
    color: #fff;
    border: 1px solid #AEAEAE;
    border-radius: 30px;
    background: #605F61;
    font-size: 31px;
    font-weight: bold;
    display: inline-block;
    line-height: 0px;
    padding: 11px 3px;
}

.boxclose:before {
    content: "×";
}

#tiles-container {
  text-align: left;
  margin: 40px;
}
.class-tile {
  margin: 10px;
  max-width: 20rem;
  display: inline-block;
  text-align: left;
  cursor: pointer;
}
</style>
