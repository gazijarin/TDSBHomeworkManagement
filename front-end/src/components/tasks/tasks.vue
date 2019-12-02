<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <div class="col-4" style="float: right; padding-top: 15px;">
      <b-card border-variant="dark" header="Due Soon" align="left">
        <FullCalendar
          defaultView="list"
          :events="events"
          :header="{
            center: '',
            right:  ''
          }"
          :plugins="calendarPlugins"
          :visibleRange="visibleRangeSoon"
        />
      </b-card>
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
                <option :key="idx" v-for="(item, idx) in courses" :value="item.id">{{item.name}}</option>
              </select>
            </div>
            <div class="form-group">
              <div id="app">
                <vue-editor v-model="modal.description" :editorToolbar="customToolbar"></vue-editor>
              </div>
            </div>
            <form>
              <div class="form-group">
                <label for="exampleFormControlFile1">Attachment</label>
                <input type="file" ref="file" v-on:change="handleFileUpload()" class="form-control-file" id="exampleFormControlFile1"/>

                <div id="attachmentsection">
                <a v-if="checkAttachment" :download="dataUrl.filename" :href="dataUrl.filedata" id="attachmentlink">{{dataUrl.filename}}</a>
                </div>
              </div>
            </form>
            <template #modal-footer="{ ok, cancel }">
              <div style="display:block; width: 100%">
                <b-button
                  v-if="modifyModal"
                  v-on:click="deleteTask()"
                  style="float:left"
                  variant="danger"
                >Delete Task</b-button>
                <b-button style="float:right" variant="primary" @click="ok">Submit Changes</b-button>
              </div>
            </template>
          </b-modal>
        </div>
        <div>
          <b-button
            size="sm"
            variant="outline-primary"
            style="width: 20%; margin-left: 20px; margin-top: 10px; float:left;"
            v-on:click="syncNow()"
          >
            <font-awesome-icon :icon="['fas', 'sync']" />Sync with Google
          </b-button>
          <span style="float:left; margin-top: 16px; margin-left: 5px; font-size: 14px">
            <b>Last Sync Date:</b>
            {{ last_sync_date }}
          </span>
        </div>
        <FullCalendar
          defaultView="dayGridMonth"
          allDayText
          :header="{
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,listWeek'
          }"
          selectable="true"
          :events="events"
          :plugins="calendarPlugins"
          @eventClick="eventClick"
          ref="calendar"
          style="margin: 20px"
        />
        <ul style="margin-top: 1%; padding-right: 2%">
          <b-button
            v-on:click="showAllEvents()"
            size="sm"
            variant="danger"
            style="float: right; margin-left: 2px;"
          >
            <font-awesome-icon :icon="['fas', 'times']" />
          </b-button>
          <b-button
            v-on:click="handleEventRender()"
            size="sm"
            style="float: right; margin-left: 2px;"
            variant="outline-primary"
          >
            Search
            <font-awesome-icon :icon="['fas', 'search']" />
          </b-button>
          <input
            class="form-control sm-1"
            type="text"
            id="searchevents"
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
import $ from "jquery";

export default {
  name: "Tasks",
  beforeCreate() {
    if (!this.$store.state.user) {
      console.log("return home"); // eslint-disable-line no-console
      this.$router.push("/");
    }
  },
  components: {
    Datepicker,
    VueEditor,
    FullCalendar,
    navbar: navbar
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    checkAttachment() {
      return this.modifyModal && this.modal.attachments
    }
  },
  methods: {
    handleFileUpload() {
      this.modal.attachments = this.$refs.file.files[0];
    },
    retrieveFile(id) {
      this.$axios
        .get(
          this.$store.state.prefix +
            "/api/file/retrieve?id=" + id
        )
        .then(response => {
          console.log(response); // eslint-disable-line no-console
          this.modal.attachments = id
          response.data.filedata = "data:image/jpeg;base64," + response.data.filedata
          this.dataUrl = response.data
        });
    },
    showAllEvents: function() {
      $.each(this.events, function() {
        if (this.startsave) {
          this.start = this.startsave;
        }
      });
    },

    handleEventRender: function() {
      var filterquery = $("#searchevents").val();
      $.each(this.events, function() {
        if (!this.title.includes(filterquery)) {
          this.startsave = this.start;
          this.start = null;
        }
      });
    },
    handleUpdate(fileid="") {
        var self = this;
        if (this.modifyModal) {
        this.$axios
          .patch(this.$store.state.prefix + "/api/task/" + this.modal.taskid, {
            title: this.modal.title,
            date: moment(this.modal.date).format("DD MMM YYYY"),
            time: this.modal.time,
            course_id: this.modal.course,
            description: this.modal.description,
            attachments: fileid
          })
          .then(response => {
            console.log(response); // eslint-disable-line no-console
            this.events = [];
            this.loadTasks();
            return response;
          });
      } else {
        console.log(this.modal); // eslint-disable-line no-console
        this.$axios
          .post(this.$store.state.prefix + "/api/task", {
            title: this.modal.title,
            date: moment(this.modal.date).format("DD MMM YYYY"),
            time: this.modal.time,
            course: this.modal.course,
            description: this.modal.description,
            student: this.$store.state.user._id,
            attachments: fileid
          })
          .then(response => {
            console.log(response); // eslint-disable-line no-console
            self.$data.events.push({
              id: response.data._id,
              title: response.data.title,
              course: response.data.course_id,
              description: response.data.description,
              start: response.data.deadline,
              attachments: response.data.attachments
            });
            return response;
          });
      }
    },
    handleOk() {
        if (this.modal.attachments) {
          let formData = new FormData();
          formData.append("file", this.modal.attachments);

          this.$axios
          .post(this.$store.state.prefix + "/api/file/upload", formData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(response => {
            console.log(response); // eslint-disable-line no-console
            this.handleUpdate(response.data[0]._id)
          });
        } else {
          this.handleUpdate()
        }
    },
    syncNow() {
      var self = this;
      this.$store.state.user.courses.forEach(function(course) {
        self.$gapi
          .request({
            path:
              "https://www.googleapis.com/calendar/v3/calendars/" +
              course.calendarId +
              "/events",
            method: "GET"
          })
          .then(response => {
            response.result.items.forEach(function(item) {
              var dateofevent = item.created;
              console.log(new Date(dateofevent).getTime()); // eslint-disable-line no-console
              console.log(new Date(self.last_sync_date).getTime()); // eslint-disable-line no-console
              if (
                new Date(dateofevent).getTime() >=
                new Date(self.last_sync_date).getTime()
              ) {
                self.$axios
                  .post(self.$store.state.prefix + "/api/task", {
                    title: item.summary,
                    date: moment(item.start.dateTime || item.start.date).format(
                      "DD MMM YYYY"
                    ),
                    time: moment(item.start.dateTime || item.start.date).format(
                      "HH:mm"
                    ),
                    course: course.id,
                    description: item.description,
                    student: self.$store.state.user._id,
                    attachments: ""
                  })
                  .then(response => {
                    self.$data.events.push({
                      id: response.data._id,
                      title: response.data.title,
                      course: response.data.course_id,
                      description: response.data.description,
                      start: response.data.deadline,
                      attachments: ""
                    });
                    return response;
                  });
              }
            });
            self.$axios
              .patch(
                self.$store.state.prefix +
                  "/api/student/" +
                  self.$store.state.user._id +
                  "?sync=true",
                {}
              )
              .then(response => {
                self.last_sync_date = moment(String(new Date())).format(
                  "MM/DD/YYYY HH:mm:ss"
                );
                return response;
              });
          });
      });
    },

    getLastSyncDate() {
      var self = this;
      this.$axios
        .get(
          this.$store.state.prefix +
            "/api/student/" +
            this.$store.state.user._id
        )
        .then(response => {
          if (response.data.last_sync_date === response.data.created_date) {
            this.$store.state.user.courses.forEach(function(course) {
              self.$gapi
                .request({
                  path:
                    "https://www.googleapis.com/calendar/v3/calendars/" +
                    course.calendarId +
                    "/events",
                  method: "GET"
                })
                .then(response => {
                  response.result.items.forEach(function(item) {
                    self.$axios
                      .post(this.$store.state.prefix + "/api/task", {
                        title: item.summary,
                        date: moment(
                          item.start.dateTime || item.start.date
                        ).format("DD MMM YYYY"),
                        time: moment(
                          item.start.dateTime || item.start.date
                        ).format("HH:mm"),
                        course: course.id,
                        description: item.description,
                        student: self.$store.state.user._id,
                        attachments: ""
                      })
                      .then(response => {
                        self.$data.events.push({
                          id: response.data._id,
                          title: response.data.title,
                          course: response.data.course,
                          description: response.data.description,
                          start: response.data.deadline,
                          attachments: ""
                        });
                        return response;
                      });
                  });
                });
            });

            this.$axios
              .patch(
                this.$store.state.prefix +
                  "/api/student/" +
                  this.$store.state.user._id +
                  "?sync=true",
                {}
              )
              .then(response => {
                return response;
              });
          } else {
            var adjust_time_zone = new Date(response.data.last_sync_date);
            adjust_time_zone.setHours(adjust_time_zone.getHours() - 5);
            this.last_sync_date = moment(String(adjust_time_zone)).format(
              "MM/DD/YYYY HH:mm:ss"
            );
          }
        });
    },
    deleteTask() {
      this.$axios
        .delete(this.$store.state.prefix + "/api/task/" + this.modal.taskid)
        .then(response => {
          this.events = [];
          this.loadTasks();
          this.$bvModal.hide("modal-1");
          return response;
        });
    },
    eventClick: function(event) {
      this.modifyModal = true;
      this.modal.attachments = event.event._def.extendedProps.attachments;
      if (!this.modal.attachments == "") {
        this.retrieveFile(this.modal.attachments)
      }
      this.$bvModal.show("modal-1");
      this.modal.taskid = event.event.id;
      this.modal.title = event.event.title;
      this.modal.date = event.event.start;
      this.modal.time = moment(event.event.start).format("HH:mm");
      this.modal.course = event.event._def.extendedProps.course;
      this.modal.description = event.event._def.extendedProps.description;
    },
    resetModal() {
      this.modal.title = "";
      this.modal.date = "";
      this.modal.time = "";
      this.modal.course = "";
      this.modal.description = "";
      this.modal.attachments = "";
    },
    openAddTask: function() {
      this.modifyModal = false;
      this.$bvModal.show("modal-1");
    },
    loadTasks: function() {
      var self = this;

      this.$axios
        .get(
          this.$store.state.prefix +
            "/api/task/student?id=" +
            this.$store.state.user._id
        )
        .then(response => {
          response.data.forEach(function(item) {
            self.$data.events.push({
              id: item._id,
              title: item.title,
              start: item.deadline,
              course: item.course_id,
              description: item.description,
              attachments: item.attachments
            });
          });
          this.handleEventRender();
        });
    },
    visibleRangeFunction: function() {
      // Generate a new date for manipulating in the next step
      var startDate = new Date();
      var endDate = new Date();

      // Adjust the start & end dates, respectively
      endDate.setDate(startDate.getDate() + 5); // Two days into the future

      this.visibleRangeSoon.start = startDate;
      this.visibleRangeSoon.end = endDate;
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
      courses: this.$store.state.user.courses,
      visibleRangeSoon: {},
      last_sync_date: null,
      modifyModal: false,
      modal: {
        taskid: "",
        title: "",
        date: "",
        time: "",
        course: "",
        description: "",
        attachments: ""
      },
      dataUrl: null,
    };
  },
  beforeMount() {
    this.visibleRangeFunction();
    this.loadTasks();
    this.getLastSyncDate();

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

.fc-event {
  cursor: pointer;
}

.fc td,
.fc th {
  border-style: none !important;
}

.fc-head .fc-widget-header {
  border-bottom: 1px solid #ddd !important;
}

.display-none {
  display: none !important;
}
</style>
