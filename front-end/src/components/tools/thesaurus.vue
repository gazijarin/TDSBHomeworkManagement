<template>
  <div class="row" id="Thesaurus">
    <div class="input-group">
      <b-form-input style="margin-left: 10px" v-model="wordText" placeholder="Enter a word for its synonyms."></b-form-input>
      <span class="input-group-btn">
        <button
          type="submit"
          style="margin-left: 10px; margin-right: 10px"
          class="btn btn-primary"
        v-on:click="formSubmit">Go</button>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Thesaurus",
  data() {
    return {
      wordText: ""
    };
  },
  methods: {
    formSubmit(e) {
      this.$emit("formSubmit", this.wordText);
      e.preventDefault();
    }
  }
};
</script>

<style>
/* #transForm {
  border-radius: 10px;
  border: 1px #ccc solid;
} */
</style>