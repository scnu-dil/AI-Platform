<template>
  <div id="spacenlp">
    <el-input placeholder="请输入内容" v-model="input" clearable></el-input>
    <el-button type="primary" round>主要按钮</el-button>
    <br>
    <br>
    <br>
    <br>
    <hr>
    <div id="nlpbox">
      <div class="nlpbox1">
        <h2>Word Segmentation</h2>
        <input type="text" class="from_input" placeholder="结果显示">
      </div>
      <div class="nlpbox2">
        <h2>Named Entities</h2>
        <el-input v-model="input" placeholder="结果显示"></el-input>
      </div>
      <div class="nlpbox3">
        <h2>Person Standard</h2>
        <el-input v-model="input" placeholder="结果显示"></el-input>
      </div>
      <div class="nlpbox4">
        <h2>Person Named Entity</h2>
        <el-input v-model="input" placeholder="结果显示"></el-input>
      </div>
      <div class="nlpbox5">
        <h2>Keywords</h2>
        <el-input v-model="input" placeholder="结果显示"></el-input>
      </div>
      <div class="nlpbox6">
        <h2>Polarity</h2>
        <el-input v-model="input" placeholder="结果显示"></el-input>
      </div>
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: ""
    };
  }
};
</script>

<style>
.el-input {
  font-size: 14px;
  height: 40px;
  width: 50%;
}
#nlpbox {
  width: 600px;
}
.nlpbox1 {
  height: 100px;
}
.nlpbox2 {
  height: 100px;
}
.nlpbox3 {
  height: 100px;
}
.nlpbox4 {
  height: 100px;
}
.nlpbox5 {
  height: 100px;
}
.nlpbox6 {
  height: 100px;
}
.from_input {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 14px;
  height: 40px;
  width: 50%;
  border-radius: 4px;
  box-sizing: border-box;
  border: 1px solid #dcdfe6;
  color: #606266;
  outline: 0;
  padding: 0 15px;
}
</style>