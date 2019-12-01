<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <div class="col-4" style="float: right; padding-top: 15px;">
      <b-card border-variant="dark" header="Due Soon" align="left">Tasks due soon.</b-card>
    </div>
    <div class="col-8" style="padding-top: 15px">
      <div class="card" style="border:1px solid black;">
        <div class="card-header">
          <h6 style="float: left; padding-top: 10px">Tasks</h6>
          <b-button v-on:click="openAddTask()" size="sm" style="float: right; margin-left: 15px;">
            Add Task
            <font-awesome-icon :icon="['fas', 'plus']" />
          </b-button>
          <b-modal
            id="modal-1"
            size="lg"
            centered
            ref="modal"
            :title="modifyModal ? 'View and Modify Task' : 'Add Task'"
            @ok="handleOk"
            @show="resetModal"
            @hidden="resetModal"
          >
            <div class="form-group">
              <b-form-input v-model="modal.title" placeholder="Title"></b-form-input>
            </div>
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <datepicker placeholder="Due Date" v-model="modal.date"></datepicker>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <input
                    class="form-control"
                    type="time"
                    v-model="modal.time"
                    style="margin-top: 2%"
                  />
                </div>
              </div>
            </div>
            <div class="form-group">
              <select class="form-control" v-model="modal.course">
                <option value="Course 1">Course 1</option>
                <option value="Course 2">Course 2</option>
                <option value="Course 3">Course 3</option>
                <option value="Course 4">Course 4</option>
              </select>
            </div>
            <div class="form-group">
              <div id="app">
                <vue-editor v-model="modal.description" :editorToolbar="customToolbar"></vue-editor>
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
        <b-button size="sm" style="width: 20%; margin-left: 20px; margin-top: 10px">
          <font-awesome-icon :icon="['fas', 'sync']" />Sync with Google
        </b-button>
        <FullCalendar
          defaultView="dayGridMonth"
          allDayText
          :header="{
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
          }"
          selectable="true"
          :events="events"
          :plugins="calendarPlugins"
          @eventClick="eventClick"
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
import navbar from "../navbar/navbar";
import moment from "moment";
import interactionPlugin from "@fullcalendar/interaction";

export default {
  name: "Tasks",
  components: {
    Datepicker,
    VueEditor,
    FullCalendar,
    navbar: navbar
  },
  computed: {
    user() {
      return this.$store.state.user;
    }
  },
  methods: {
    handleOk() {
      var self = this;
      if (this.modifyModal) {
        console.log(this.modal); // eslint-disable-line no-console
        this.$axios
          .patch("http://localhost:5000/api/task?id=" + this.modal.taskid, {
            title: this.modal.title,
            date: moment(this.modal.date).format("DD MMM YYYY"),
            time: this.modal.time,
            course: this.modal.course,
            description: this.modal.description,
            attachments: "[]"
          })
          .then(response => {
            console.log(response); // eslint-disable-line no-console
            this.events = []
            this.loadTasks()
            return response;
          });
      } else {
        console.log(moment(this.modal.date).format("dd MMM yyyy")); // eslint-disable-line no-console
        console.log(this.modal); // eslint-disable-line no-console
        this.$axios
          .post("http://localhost:5000/api/task", {
            title: this.modal.title,
            date: moment(this.modal.date).format("DD MMM YYYY"),
            time: this.modal.time,
            course: this.modal.course,
            description: this.modal.description,
            student: this.$store.state.user._id,
            attachments: "[]"
          })
          .then(response => {
            console.log(response); // eslint-disable-line no-console
            self.$data.events.push({
              id: response.data._id,
              title: response.data.title,
              course: response.data.course,
              description: response.data.description,
              start: response.data.deadline
            });
            return response;
          });
      }
    },
    eventClick: function(event) {
      this.modifyModal = true;
      this.$bvModal.show("modal-1");
      this.modal.taskid = event.event.id;
      this.modal.title = event.event.title;
      this.modal.date = event.event.start;
      this.modal.time = moment(event.event.start, moment.ISO_8601).format(
        "H:mm"
      );
      this.modal.course = event.event._def.extendedProps.course;
      this.modal.description = event.event._def.extendedProps.description;
    },
    resetModal() {
      this.modal.title = "";
      this.modal.date = "";
      this.modal.time = "";
      this.modal.course = "";
      this.modal.description = "";
    },
    openAddTask: function() {
      this.modifyModal = false;
      this.$bvModal.show("modal-1");
    },
    loadTasks: function() {
        var self = this;

    this.$axios
      .get(
        "http://localhost:5000/api/task/student?id=" +
          this.$store.state.user._id
      )
      .then(response => {
        response.data.forEach(function(item) {
          console.log(item); // eslint-disable-line no-console
          self.$data.events.push({
            id: item._id,
            title: item.title,
            start: item.deadline,
            course: item.course,
            description: item.description,
            attachments: item.attachments
          });
        });
      });
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
      calendarPlugins: [
        dayGridPlugin,
        timeGridPlugin,
        listPlugin,
        interactionPlugin
      ],
      config: {
        defaultView: "month",
        selectable: true
      },
      modifyModal: false,
      modal: {
        taskid: "",
        title: "",
        date: "",
        time: "",
        course: "",
        description: "",
        attachments: "[]"
      }
    };
  },
  beforeMount() {
    this.loadTasks()

    // this.$gapi.request({
    //   path: 'https://www.googleapis.com/calendar/v3/calendars/' + this.$store.state.user.email + '/events',
    //   method: 'GET'
    // }).then(response => {
    //   console.log(response) // eslint-disable-line no-console
    //   response.result.items.forEach(function (item) {
    //   self.$data.events.push({
    // 								id: item.id,
    // 								title: item.summary,
    // 								start: item.start.dateTime || item.start.date,
    // 		});
    //   });
    // })
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
