<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    Welcome <span v-if="user !== null">{{ user.first_name }}</span>
    <div class="col-4" style="float: right; padding-top: 15px;">
      <b-card border-variant="dark">
        <FullCalendar :header="calendarHeader"
        :plugins="calendarPlugins"
        defaultView="dayGridMonth"
        :events="events"></FullCalendar>
      </b-card>
      <br/>
      <!-- <b-card border-variant="dark" header="Progress" align="left">
        <FullCalendar :header="false"
        :plugins="taskPlugins"
        defaultView="listWeek"
        :events="events"></FullCalendar>
      </b-card> -->
    </div>
    <div class="col-8" style="padding-top: 15px">
      <b-card class="today-container"
        border-variant="dark"
        header="Today"
        align="left">
          <b-card-body style="margin-top: -25px; margin-bottom: -15px;">
            <FullCalendar :header="false"
              :height="20"
              :plugins="todayPlugins"
              defaultView="dayGridDay"
              :events="events"></FullCalendar>
          </b-card-body>
      </b-card>
    </div>
    <div class="col-8" style="padding-top: 2%">
      <b-card border-variant="dark" header="Feed" align="left">

      </b-card>
    </div>
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import listPlugin from '@fullcalendar/list'
import navbar from '../navbar/navbar'

export default {
  name: 'Home', //this is the name of the component
  components: {
    'navbar': navbar,
    FullCalendar // make the <FullCalendar> tag available
  },
  data() {
    return {
      events: [
        {
            title  : 'Literacy Worksheet',
            start  : '2019-11-01',
        },
        {
            title  : 'Photosynthesis Worksheet',
            start  : '2019-11-05',
        },
        {
            title  : 'Algebra Test',
            start  : '2019-11-09T12:30:00',
            allDay : false,
        },
      ],
      calendarHeader: {
        left:   'prev',
        center: 'title',
        right:  'next'
      },
			taskListConfig: {
        defaultView: 'weekList'
      },
      todayPlugins: [ dayGridPlugin ],
      calendarPlugins: [ dayGridPlugin, timeGridPlugin, listPlugin ],
      taskPlugins: [ listPlugin ]
    }
  },
  computed: {
    user () {
      return this.$store.state.user
    }
  }
}

</script>

<style lang='scss'>
@import '~@fullcalendar/core/main.css';
@import '~@fullcalendar/list/main.css';
</style>
