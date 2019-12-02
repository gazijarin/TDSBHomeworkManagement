<template>
  <div>
    <navbar></navbar>
    <div id="wrapper">

      <img id="profile_pic" :src=this.$store.state.user.image>

      <div id="main_name">{{first_name}} {{last_name}}</div>

      <div id="settings">
        <div>
          First Name: <input class="settings_input" v-model="first_name">
        </div>
        <div>
          Last Name: <input class="settings_input" v-model="last_name">
        </div>
        <div>
          Language: <input class="settings_input" v-model="language">
        </div>
        <div>
          Time Zone: <input class="settings_input" v-model="time_zone">
        </div>
      </div>

      <button id="save" @click="alert('Changes saved successfully!')">Save Changes</button>

    </div>
  </div>
</template>

<script>
import navbar from '../navbar/navbar';

export default {
  name: 'Profile', //this is the name of the component
  components: {
    'navbar': navbar
  },
  data() {
    return {
      first_name: "",
      last_name: "",
      language: "",
      time_zone: ""
    };
  },
  methods: {
    alert: function(input) {
      alert(input);
    }
  },
  beforeMount() {
    this.$data.first_name = this.$store.state.user.first_name;
    this.$data.last_name = this.$store.state.user.last_name;
    this.$data.language = "System Default (English CA)";
    this.$data.time_zone = "Eastern Time (US & Canada)";
  }
}
</script>
<style>
#wrapper {
  margin-top: 100px;
}

#profile_pic {
  border-radius: 50%;
}

#main_name {
  font-size: 200%;
  margin-bottom: 40px;
}

#settings div {
  margin-top: 10px;
}

.settings_input {
  display: inline-block;
  width: 50%;
  margin-left: 10px;
  border-radius: 5px;
}

#save {
  margin-top: 30px;
  border-radius: 5px;
  outline: none;
}
</style>
