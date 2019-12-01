import Vue from 'vue'
import VueRouter from 'vue-router'
import home from '@/components/home/home' // this is the import line to add
import courses from '@/components/courses/courses' // this is the import line to add
import progress from '@/components/progress/progress'
import tasks from '@/components/tasks/tasks' // this is the import line to add
import login from '@/components/login/login' // this is the import line to add
import tools from '@/components/tools/tools'

Vue.use(VueRouter);

const routes = [
  {   
    path: '/',
    name: 'Login',
    component: login
  },
  {
    path: '/home',
    name: 'Home',
    component: home
  },
  {
    path: '/courses',
    name: 'Courses',
    component: courses
  },
  {
    path: '/progress',
    name: 'Progress',
    component: progress
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: tasks
  },
  {
    path: '/tools',
    name: 'Tools',
    component: tools
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
];

const router = new VueRouter({
  routes,
  mode: 'history'
});

export default router
