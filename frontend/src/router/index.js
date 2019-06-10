import Vue from 'vue'
import Router from 'vue-router'
import SpaceNLP from '../components/SpaceNLP'
import Home from '../components/Home'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // }
  //   {
  //     path: '/',
  //     component: Home => require(['../components/Home'], Home),
  //   },
  //   {
  //     path: '/',
  //     component: SpaceNLP => require(['../components/SpaceNLP'], SpaceNLP)
  //   }
  // ]
      {
      path: '/',
      name: 'Home',
      // component: Home => require(['../components/Home'], Home),
      component: Home
    },
    {
      path: '/SpaceNLP',
      name: 'SpaceNLP',
      // component: SpaceNLP => require(['../components/SpaceNLP'], SpaceNLP)
      component: SpaceNLP
    }
  ],
})
