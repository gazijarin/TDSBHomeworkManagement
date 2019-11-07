<template>
  <div class="col-12" id="container" style="margin-top: 5%;">

    <div class="col-4" style="float: right; padding-top: 100px;">
     <div class="content">
      <div class="" id="inputForm"> 
        <div>
          <h3 class="headline mb-0"> <b>Welcome Student</b></h3>
          <p class="subheading"><b>Login below using your TDSB google Account </b></p>
        </div>
        
        <button type="primary"
            icon="fas fa-edit"
            @click="handleClickSignIn"
            class="btn btn-lg btn-primary pull-xs-right
            ">
            Google Log in
            </button>
       </div>
     </div>
   </div>
  </div>
</template>

<script>
/* eslint-disable */

import axios from 'axios';
export default {
  name: "login",
  props: {
    msg: String
  },
  data() {
    return {
      profile: null
    };
  },
  methods: {
    handleClickLogin() {
      this.$gAuth
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
      this.$gAuth
        .signIn()
        .then(GoogleUser => {
          //on success 

          this.profile = GoogleUser.getBasicProfile()
          const payLoad = {
            _id: this.profile.getId(),
            first_name: this.profile.getGivenName(),
            last_name: this.profile.getFamilyName(),  
            image: this.profile.getImageUrl(),
            email: this.profile.getEmail(),  
          }

          axios.post('http://localhost:5000/api/students', payLoad)
          .then(
            console.log(payLoad)
          )

          //bearer token
          //const token = GoogleUser.getAuthResponse().access_token;

          this.$store.dispatch('setUser', payLoad)
          
          //direct to user home
          this.$router.push({
          name: 'Home'
          })
          // console.log("GoogleUser", GoogleUser);
          // console.log("getId", GoogleUser.getId());
          // console.log("getBasicProfile", GoogleUser.getBasicProfile());
          // console.log("getAuthResponse", GoogleUser.getAuthResponse());
          // console.log(
          //   "getAuthResponse",
          //   this.$gAuth.GoogleAuth.currentUser.get().getAuthResponse()
          // );
          //this.isSignIn = this.$gAuth.isAuthorized;
        })
        .catch(error => {
          console.log('Something went wrong')
        });
    },

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
  },
};
</script>

<style>

</style>
