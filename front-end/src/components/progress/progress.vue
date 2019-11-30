<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <div class="col-4" style="float: right; padding-top: 15px;">
      <div class="card" style="border:1px solid black; margin-bottom:20px">
        <div class="card-header">
          <h6 style="float: left; padding-top: 10px">Courses</h6>
          <div class="form-group">
            <select class="form-control" v-model="selectedCourse">
              <option value="" selected disabled hidden>Pick a Course</option>
              <option v-for="course in courseList" :key="course">{{course}}</option>
            </select>
          </div>
          <div v-if="selectedCourse">
            <b-modal
              id="modal-1"
              size="lg"
              centered
              ref="modal"
              title="Add Assignment"
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
              <!-- <div class="form-group">
                <input type="number" class="form-control" id="GradeInput" placeholder="Grade" />
              </div>-->
              <label for="completedAssignment">Amount Completed</label>
              <div class="form-group">
                <vue-slider v-model="value" :marks="marks">
                  <template v-slot:step="{ label, active }">
                    <div :class="['custom-step', { active }]"></div>
                  </template>
                </vue-slider>
              </div>
              <label for="attachments">Attachment(s)</label>
              <div class="form-group">
                <input type="file" class="form-control-file" id="exampleFormControlFile1" />
              </div>
            </b-modal>
            <hr>
            <b-tabs content-class="mt-3" fill pills>
              <b-tab title="Assignments" active>
                <b-card>
                  <template v-slot:header>
                    <h5 class="mb-0" style="float: left; margin-left: 15px; margin-top: 5px">Names</h5>
                    <b-button v-b-modal.modal-1 size="sm" style="float: right; margin-left: 15px;">
                      Add Assignment
                      <font-awesome-icon :icon="['fas', 'plus']" />
                    </b-button>
                  </template>
                  <b-list-group flush>
                    <b-list-group-item v-for="assignment in assignmentList" :key="assignment">
                      <p style="float: left">{{assignment.name}}</p>
                      <b-button v-b-modal.modal-1 size="sm" variant="danger" style="float: right; margin-top: -5px; margin-left: 10px;">
                        Delete
                        <font-awesome-icon :icon="['fas', 'trash']" />
                      </b-button>
                      <b-button v-b-modal.modal-1 variant="info" size="sm" style="float: right; margin-top: -5px;">
                        Edit
                        <font-awesome-icon :icon="['fas', 'edit']" />
                      </b-button>
                    </b-list-group-item>
                  </b-list-group>
                </b-card>
              </b-tab>
              <b-tab title="Grades">
                <b-card>
                  <template v-slot:header>
                    <h5 class="mb-0" style="float: left; margin-left: 15px; margin-top: 5px">Names</h5>
                    <b-button v-b-modal.modal-1 size="sm" style="float: right; margin-left: 15px;">
                      Add Assignment
                      <font-awesome-icon :icon="['fas', 'plus']" />
                    </b-button>
                  </template>
                  <b-list-group flush>
                    <b-list-group-item v-for="assignment in assignmentList" :key="assignment">
                      <p style="float: left">{{assignment.name}}</p>
                      <b-form-input :state="nameState(assignment.grade)" id="input-grade" size="sm" v-model="assignment.grade" style="float: right; width: 30%" placeholder="Grade"></b-form-input>
                    </b-list-group-item>
                  </b-list-group>
                </b-card>
              </b-tab>
            </b-tabs>
          </div>
        </div>
      </div>
    </div>

    <div class="col-8" style="padding-top: 15px">
      <div class="card" style="border:1px solid black;">
        <div class="card-header">
          <h6 style="float: left; padding-top: 10px">Progress</h6>
        </div>
        <div>
          <TrendChart
            :datasets="[
              {
                data: chartData,
                smooth: true,
                fill: false
              },
              {
                data: [10, 30, 75, 90, 100, 15, 65, 0, 80, 60, 90, 55, 95, 35, 50],
                smooth: true,
                fill: false
              }
            ]"
            :grid="{
              verticalLines: true,
              horizontalLines: true
            }"
            :labels="{
              xLabels: xAxisList,
              yLabels: 5
            }"
            :min="0"
            :max="100"
            :interactive="true">
          </TrendChart>
        </div>
      </div>
    </div>

    <div class="col-8" style="padding-top: 15px">
      <div class="card" style="border:1px solid black; padding-bottom:10px">
        <div class="card-header" style="margin-bottom:20px">
          <h6 style="float: left; padding-top: 10px">Completion Per Assignment</h6>
        </div>
        <div>
          <pure-vue-chart
            :points="barGraphData"
            :show-y-axis="true"
            :show-x-axis="true"
            :show-values="true"
            :width="800"
            :height="400"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "../navbar/navbar";
import Datepicker from "vuejs-datepicker";
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/antd.css";
import PureVueChart from "pure-vue-chart";
import TrendChart from "vue-trend-chart";

export default {
  name: "Progress", //this is the name of the component
  components: {
    Datepicker,
    VueSlider,
    PureVueChart,
    TrendChart,
    navbar: navbar
  },
  data() {
    return {
      value: 50,
      selectedCourse: "",
      assignmentList: [{name: "A1", grade: 88}, {name: "A2", grade: 79}, {name: "A3", grade: 98}],
      chartData: [100, 20, 55, 90, 50, 10, 35, 55, 60, 80, 100, 85, 25, 95, 70],
      xAxisList: ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15"],
      barGraphData: [{label: 'A1', value: 40}, {label: 'A2', value: 10}, {label: 'A3', value: 100}, {label: 'A4', value: 60}],
      courseList: [],
      marks: val => val % 20 === 0
    };
  },
  methods: {
    getCourseInformation: function(course) {
      // Get the course's assignments from the backend.
      // Set all the course information.
      this.allAssignments = true
      this.allGrades = true
      this.xAxisList = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15"]
      this.chartData = [100, 20, 55, 90, 50, 10, 35, 55, 60, 80, 100, 85, 25, 95, 70]
      return course
    },
    getXAxisLabels: function(xList) {
      // For each data, add its timestamp as the x Axis label.
      return xList
    },
    getCompletionPercentage: function(assignmentList) {
      // Convert the assignments to their completion percentage.
      return assignmentList
    },
    nameState: function(grade) {
      return grade >= 0 && grade <= 100 ? true : false
    },
    getCourses: function() {
      this.courseList = ["All", "Course 1", "Course 2", "Course 3", "Course 4"]
    }
  },
  computed: {
    allAssignments: function() {
      return this.selectedCourse === "All"
    },
    allGrades: function() {
      return this.selectedCourse === "All"
    }
  },
  created: function() {
    this.getCourses()
  }
};
</script>
<style>
.custom-step {
  width: 100%;
  height: 90%;
  border-radius: 50%;
  box-shadow: 0 0 0 3px #ccc;
  background-color: #fff;
}
.custom-step.active {
  box-shadow: 0 0 0 3px #3498db;
  background-color: #3498db;
}
</style>