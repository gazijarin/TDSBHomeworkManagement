<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <div class="col-4" style="float: right; padding-top: 15px;">
      <b-card border-variant="dark">
        Calendar here.
      </b-card>
      <br/>
      <b-card border-variant="dark">
        Task list here.
      </b-card>
    </div>
    <div class="col-8" style="padding-top: 15px">
      <b-card class="today-container"
        border-variant="dark"
        header="Today"
        align="left">
          <b-card-body style="margin-top: -25px; margin-bottom: -15px;">
            No tasks today.
          </b-card-body>
      </b-card>
    </div>
    <div class="col-8" style="padding-top: 2%">
      <b-card border-variant="dark" header="Feed" align="left" style="height: 2000px;">

      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home' //this is the name of the component
}
</script>

<style>
</style>