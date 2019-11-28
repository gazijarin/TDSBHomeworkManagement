<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <div class="col-4" style="float: right; padding-top: 15px;">
      <div class="card" style="border:1px solid black;">
        <div class="card-header">
          <h6 style="float: left; padding-top: 10px">Assignments</h6>
          <b-button v-b-modal.modal-1 size="sm" style="float: right; margin-left: 15px;">
            Add Assignment
            <font-awesome-icon :icon="['fas', 'plus']" />
          </b-button>
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
          <div class="form-group">
            <select class="form-control">
              <option>All</option>
              <option>Course 1</option>
              <option>Course 2</option>
              <option>Course 3</option>
            </select>
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
          <pure-vue-chart
            :points="[{label: 'A1', value: 40}, {label: 'A2', value: 10}, {label: 'A3', value: 100}, {label: 'A4', value: 60}]"
            :show-y-axis="true"
            :show-x-axis="true"
            :show-values="true"
            :width="800"
            :height="400"
          />
        </div>
      </div>
    </div>
    <div class="col-8" style="padding-top: 15px">
      <div class="card" style="border:1px solid black;">
        <div class="card-header">
          <h6 style="float: left; padding-top: 10px">Grades</h6>
          <div class="form-group">
            <select class="form-control">
              <option>All</option>
              <option>Course 1</option>
              <option>Course 2</option>
              <option>Course 3</option>
            </select>
          </div>
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

export default {
  name: "Progress", //this is the name of the component
  components: {
    Datepicker,
    VueSlider,
    PureVueChart,
    navbar: navbar
  },
  data() {
    return {
      value: 50,
      marks: val => val % 20 === 0
    };
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