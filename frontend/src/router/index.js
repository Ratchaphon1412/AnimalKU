import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from "@/views/Dashboard";

const routes = [
  {
    path: '/',
    name: 'home',
    component: function () {
      return import(/* webpackChunkName: "Main" */ '../views/Main.vue')
    }
  },
  {
    path:'/Login',
    name:'Login',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Login.vue')
    }
  },
  {
    path:'/Dashboard',
    name: 'Dashboard',
    component: function () {
      return import(/* webpackChunkName: "dashboard"*/'@/views/Dashboard.vue')
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
