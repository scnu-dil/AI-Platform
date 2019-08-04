<template>
  <el-form :model="form">
    <el-form-item label="测试图片" :label-width="formLabelWidth">
      <el-upload
        ref="upload"
        name="upload"
        action="http://127.0.0.1:5000/getMsg"
        accept="image/png,image/gif,image/jpg,image/jpeg"
        list-type="picture-card"
        :limit=limitNum
        :auto-upload="false"
        :on-exceed="handleExceed"
        :before-upload="handleBeforeUpload"
        :on-preview="handlePictureCardPreview"
        :on-remove="handleRemove">
        <i class="el-icon-plus"></i>
      </el-upload>
      <el-dialog :visible.sync="dialogVisible">
        <img width="100%" :src="dialogImageUrl" alt="">
      </el-dialog>
    </el-form-item>

    <el-form-item>
      <el-button size="small" type="primary" @click="uploadFile">立即上传</el-button>
    </el-form-item>
<el-form-item label="检测图片" :label-width="formLabelWidth">
      <el-upload
        ref="upload1"
        name="upload1"
        action="http://127.0.0.1:5000/getPic"
        accept="image/png,image/gif,image/jpg,image/jpeg"
        list-type="picture-card"
        :limit=limitNum1
        :auto-upload="false"
        :on-exceed="handleExceed1"
        :before-upload="handleBeforeUpload"
        :on-preview="handlePictureCardPreview"
        :on-remove="handleRemove">
        <i class="el-icon-plus"></i>
      </el-upload>
      <el-dialog :visible.sync="dialogVisible">
        <img width="100%" :src="dialogImageUrl" alt="">
      </el-dialog>
    </el-form-item>
    <el-form-item>
      <el-button size="small" type="primary" @click="uploadFile1">立即上传</el-button>
    </el-form-item>
    <el-form-item>
      <el-button size="small" type="primary" @click="getData">开始识别</el-button>
    </el-form-item>
    <el-form-item>
      <h3>结果图像</h3>
	<img :src="imgUrl" alt="" width="800"/>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return{
      dialogImageUrl: '',
      dialogVisible: false,
      formLabelWidth: '80px',
      limitNum: 3,
	limitNum1:1,
      form: {},
      imgUrl:''
    }
  },
  methods: {
    // 上传文件之前的钩子
    handleBeforeUpload(file){
      console.log('before')
      if(!(file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type === 'image/jpeg')) {
        this.$notify.warning({
          title: '警告',
          message: '请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片'
        })
      }
      let size = file.size / 1024 / 1024 / 2
      if(size > 2) {
        this.$notify.warning({
          title: '警告',
          message: '图片大小必须小于2M'
        })
      }
    },
    // 文件超出个数限制时的钩子
    handleExceed(files, fileList) {
this.$notify.warning({
          title: '警告',
          message: '最多上传3张图片！'
        })
    },
 handleExceed1(files, fileList) {
this.$notify.warning({
          title: '警告',
          message: '最多上传1张图片！'
        })
    },
    // 文件列表移除文件时的钩子
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    // 点击文件列表中已上传的文件时的钩子
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    uploadFile() {
      this.$refs.upload.submit()
    },
    uploadFile1() {
      this.$refs.upload1.submit()
    }, getData() {
          let that=this;
          const path = 'http://127.0.0.1:5000/checkFace';
          axios.get(path).then(function (response) {
            var msg = response.data.msg;
            that.imgUrl=msg+"?"+response.data.times;
          }).catch(function (error) {
            alert('Error ' + error);
          })
        }
  } 
}
</script>

