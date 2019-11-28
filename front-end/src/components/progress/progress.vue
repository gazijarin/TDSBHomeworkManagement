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
        </div>
      </div>
    </div>
    <div class="col-8" style="padding-top: 15px">
      <div class="card" style="border:1px solid black;">
        <div class="card-header">
          <h6 style="float: left; padding-top: 10px">Progress</h6>
        </div>
      </div>
    </div>
    <div class="col-8" style="padding-top: 15px">
      <div class="card" style="border:1px solid black;">
        <div class="card-header">
          <h6 style="float: left; padding-top: 10px">Grades</h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "../navbar/navbar";

export default {
  name: "Progress", //this is the name of the component
  components: {
    navbar: navbar
  }
};
</script>
<style>
</style>