<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <div class="col-6" style="margin: 0 auto; float: none; margin-top: 20px; padding-top: 15px">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h5 class="mb-0">Dictionary</h5>
        </template>
        <b-form-input v-model="text" placeholder="Enter a word."></b-form-input>
      </b-card>
    </div>
  </div>
</template>

<script>
import navbar from "../navbar/navbar";

export default {
  name: "Tools", //this is the name of the component
  components: {
    navbar: navbar
  }
};
</script>
<style>
</style>