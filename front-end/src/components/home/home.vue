<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <!-- <div class="slanted" style="background-color: #79BC6D; margin-left: -20%; z-index: -5;"></div>
    <div class="slanted" style="background-color: #FCB711; margin-left: -10%; z-index: -6;"></div>
    <div class="slanted" style="background-color: #4277A5; margin-left: -5%; z-index: -7;"></div>
    <div class="slanted" style="background-color: #EC7B1C; margin-left: 0%; z-index: -8;"></div> -->
    <h2 class="headline mb-0">
      <b>
        Welcome,
        <span v-if="user !== null">{{ user.first_name }}</span>
        <span v-else>Student.</span>
      </b>
    </h2>
    <div class="col-5" style="float: right; margin-top: 20px; padding-top: 15px;">
      <b-card border-variant="dark">
        <FullCalendar
          :header="calendarHeader"
          :plugins="calendarPlugins"
          defaultView="dayGridMonth"
          :events="events"
        ></FullCalendar>
      </b-card>
      <br />
      <!-- <b-card border-variant="dark" header="Progress" align="left">
        <FullCalendar :header="false"
        :plugins="taskPlugins"
        defaultView="listWeek"
        :events="events"></FullCalendar>
      </b-card>-->
    </div>
    <div class="col-7" style="padding-top: 15px; margin-top: 20px">
      <b-card class="today-container" border-variant="dark" header-tag="header" align="left">
        <template v-slot:header>
          <h6 class="mb-0">Today</h6>
        </template>
        <b-card-body style="margin-top: -25px; margin-bottom: -15px;">
          <FullCalendar
            :header="false"
            :height="20"
            :plugins="todayPlugins"
            defaultView="dayGridDay"
            :events="events"
          ></FullCalendar>
        </b-card-body>
      </b-card>
    </div>
    <div class="col-7" style="padding-top: 2%">
      <!-- <b-card border-variant="light" header-tag="header" align="left"></b-card>
            <template v-slot:header>
        <h6 class="mb-0">Header Slot</h6>
      </template>-->
      <b-card header-tag="header" border-variant="dark" align="left">
        <template v-slot:header>
          <h6 class="mb-0">Recently Added</h6>
        </template>
          <div style="max-height: 350px; overflow-y: scroll;">
            <div class="div-list" :key="idx" v-for="(item, idx) in events">
              {{ user.first_name }} added {{ item.title }} on

              <span>{{ item.created | formatDate }}</span>
            </div>
          </div>
            

        
       
      </b-card>
    </div>
  </div>
</template>

<script>
import FullCalendar from "@fullcalendar/vue";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import listPlugin from "@fullcalendar/list";
import navbar from "../navbar/navbar";
import moment from "moment";

export default {
  name: "Home", //this is the name of the component
  components: {
    navbar: navbar,
    FullCalendar // make the <FullCalendar> tag available
  },
  beforeMount() {
    this.loadTasks();
  },
  data() {
    return {
      events: [
      ],
      recentlyadded: [
      { message: 'Do Math Homework' },
      { message: 'Do science project' }
      ],
      calendarHeader: {
        left: "prev",
        center: "title",
        right: "next"
      },
      taskListConfig: {
        defaultView: "weekList"
      },
      todayPlugins: [dayGridPlugin],
      calendarPlugins: [dayGridPlugin, timeGridPlugin, listPlugin],
      taskPlugins: [listPlugin]
    };
  },
  computed: {
    user() {
      return this.$store.state.user;
    }
  }, 
  filters: {
    formatDate: function(value) {
      if (value) {
        var adjust_time_zone = new Date(value);
        adjust_time_zone.setHours(adjust_time_zone.getHours() - 5);
        return moment(String(adjust_time_zone)).format('MM/DD/YYYY hh:mm')
      }
  }
  },
  methods: {
       loadTasks: function() {
      var self = this;

      this.$axios
        .get(
          this.$store.state.prefix + "/api/task/student?id=" +
            this.$store.state.user._id
        )
        .then(response => {
          response.data.forEach(function(item) {
            self.$data.events.push({
              id: item._id,
              title: item.title,
              start: item.deadline,
              course: item.course,
              description: item.description,
              attachments: item.attachments,
              created: item.created,
              grade: item.grade,
              progress: item.progress
            });
          });
        });
    }
  }
};
</script>

<style lang='scss'>
@import "~@fullcalendar/core/main.css";
@import "~@fullcalendar/list/main.css";

.slanted {
  height: 100%;
  width: 60%;
  position: fixed;
  top: 0;
  left: -40%;
  overflow: hidden;
  transform: skewX(0deg);
  transition: left 1s;
}
.slanted:hover {
  left: -38%;
}
.div-list {
  border-top: 1px solid #e6e3e4;
  border-bottom: 1px solid #e6e3e4;
  height: 40px;
  padding: 10px;
  margin-top: 5px;
}
</style>
