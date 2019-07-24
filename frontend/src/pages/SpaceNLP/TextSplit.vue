<template>
  <el-container>
    <el-main>
      <div id="topbox">
        <el-input placeholder="请输入一个句子" v-model="input" clearable></el-input>
        <el-button type="primary" name="submit" @click="onSubmit" round>开始分析</el-button>
      </div>
      <hr>
      <div id="nlpbox">
        <div class="nlpbox1">
          <h2>Word Segmentation</h2>
          <textarea type="text" class="from_input1" placeholder="结果显示" readonly="readonly">{{ split_result }}</textarea>
        </div>
        <div class="nlpbox1">
          <h2>Part-of-Speech tagging</h2>
          <textarea type="text" class="from_input2" placeholder="结果显示" readonly="readonly">{{ word_tag }}</textarea>
        </div>
        <div class="nlpbox1">
          <h2>Keywords</h2>
          <textarea type="text" class="from_input3" placeholder="结果显示" readonly="readonly">{{ key_word }}</textarea>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import axios from 'axios';
import HeaderTop from "../../Layout/HeaderTop.vue";
export default {
  name: "split",
  data() {
    return {
      input: "数据智能实验室",
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
      const path = `http://47.107.228.165/api/nlp`;
      
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

<style >
body {
  margin: 0em;
}
.el-header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 2em;
  padding: 0em;
}
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 5em;
}
body > .el-container {
  margin-bottom: 2.5em;
}
.el-menu--horizontal > .el-menu-item {
  float: right;
}
.el-menu--horizontal > .el-submenu {
  float: right;
}
#topbox {
  width: 95%;
  padding: 0em 4.8em 1.2em 15em;
  text-align: left;
}
.el-input {
  font-size: 1em;
  height: 1.5em;
  width: 60%;
}
#nlpbox {
  width: 90%;
  padding: 0em 5.2em 1.2em 15em;
  text-align: left;
  position: relative;
}
.nlpbox1 {
  height: 12em;
  width: 80%;
}
h2 {
  margin-block-start: 0.2em;
  margin-block-end: 0.2em;
}
.from_input1,
.from_input2,
.from_input3 {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 1.2em;
  height: 7em;
  width: 90%;
  border-radius: 0.3em;
  box-sizing: border-box;
  border: 1px solid #dcdfe6;
  outline: 0;
  padding: 0.3em 0.7em;
}
::-webkit-input-placeholder {
  /* WebKit browsers */
  color: rgb(182, 181, 181);
}
</style>
