<template>
  <el-container>
    <el-main>
      <div class="data-collection upload">
        <div class="boxheader">
          <h2>上传数据集</h2>
        </div>
        <div class="uploadfile">
          <el-upload
            class="upload-demo"
            drag  
      accept=".csv,.txt"
      multiple  
            name="file"
      :action="import_url"
      :headers="importHeaders"
      :before-upload="beforeUpload"
      :on-preview="handlePreview"
      :data="upload_data"
      :on-success="uploadSuccess"
      :on-error="uploadFail"
      :auto-upload="false"
      :show-file-list="true"
      ref="commit"
    >     <!-- accept="image/jpeg,image/gif,image/png, file/txt, file/csv" -->
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">
              将文件拖到此处，或
              <em>点击加载</em>
            </div>
            <!-- <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div> -->
          </el-upload>
     <el-button size="small" type="primary" name="submit" @click="submitUpload">立即上传</el-button>
     <el-button size="small" @click="cancel_upload">取消</el-button>
      </div>
  <!-- </el-container> -->
</template>

<script>
//import axios from 'axios'

export default {
  name: "upload",
  data(){
    return{
    
      importHeaders: {
        enctype: "multipart/form-data"
      },
      import_url: "http://127.0.0.1:5000/upload"
    };
  },

  methods: {
    beforeUpload(file) {
      //上传前配置
    },
    upload_data(){
      //传给后台的数据
      dataType: "0"
      data_back: 22
    },
    handlePreview(file) {
      //接收后端传来的数据
    },
    submitUpload(){
      //点击，触发上传功能
      this.$refs.commit.submit()
    },
    onUploadChange(file)
    {
      
/*      const isIMAGE = (file.raw.type === 'image/jpeg' || file.raw.type === 'image/png'|| file.raw.type === 'image/gif' === 'file/csv');
      const isLt1M = file.size / 1024 / 1024 < 1;

      if (!isIMAGE) {
        this.$message.error('上传文件只能是图片格式!');
        return false;
      }
      if (!isLt1M) {
        this.$message.error('上传文件大小不能超过 1MB!');
        return false;
      }
      var reader = new FileReader();
      reader.readAsDataURL(file.raw);
/*      reader.onload = function(e){
      console.log(this.result)//图片的base64数据
      }*/
    },
    //上传成功
    uploadSuccess(response, file, fileList) {
      this.$notify.success({
      title: '成功',
      message: `文件上传成功`
      });
      this.clearFiles()
    },
    uploadFail(err, file, fileList) {
      this.$notify.error({
      title: '错误',
      message: `文件上传失败`
      });
    }
  }
  
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
