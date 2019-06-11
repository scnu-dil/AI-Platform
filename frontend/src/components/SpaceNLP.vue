<template>
  <el-container>
    <router-view></router-view>
    <el-header height="60px">
      <router-view/>
      <headertop></headertop>
    </el-header>
    <el-main>
      <el-input placeholder="请输入内容" v-model="input" clearable></el-input>
      <!-- <el-button type="primary" name="submit" onclick="onSubmit()" round>开始分析</el-button> -->
      <el-button type="primary" name="submit" @click="onSubmit" round>开始分析</el-button>  
      <br>
      <hr>
      <div id="nlpbox">
        <div class="nlpbox1">
          <h2>Word Segmentation</h2>
          <!-- <input type="text" class="from_input" placeholder="结果显示"> -->
          <input type="text" class="from_input" placeholder="分词结果显示" v-model=split_result>
        </div>
        <div class="nlpbox1">
          <h2>Part-of-Speech tagging</h2>
          <input type="text" class="from_input" placeholder="词性分析结果显示" v-model=word_tag>
        </div>
        <div class="nlpbox1">   
          <h2>Named Entity Recognition</h2>
          <input type="text" class="from_input" placeholder="命名结果显示">
        </div>
        <div class="nlpbox1">
          <h2>Syntactic parsing</h2>
          <input type="text" class="from_input" placeholder="结果显示">
        </div>
        <div class="nlpbox1">
          <h2>Keywords</h2>
          <input type="text" class="from_input" placeholder="关键词提取结果显示" v-model=key_word>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import HeaderTop from "./HeaderTop";
import axios from 'axios'

export default {
  name: 'SpaceNLP',
  data() {
    return {
      input: "华南师范大学数据智能实验室AI平台",
      split_result: "",
      word_tag: "",
      key_word: ""
    };
  },
  components: {
    headertop: HeaderTop
  },
  mounted(){
    this.onSubmit()
  },
  methods: {
    onSubmit () {
      const path = `http://127.0.0.1:5000/api/nlp`;
      
      axios.get(path,
      {params: {input: this.input}})
        .then(response => {
          this.split_result = response.data.split_result
          this.word_tag = response.data.word_tag
          this.key_word = response.data.key_word
        })
        .catch(error => {
          console.log(error)
        })
    }
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