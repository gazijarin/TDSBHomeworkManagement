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
      <b-card class="today-container"
        border-variant="dark"
        header="Tasks"
        align="left">
          <b-card-body style="margin-top: -25px; margin-bottom: -15px;">
            Task list here. Make searchable.
          </b-card-body>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tasks' //this is the name of the component
}
</script>

<style>
</style>