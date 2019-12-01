<template>
  <div class="row" id="Dictionary">
    <form class="form-inline">
      <div class="form-group mx-sm-3 mb-2">
        <b-form-input v-model="wordText" placeholder="Enter a word."></b-form-input>
      </div>
      <button type="submit" class="btn btn-primary mb-2">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Dictionary",
  data() {
    return {
      wordText: ""
    };
  },
  methods: {
    formSubmit(e) {
      alert(this.wordText);
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