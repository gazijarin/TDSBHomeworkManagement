<template>
  <div class="col-12" id="container" style="margin-top: 5%;">
    <b-navbar fixed="top" toggleable="lg" type="light" variant="light">
      <a class="navbar-brand" href="#">
        <img
          src="https://i.imgur.com/7VlkcFE.png"
          width="60"
          height="25"
          class="d-inline-block align-top"
          alt
        />
      </a>
    </b-navbar>

    <div class="slanted" style="background-color: #79BC6D; z-index: -5;"></div>
    <div class="slanted" style="background-color: #FCB711; margin-left: 11%; z-index: -6;"></div>
    <div class="slanted" style="background-color: #4277A5; margin-left: 25%; z-index: -7;"></div>
    <div class="slanted" style="background-color: #EC7B1C; margin-left: 30%; z-index: -8;"></div>

    <div class="col-4" style="float: right; padding-top: 300px;">
      <div class="content">
        <div class id="inputForm">
          <div>
            <h3 class="headline mb-0">
              <b>Welcome, Student.</b>
            </h3>
            <p class="subheading">
              <b>Log-in below using your TDSB Google account.</b>
            </p>
          </div>

          <button
            type="primary"
            icon="fas fa-edit"
            @click="handleClickSignIn"
            class="btn btn-lg btn-primary pull-xs-right"
          >Log-in</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

import axios from "axios";
export default {
  name: "login",
  props: {
    msg: String
  },
  data() {
    return {
      profile: null,
      _id: null,
      first_name: null,
      last_name: null,
      image: null,
      email: null,
      courses: []
    };
  },
  methods: {
    handleClickLogin() {
      this.$gapi
        .getAuthCode()
        .then(authCode => {
          //on success
          console.log("authCode", authCode);
        })
        .catch(error => {
          //on fail do something
        });
    },

    //Sign in
    handleClickSignIn() {
      this.$gapi
        .signIn()
        .then(user => {
          //on success

          (this._id = user.id), (this.first_name = user.firstname);
          this.last_name = user.lastname;
          this.image = user.image;
          this.email = user.email;

          this.$gapi
            .request({
              path: `https://classroom.googleapis.com/v1/courses?studentId=${this._id}&key=AIzaSyCHTg9xYmGmauaWLs7uqS99FxwcD_tEqlI`,
              method: "GET"
            })
            .then(response => {
              //console.log(response.body)
              const payLoad = {
                _id: this._id,
                first_name: this.first_name,
                last_name: this.last_name,
                image: this.image,
                email: this.email,
                courses: JSON.parse(response.body).courses
              };

              var post_url;
              if (
                process.env.NODE_ENV &&
                process.env.NODE_ENV == "production"
              ) {
                post_url = "/api/students";
              } else {
                post_url = "http://localhost:5000/api/students";
              }
              this.$store.dispatch("setUser", payLoad);
              axios.post(post_url, payLoad).then(console.log(payLoad));
            });

          //direct to user home
          this.$router.push({
            name: "Home"
          });
        })
        .catch(error => {
          console.log(error);
          console.log("Something went wrong");
        });
    }

    //NOTE: METHOD FOR SIGNING OUT

    // handleClickSignOut() {
    //   this.$gAuth
    //     .signOut()
    //     .then(() => {
    //       //on success do something
    //       this.isSignIn = this.$gAuth.isAuthorized;
    //     })
    //     .catch(error => {
    //       //on fail do something
    //     });
    // }
  }
};
</script>

<style>
.slanted {
  height: 100%;
  width: 60%;
  position: fixed;
  top: 0;
  left: -40%;
  overflow: hidden;
  transform: skewX(-15deg);
  transition: left 1s;
}
.slanted:hover {
  left: -38%;
}
</style>
