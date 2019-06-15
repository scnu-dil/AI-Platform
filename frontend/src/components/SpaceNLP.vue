<template>
  <el-container>
    <router-view></router-view>
    <el-header height="60px">
      <router-view/>
      <headertop></headertop>
    </el-header>
    <el-main>
      <el-input placeholder="请输入一个句子" v-model="input" clearable></el-input>
      <el-button type="primary" name="submit" onclick="onSubmit()" round>开始分析</el-button>
      <br>
      <hr>
      <div id="nlpbox">
        <div class="nlpbox1">
          <h2>Word Segmentation</h2>
          <textarea type="text" class="from_input" placeholder="结果显示" readonly="readonly"></textarea>
        </div>
        <div class="nlpbox1">
          <h2>Part-of-Speech tagging</h2>
          <textarea type="text" class="from_input" placeholder="结果显示" readonly="readonly"></textarea>
        </div>
        <div class="nlpbox1">
          <h2>Named Entity Recognition</h2>
          <textarea type="text" class="from_input" placeholder="结果显示" readonly="readonly"></textarea>
        </div>
        <div class="nlpbox1">
          <h2>Syntactic parsing</h2>
          <textarea type="text" class="from_input" placeholder="结果显示" readonly="readonly"></textarea>
        </div>
        <div class="nlpbox1">
          <h2>Keywords</h2>
          <textarea type="text" class="from_input" placeholder="结果显示" readonly="readonly"></textarea>
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
body {
  margin: 0px;
}
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
  width: 60%;
  padding: 0px 100px 20px 240px;
  text-align: left;
}
.nlpbox1 {
  height: 230px;
  width: 100%;
}
h2 {
  margin-block-start: 0.2em;
  margin-block-end: 0.2em;
}
.from_input {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 16px;
  height: 150px;
  width: 90%;
  border-radius: 4px;
  box-sizing: border-box;
  border: 1px solid #dcdfe6;
  outline: 0;
  padding: 10px 15px;
}
::-webkit-input-placeholder {
  /* WebKit browsers */
  color: rgb(182, 181, 181);
}
</style>