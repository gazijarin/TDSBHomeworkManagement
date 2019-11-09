<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <div class="col-4" style="float: right; padding-top: 15px;">
      <b-card border-variant="dark" header="Classes" align="left">Classes here.</b-card>
      <br />
      <b-card border-variant="dark" header="Due Soon" align="left">Tasks due soon.</b-card>
    </div>
    <div class="col-8" style="padding-top: 15px">
      <div class="card" style="border:1px solid black;">
        <div class="card-header">
          <h6 style="float: left; padding-top: 10px">Tasks</h6>
          <b-button v-b-modal.modal-1 size="sm" style="float: right; margin-left: 15px;">
            Add Task
            <font-awesome-icon :icon="['fas', 'plus']" />
          </b-button>
          <b-modal
            id="modal-1"
            size="lg"
            centered
            ref="modal"
            title="Add Task"
            @show="resetModal"
            @hidden="resetModal"
            @ok="handleOk"
          >
            <div class="form-group">
              <b-form-input v-model="text" placeholder="Title"></b-form-input>
            </div>
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <datepicker placeholder="Due Date"></datepicker>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <input class="form-control" type="time" value="12:00:00" style="margin-top: 2%" />
                </div>
              </div>
            </div>
            <div class="form-group">
              <select class="form-control">
                <option>Course</option>
              </select>
            </div>
            <div class="form-group">
              <div id="app">
                <vue-editor v-model="content" :editorToolbar="customToolbar"></vue-editor>
              </div>
            </div>
            <form>
              <div class="form-group">
                <label for="exampleFormControlFile1">Attachment(s)</label>
                <input type="file" class="form-control-file" id="exampleFormControlFile1" />
              </div>
            </form>
          </b-modal>
        </div>
        <FullCalendar
          defaultView="dayGridMonth"
          allDayText
          :header="{
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
          }"
          :events="events"
          :plugins="calendarPlugins"
          style="margin: 20px"
        />
        <ul style="margin-top: 1%; padding-right: 2%">
          <b-button size="sm" style="float: right; margin-left: 2px;">
            Search
            <font-awesome-icon :icon="['fas', 'search']" />
          </b-button>
          <input
            class="form-control sm-1"
            type="text"
            placeholder="Search"
            aria-label="Search"
            style="width: 50%; float: right; height: 10%; margin-top: -2px"
          />
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import Datepicker from "vuejs-datepicker";
import { VueEditor } from "vue2-editor";
import FullCalendar from "@fullcalendar/vue";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import listPlugin from "@fullcalendar/list";

export default {
  name: "Tasks",
  components: {
    Datepicker,
    VueEditor,
    FullCalendar
  },
  computed: {
    user() {
      return this.$store.state.user;
    }
  },
  data() {
    return {
      content: "<h4>Description</h4>",
      customToolbar: [
        ["bold", "italic", "underline"],
        [{ list: "ordered" }, { list: "bullet" }],
        ["image", "code-block"]
      ],
      events: [],
      calendarPlugins: [dayGridPlugin, timeGridPlugin, listPlugin],
      config: {
        defaultView: "month"
      }
    };
  },
    beforeMount() {
    var self = this;
    this.$gapi.request({
      path: 'https://www.googleapis.com/calendar/v3/calendars/' + this.$store.state.user.email + '/events',
      method: 'GET'
    }).then(response => {
      console.log(response) // eslint-disable-line no-console
      response.result.items.forEach(function (item) {
      self.$data.events.push({
										id: item.id,
										title: item.summary,
										start: item.start.dateTime || item.start.date,
				});
      });
    })
  }
};
</script>

<style>
body {
  font-family: "Helvetica Neue Light", Helvetica, sans-serif;
  padding: 1em 2em 2em;
}
input,
select {
  padding: 0.75em 0.5em;
  font-size: 100%;
  border: 1px solid #ccc;
  width: 100%;
}

select {
  height: 2.5em;
}

.example {
  background: #f2f2f2;
  border: 1px solid #ddd;
  padding: 0em 1em 1em;
  margin-bottom: 2em;
}

code,
pre {
  margin: 1em 0;
  padding: 1em;
  border: 1px solid #bbb;
  display: block;
  background: #ddd;
  border-radius: 3px;
}

.settings {
  margin: 2em 0;
  border-top: 1px solid #bbb;
  background: #eee;
}

h5 {
  font-size: 100%;
  padding: 0;
}

.form-group {
  margin-bottom: 1em;
}

.form-group label {
  font-size: 60%;
  display: block;
}
</style>
<style lang='scss'>
@import "~@fullcalendar/core/main.css";
@import "~@fullcalendar/daygrid/main.css";
@import "~@fullcalendar/list/main.css";

.fc-event-time,
.fc-event-title {
  padding: 0 1px;
  white-space: nowrap;
}

.fc-title {
  white-space: normal;
  color: white;
}
</style>