<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <div class="slanted" style="background-color: #79BC6D; margin-left: -20%; z-index: -5;"></div>
    <div class="slanted" style="background-color: #FCB711; margin-left: -10%; z-index: -6;"></div>
    <div class="slanted" style="background-color: #4277A5; margin-left: -5%; z-index: -7;"></div>
    <div class="slanted" style="background-color: #EC7B1C; margin-left: 0%; z-index: -8;"></div>
    <h2 class="headline mb-0">
      <b>
        Welcome,
        <span v-if="user !== null">{{ user.first_name }}</span>
        <span v-else>Student.</span>
      </b>
    </h2>
    <div class="col-5" style="float: right; margin-top: 20px; padding-top: 15px;">
      <b-card border-variant="light">
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
      <b-card class="today-container" border-variant="light" header-tag="header" align="left">
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
      <b-card header-tag="header" align="left">
        <template v-slot:header>
          <h6 class="mb-0">Recently Added</h6>
        </template>
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

export default {
  name: "Home", //this is the name of the component
  components: {
    navbar: navbar,
    FullCalendar // make the <FullCalendar> tag available
  },
  data() {
    return {
      events: [
        {
          title: "Literacy Worksheet",
          start: "2019-11-01"
        },
        {
          title: "Photosynthesis Worksheet",
          start: "2019-11-05"
        },
        {
          title: "Algebra Test",
          start: "2019-11-09T12:30:00",
          allDay: false
        }
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
  transform: skewX(-15deg);
  transition: left 1s;
}
.slanted:hover {
  left: -38%;
}
</style>
