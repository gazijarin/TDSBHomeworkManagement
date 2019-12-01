<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <div class="col-6" style="margin: 0 auto; float: left; margin-top: 20px; padding-top: 15px">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h5 class="mb-0">Dictionary</h5>
        </template>
        <Dictionary v-on:formSubmit="searchWord"></Dictionary>
        <dictionaryOutput v-text="meaning"></dictionaryOutput>
      </b-card>
      </div>
      <div class="col-6" style="margin: 0 auto; float: right; margin-top: 20px; padding-top: 15px">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h5 class="mb-0">Thesaurus</h5>
        </template>
        <Thesaurus></Thesaurus>
      </b-card>
    </div>
  </div>
</template>

<script>
import navbar from "../navbar/navbar";
import Dictionary from "../tools/dictionary";
import dictionaryOutput from "../tools/dictionaryOutput";
import Thesaurus from "../tools/thesaurus";

export default {
  name: "Tools",
  components: {
    navbar,
    Dictionary,
    dictionaryOutput,
    Thesaurus
  },
  data: function() {
    return {
      meaning: ""
    };
  },
  methods: {
    searchWord: function(text) {
      this.$axios
        .get(this.$store.state.prefix + "/api/dictionary/" + text)
        .then(response => {
          this.meaning = response;
        });
    }
  }
};
</script>
<style>
</style>