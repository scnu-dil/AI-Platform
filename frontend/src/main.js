// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import routers from './router'
import VueRouter from 'vue-router'

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(VueRouter)

import Home from "./components/Home.vue";
import SpaceNLP from "./components/SpaceNLP.vue";
import TextSummar from "./components/TextSummar.vue";

const routes = [
  { path: '/home', component: Home },
  { path: '/spacenlp', component: SpaceNLP },
  { path: '/textsummar', component: TextSummar },
  { path: '*', redirect: '/home' }   /*默认跳转路由*/
]

const router = new VueRouter({
  routes // （缩写）相当于 routes: routes
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  routers,
  components: {
    App,
    home: Home,
    spcenlp: SpaceNLP,
    textsummar: TextSummar
  },
  template: '<App/>'
})
