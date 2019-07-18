import Vue from 'vue'
import Router from 'vue-router'

import Container from '@/Layout/Container'

import DelelteData from '@/pages/DataCollection/DelelteData'
// import Download from '@/pages/DataCollection/Download'
import Upload from '@/pages/DataCollection/Upload'
import Query from '@/pages/DataCollection/Query'
import TextSummar from '@/pages/SpaceNLP/TextSummar'
import TextSplit from '@/pages/SpaceNLP/TextSplit'
import ChatRobot from '@/pages/SpaceNLP/ChatRobot'
import Chat from '@/pages/SpaceNLP/Chat'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Container,
      redirect: '/DataCollection/Upload',
      children: [
        {
          name: '数据集上传',
          path: 'DataCollection/Upload',
          component: Upload
        },
        // {
        //   name: '数据集下载',
        //   path: 'DataCollection/Download',
        //   component: Download
        // },
        {
          name: '数据集删除',
          path: 'DataCollection/Delete',
          component: DelelteData
        },
        {
          name: '数据集列表',
          path: 'DataCollection/Query',
          component: Query
        }
      ]
    },
    {
      path: '/',
      component: Container,
      redirect: '/SpaceNLP/TextSplit',
      children: [
        {
          name: '文本分词',
          path: '/SpaceNLP/TextSplit',
          component: TextSplit
        },
        {
          name: '文本摘要',
          path: '/SpaceNLP/TextSummar',
          component: TextSummar
        },
        {
          name: '聊天机器人',
          path: '/SpaceNLP/ChatRobot',
          component: ChatRobot
        },
        {
          name: '对话系统',
          path: '/SpaceNLP/Chat',
          component: Chat
        }
        // children:[
        //   {
        //     name: '对话系统',
        //     path: '/SpaceNLP/Chat',
        //     component: Chat
        //   }
        // ]
      ]
    }
  ]
})
