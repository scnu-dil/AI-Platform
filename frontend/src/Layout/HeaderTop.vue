<template>
  <div class="header">
    <div id="pfname">
      <h1>AI平台</h1>
    </div>
    <!-- <div id="pfheaderbox">
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
      >
        <el-menu-item index="1" style="text-align:right" class="atext">处理中心</el-menu-item>
        <el-submenu index="2">
          <template slot="title" class="atext">我的工作台</template>
          <el-menu-item index="2-1" style="text-align:left">自然语言处理</el-menu-item>
          <el-menu-item index="2-2">情绪识别</el-menu-item>
          <el-menu-item index="2-3">动作识别</el-menu-item>
          <el-submenu index="2-4">
            <template slot="title">人脸识别</template>
            <el-menu-item index="2-4-1">人脸检测</el-menu-item>
            <el-menu-item index="2-4-2">人脸匹配</el-menu-item>
            <el-menu-item index="2-4-3">选项3</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="3" class="atext">消息中心</el-menu-item>
        <el-menu-item index="4">
          <a href="http://localhost:8081/#/home" class="atext">主页</a>
        </el-menu-item>
      </el-menu>
      <div></div> 
    </div>-->
    <!-- <div class="logo">
      <img src="~@/assets/logo.png" alt>
    </div>-->
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>
<style>
.header {
  display: flex;
  height: 60px;
  justify-content: space-between;
  background: linear-gradient(
    90deg,
    rgba(66, 161, 255, 1) 0,
    rgba(66, 161, 255, 0.6) 100%
  );
  /* position: relative; */
  z-index: 1000;
}
#pfname {
  text-align: center;
  padding: 1em 0em 0em 4em;
}
#pfheaderbox {
  height: 60px;
}
.el-menu-demo el-menu--horizontal el-menu {
  height: 60px;
}
</style>
