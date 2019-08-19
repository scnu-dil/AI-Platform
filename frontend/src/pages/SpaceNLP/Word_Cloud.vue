<template>
  <el-container>
	<form>
		<textarea type="text" class="from_input1" placeholder="请导入待生成词云的文本内容">{{ cloud_text_en }}</textarea>
		<!-- <el-input placeholder="请输入一个句子" v-model="cloud_text_en" clearable></el-input> -->
		<input type="file" @change="getFile($event)">
		<button @click="submitForm($event)">加载</button>
		<button type="primary" name="submit" @click="submit" round>生成词云</button>
		<div class=divcss5>
			<img :src="flowPic" />
		</div>
			
	</form>

  </el-container>
</template>

<script>
import axios from 'axios';
export default {
	data() {
		return{
			  name: '',
			  age: '',
			  file: 'file',
			  cloud_text_en: '',
			  flowPic: ' '
			};
	},
	methods: {
	  getFile(event) {
		this.file = event.target.files[0];
		console.log(this.file);

	  },
	  submitForm(event) {
		event.preventDefault();
		let formData = new FormData();
		const privateKeyFile = this.file;		
		let reader = new FileReader()
		if (typeof FileReader === 'undefined') {
			this.$message({  
			  type: 'info',
			  message: '您的浏览器不支持FileReader接口'
			})
			return
		}
		reader.readAsText(privateKeyFile)
		let $this = this  // 回头得看懂这一行的作用
		reader.onload = function () {
			$this.cloud_text_en = reader.result
			alert("加载成功")
		}
	  },
		submit () {
			axios.get("http://127.0.0.1:5000/api/word_cloud",
			{params:{content: this.cloud_text_en}}
			)
			.then(response => {
				this.flowPic = response.data.img_url
			})
		}
	},
	uploadPrivateKey () {
		  const privateKeyFile = this.$refs.uploads.uploadFiles[0].raw
		  let reader = new FileReader()
		  reader.readAsText(privateKeyFile)
		  var _this = this
		  reader.onload = function (e) {
			alert("解析成功")
			console.log(e.target.result)
		  }
	}
};

</script>

<style>
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 5em;
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
.inputfile {
	width: 0.1px;
	height: 0.1px;
	opacity: 0;
	overflow: hidden;
	position: absolute;
	z-index: -1;
}
.from_input1 {
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
.divcss5 img{
  width:300px;
  height:300px;
} 
</style>
