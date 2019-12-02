<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <navbar></navbar>
    <div class="col-6" style="margin: 0 auto; float: left; margin-top: 20px; padding-top: 15px">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h5 class="mb-0">Dictionary</h5>
        </template>
        <Dictionary v-on:formSubmit="searchWord"></Dictionary>
        <!-- <dictionaryOutput v-if="dictionaryQuery" v-bind:meaning="meaning[0]"></dictionaryOutput> -->
        <div v-if="dictionaryQuery && typeof meaning === 'object'">
          <h3 style="margin-top: 10px">{{meaning.word}}</h3>
          <h5>{{meaning.phonetic}}</h5>
          <h7>{{meaning.origin}}</h7>
          <h5 style="margin-top: 20px">Definition</h5>
          <h6>{{ meaning.meaning.noun[0].definition}}</h6>
          <h5>Usage</h5>
          <h6>{{meaning.meaning.noun[0].example}}</h6>
        </div>
        <div style="padding-top: 20px;" v-else-if="dictionaryQuery">No Results Found</div>
      </b-card>
    </div>
    <div class="col-6" style="margin: 0 auto; float: right; margin-top: 20px; padding-top: 15px">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h5 class="mb-0">Thesaurus</h5>
        </template>
        <Dictionary v-on:formSubmit="findSynonym"></Dictionary>
        <!-- <dictionaryOutput v-if="dictionaryQuery" v-bind:meaning="meaning[0]"></dictionaryOutput> -->
        <div v-if="thesaurusQuery && typeof synonymOut === 'object'">
          <h3 style="margin-top: 10px">{{synonymOut.word}}</h3>
          <h5>{{synonymOut.phonetic}}</h5>
          <h5>{{"Synonyms"}}</h5>
          <div v-for="synonym in synonymOut.meaning.noun[0].synonyms" :key="synonym">{{synonym}}</div>
        </div>
        <div style="padding-top: 20px;" v-else-if="thesaurusQuery">No Results Found</div>
      </b-card>
      <!-- <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h5 class="mb-0">Thesaurus</h5>
        </template>
        <Thesaurus v-on:formSubmit="searchWord"></Thesaurus>
        <div v-if="thesaurusQuery && typeof meaning === 'object'">
          <h3 style="margin-top: 10px">{{meaning.word}}</h3>
          <h5>{{meaning.phonetic}}</h5>
          <h5>{{"Synonyms"}}</h5>
          <div v-for="synonym in meaning.meaning.noun[0].synonyms" :key="synonym">{{synonym}}</div>
        </div>
        <div style="padding-top: 20px;" v-else-if="thesaurusQuery">No Results Found</div>
      </b-card>-->
    </div>
  </div>
</template>

<script>
import navbar from "../navbar/navbar";
import Dictionary from "../tools/dictionary";
// import Thesaurus from "../tools/thesaurus";

export default {
  name: "Tools",
  components: {
    navbar,
    Dictionary
  },
  data: function() {
    return {
      meaning: "",
      synonymOut: "",
      dictionaryQuery: false,
      thesaurusQuery: false
    };
  },
  computed: {},
  methods: {
    searchWord: function(text) {
      this.$axios
        .get(this.$store.state.prefix + "/api/dictionary?word=" + text.trim())
        .then(response => {
          console.log(response.data[0]); // eslint-disable-line no-console
          this.meaning = response.data[0];
          this.dictionaryQuery = true;
        });
    },
    findSynonym: function(text) {
      this.$axios
        .get(this.$store.state.prefix + "/api/dictionary?word=" + text.trim())
        .then(response => {
          console.log("synonym"); // eslint-disable-line no-console
          console.log(response.data[0]); // eslint-disable-line no-console
          this.synonymOut = response.data[0];
          this.thesaurusQuery = true;
        });
    }
  }
};
</script>
<style>
</style>