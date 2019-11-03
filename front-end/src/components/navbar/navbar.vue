<template>
    <!-- <nav>
      <router-link to="/home">Home</router-link>
      <router-link to="/courses">Courses</router-link>
      <router-link to="/tasks">Tasks</router-link>
      <router-link to="/gallery">Gallery</router-link>
      <router-link to="/tools">Tools</router-link>
    </nav> -->
    <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-brand>TDSB App</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
            <b-nav-item to="/home">Home</b-nav-item>
            <b-nav-item to="/courses">Courses</b-nav-item>
            <b-nav-item to="/tasks">Tasks</b-nav-item>
            <b-nav-item to="/gallery">Gallery</b-nav-item>
            <b-nav-item to="/tools">Tools</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
                <em>User</em>
            </template>
            <b-dropdown-item to="#">Profile</b-dropdown-item>
            <b-dropdown-item to="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
        </b-navbar-nav>
        </b-collapse>
    </b-navbar>
    </div>
</template>
