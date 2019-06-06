<template>
  <el-row class="tac">
    <el-col :span="24">
      <h3 style="text-align:center">AI平台</h3>
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        router
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-s-data"></i>
            <span>实验数据集</span>
          </template>
          <el-menu-item index="1-1">数据集上传</el-menu-item>
          <el-menu-item index="1-2">数据集下载</el-menu-item>
          <el-menu-item index="1-3">数据集删除</el-menu-item>
          <el-menu-item index="1-4">数据集查看</el-menu-item>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span slot="title">模型管理</span>
          </template>
          <el-menu-item index="2-1">模型上传</el-menu-item>
          <el-menu-item index="2-2">模型下载</el-menu-item>
          <el-menu-item index="2-3">模型删除</el-menu-item>
          <el-menu-item index="2-4">模型查看</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-document"></i>
            <router-link to="/SpaceNLP">自然语言处理</router-link>
            <router-view/>
            <!-- <span>自然语言处理</span> -->
          </template>
          <el-menu-item index="3-1">文本分词</el-menu-item>
          <el-menu-item index="3-2">词性标注</el-menu-item>
          <el-menu-item index="3-3">语法分析</el-menu-item>
          <el-submenu index="3-4">
            <template slot="title">句法分析</template>
            <el-menu-item index="3-4-1">等</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="4">
          <i class="el-icon-setting"></i>
          <span slot="title">情绪识别</span>
        </el-menu-item>
        <el-menu-item index="5">
          <i class="el-icon-mic"></i>
          <span slot="title">语音识别</span>
        </el-menu-item>
        <el-submenu index="6">
          <template slot="title">
            <i class="el-icon-s-check"></i>
            <span slot="title">人脸识别</span>
          </template>
          <el-menu-item index="3-1">人脸检测</el-menu-item>
          <el-menu-item index="3-2">人脸匹配</el-menu-item>
          <el-menu-item index="3-3">表情识别</el-menu-item>
        </el-submenu>
        <el-menu-item index="7">
          <i class="el-icon-video-camera-solid"></i>
          <span slot="title">动作识别</span>
        </el-menu-item>
        <el-menu-item index="8">
          <i class="el-icon-camera-solid"></i>
          <span slot="title">物体识别</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>
<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>



