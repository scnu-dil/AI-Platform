<template>
  <el-container>
    <router-view></router-view>
    <el-header height="60px">
      <router-view/>
      <headertop></headertop>
    </el-header>
    <el-main>
      <el-input placeholder="请输入内容" v-model="input" clearable></el-input>
      <el-button type="primary" name="submit" onclick="onSubmit()" round>开始分析</el-button>
      <br>
      <hr>
      <div id="nlpbox">
        <div class="nlpbox1">
          <h2>Word Segmentation</h2>
          <input type="text" class="from_input" placeholder="结果显示">
        </div>
        <div class="nlpbox1">
          <h2>Part-of-Speech tagging</h2>
          <input type="text" class="from_input" placeholder="结果显示">
        </div>
        <div class="nlpbox1">
          <h2>Named Entity Recognition</h2>
          <input type="text" class="from_input" placeholder="结果显示">
        </div>
        <div class="nlpbox1">
          <h2>Syntactic parsing</h2>
          <input type="text" class="from_input" placeholder="结果显示">
        </div>
        <div class="nlpbox1">
          <h2>Keywords</h2>
          <input type="text" class="from_input" placeholder="结果显示">
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import HeaderTop from "./HeaderTop";

export default {
  data() {
    return {
      input: ""
    };
  },
  components: {
    headertop: HeaderTop
  }
};
</script>

<style>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
  padding: 0px;
}
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 80px;
}
body > .el-container {
  margin-bottom: 40px;
}
.el-menu--horizontal > .el-menu-item {
  float: right;
}
.el-menu--horizontal > .el-submenu {
  float: right;
}
.el-input {
  font-size: 14px;
  height: 40px;
  width: 60%;
}
#nlpbox {
  width: 600px;
  padding: 0px 100px 20px 230px;
  text-align: left;
}
.nlpbox1 {
  height: 150px;
}
h2 {
  margin-block-start: 0.6em;
  margin-block-end: 0.6em;
}
.from_input {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 14px;
  height: 40px;
  width: 60%;
  border-radius: 4px;
  box-sizing: border-box;
  border: 1px solid #dcdfe6;

  outline: 0;
  padding: 0 15px;
}
::-webkit-input-placeholder {
  /* WebKit browsers */
  color: rgb(182, 181, 181);
}
</style>