<template>
  <!-- <el-container> -->
  <div class="bgbox">
    <div class="data-collection upload">
      <div class="boxheader">
        <h2>上传数据集</h2>
      </div>
      <div class="uploadfile">
        <el-upload
          class="upload-demo"
          drag
          action="https://jsonplaceholder.typicode.com/posts/"
          multiple
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">
            将文件拖到此处，或
            <em>点击上传</em>
          </div>
          <!-- <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div> -->
        </el-upload>
      </div>
    </div>
  </div>
  <!-- </el-container> -->
</template>

<script>
export default {
  name: "upload"
};
</script>

<style scoped>
.bgbox {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 5em;
  height: 700px;
  margin: -20px;
  padding: px;
}
body > .el-container {
  margin-bottom: 2.5em;
}
.boxheader {
  padding: 0px 10px 10px 20px;
}
.uploadfile {
  padding: 10px 10px 10px 20px;
}
</style>