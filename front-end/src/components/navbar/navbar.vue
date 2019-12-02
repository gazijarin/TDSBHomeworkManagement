<template>
  <!-- <nav>
      <router-link to="/home">Home</router-link>
      <router-link to="/courses">Courses</router-link>
      <router-link to="/tasks">Tasks</router-link>
      <router-link to="/gallery">Gallery</router-link>
      <router-link to="/tools">Tools</router-link>
  </nav>-->
  <div>
    <b-navbar fixed="top" toggleable="lg" type="light" variant="light">
        <a class="navbar-brand" href="#">
    <img src="https://i.imgur.com/7VlkcFE.png" width="50" height="25" class="d-inline-block align-top" alt="">
  </a>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <!-- <b-navbar-brand href="#"  class="d-inline-block align-top">
        <img src="https://i.imgur.com/7VlkcFE.png" alt="Kitten" />
      </b-navbar-brand> -->

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/home">Home</b-nav-item>
          <b-nav-item to="/courses">Courses</b-nav-item>
          <b-nav-item to="/tasks">Tasks</b-nav-item>
          <b-nav-item to="/progress">Progress</b-nav-item>
          <b-nav-item to="/tools">Tools</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>
                <font-awesome-icon :icon="['fa', 'user-circle']" />
              </em>
            </template>
            <b-dropdown-item to="#">Profile</b-dropdown-item>
            <b-dropdown-item @click="signout()">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>

export default {
  name: "navbar", //this is the name of the component,
  methods: {
    signout: function() {
      this.$gapi.signOut().then(() => {
        this.$store.dispatch("setID", null);
        this.$store.dispatch("setToken", null);
        this.$store.dispatch("setUser", null).then(() => {
                this.$router.push("/");
                console.log("User disconnected."); // eslint-disable-line no-console
            });

      });
    }
  }
};
</script>
