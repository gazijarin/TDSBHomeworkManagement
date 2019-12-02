<template>
  <div>
    <h2 class="text-success">{{meaning.word}}</h2>
    <h3 class="text-success">{{meaning.phonetic}}</h3>
    <h4 class="text-success">{{meaning.origin}}</h4>
    <div v-for="key in meaning.meaning" :key="key">
      <h3>{{key}}</h3>
      <div v-for="def in meaining.meaining[key]" :key="def">
        <h4>{{"Definition: " + def.definition}}</h4>
        <h4>{{"Example: " + def.example}}</h4>
        <h4>{{"Synonyms: "}}</h4>
        <div v-for="synonym in def.synonyms" :key="synonym"
        >{{synonym}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "dictionaryOutput",
  props: ['meaining']
};
</script>

<style>
</style>