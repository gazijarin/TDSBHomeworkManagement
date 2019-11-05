<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <div class="col-4" style="float: right; padding-top: 15px;">
      <b-card border-variant="dark" header="Classes" align="left">
        Classes here.
      </b-card>
      <br/>
      <b-card border-variant="dark" header="Due Soon" align="left">
        Tasks due soon.
      </b-card>
    </div>
    <div class="col-8" style="padding-top: 15px">
      <div class="card" style="border:1px solid black;">
        <div class="card-header">
            <h6 style="float: left; padding-top: 10px">Tasks</h6>
            <b-button v-b-modal.modal-1 size="sm"
            style="float: right; margin-left: 15px;">Add Task <font-awesome-icon :icon="['fas', 'plus']" /></b-button>
            <b-modal id="modal-1" title="Add a New Task">
            <p class="my-4">... stuff here</p>
            </b-modal>
        </div>
        <FullCalendar defaultView="dayGridMonth"
          allDayText=""
          :header="{
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
          }"
          :events="events"
         :plugins="calendarPlugins" style="margin: 20px" />
        <ul style="margin-top: 1%; padding-right: 2%">
            <b-button size="sm"
                style="float: right; margin-left: 2px;">Search <font-awesome-icon :icon="['fas', 'search']" /></b-button>
                <input class="form-control sm-1" type="text"
                placeholder="Search"
                aria-label="Search"
                style="width: 50%; float: right; height: 10%; margin-top: -2px">
        </ul>
            
      </div>
    </div>
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import listPlugin from '@fullcalendar/list';

export default {
  name: 'Tasks',
  components: {
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
    calendarPlugins: [ dayGridPlugin, timeGridPlugin, listPlugin ]
  }
  
}
}

</script>

<style lang='scss'>

@import '~@fullcalendar/core/main.css';
@import '~@fullcalendar/daygrid/main.css';
@import '~@fullcalendar/list/main.css';

.fc-event-time, .fc-event-title {
padding: 0 1px;
white-space: nowrap;
}

.fc-title {
white-space: normal;
color: white;
}

</style>