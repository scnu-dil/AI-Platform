<template>
  <el-container>
    <router-view></router-view>
    <el-header height="60px">
      <router-view/>
      <headertop></headertop>
    </el-header>
    <el-main>
      <div id="intext">
        <h2>Subtitle</h2>
        <div class="summarization">
          <input placeholder="请输入标题" class="subinput">
        </div>
        <div class="stext">
          <textarea type="submit" placeholder="请输入正文" class="textinput"></textarea>
          <!-- <div class="surebutton"> -->
          <el-button type="primary" name="submit" onclick="onSubmit()" round>生成摘要</el-button>
          <!-- </div> -->
        </div>
      </div>
      <div id="outtext">
        <h2>Text Summarization</h2>
        <div class="oputtext">
          <textarea placeholder="结果显示" class="from_input"></textarea>
          <!-- <input type="text" class="from_input" placeholder="结果显示"> -->
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

<style scoped>
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
  height: 700px;
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
#intext {
  height: 530px;
  width: 50%;
  float: left;
}
.summarization {
  height: 80px;
  width: 100%;
  padding: 0px 0px 0px 0px;
}
.subinput {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 14px;
  height: 40px;
  width: 90%;
  border-radius: 4px;
  box-sizing: border-box;
  border: 1px solid #dcdfe6;
  outline: 0;
  padding: 0 15px;
}
input::-webkit-input-placeholder {
  text-align: left;
}
.stext {
  height: 500px;
  width: 100%;
}
.textinput {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 16px;
  height: 350px;
  width: 90%;
  border-radius: 4px;
  box-sizing: border-box;
  border: 1px solid #dcdfe6;
  outline: 0;
  padding: 10px 15px;
}
#outtext {
  height: 550px;
  width: 50%;
  float: left;
}
.oputtext {
  padding: 20px 0px 0px 0px;
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
  height: 400px;
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
