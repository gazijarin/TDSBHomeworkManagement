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
export default {
  name: 'Tasks'
}
</script>

<style>
</style>