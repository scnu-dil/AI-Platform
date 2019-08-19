<template>
  <!-- <el-container> -->
  <el-main>
    <div id="chatrobotbox">
      <div class="chatheader">
        <h2>AI写诗</h2>
      </div>
	<form>
		<label for="fname">start(诗首)</label>
		<input type="text" id="fname" name="firstname" v-model="input_startwords" placeholder="诗歌开头..(例如“诗情”)">

		<label for="lname">prefix(意境)</label>
		<input type="text" id="lname" name="lastname" v-model="input_prefixwords" placeholder="诗歌意境..(例如“度年一何远，宛转三千雄”)">

		<label for="country">是否藏头诗</label>
		<select id="country" name="country">
		<option value="yes">是</option>
		<option value="no">否</option>
		</select>
	  
		<el-button class="submit" type="submit" name="submit" @click="onSubmit" round>生成诗歌</el-button>
	</form>
	<textarea placeholder="结果显示" class="from_input" readonly="readonly">{{ this.result_poems }}</textarea>	
	</div>
		
	<!-- </div> -->
  </el-main>
  <!-- </el-container> -->
</template>

<script>
import axios from 'axios';

export default {
  name: "chatrobot",
  data() {
	return{
		input_startwords: "",
		input_prefixwords: "",
		result_poems: "",
		input_acrostic: "",
		test: "1"
	}
  },
  methods: {
    onSubmit () {
	  const path = "api_poem/poem"
	  axios.get(path, 
	  {params: {
	  start_words: this.input_startwords,
	  prefix_words: this.input_prefixwords,
	  acrostic: this.input_acrostic
	  }})
	  .then(response=>
	  {
		this.result_poems = response.data.results
	  })
	  var obj=document.getElementById('country');//获取select的id名
	  var index=obj.selectedIndex; //序号，取当前选中选项的序号
	  var opt = obj.options[index].text;//获取当前option的文本内容
	  if(opt=="是")
	  {
		this.test = "1";
		this.input_acrostic = "1";
	  }
	  else
	  {
		this.test = "0";
		this.input_acrostic = "0";
	  }
	}
  },
};
</script>
<style scoped>
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 5em;
  margin: -20px;
  height: 700px;
}
#topbox {
  width: 50%;
  padding: 0em 4.8em 1.2em 15em;
  text-align: left;
}
#chatrobotbox {
  height: 500px;
  width: 80%;
  padding: 0em 5.2em 0em 7em;
  position: relative;
}
.from_input {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 16px;
  height: 200px;
  width: 60%;
  border-radius: 4px;
  box-sizing: border-box;
  border: 1px solid #dcdfe6;
  outline: 0;
  padding: 10px 15px;
}
#messagebox {
  height: 300px;
  /* padding: 0em; */
  padding: 0em 0em 0em 1em;
  /* text-align: left; */
  /* position: relative; */
  background-color: #e9eef3;
}
.messagelist {
  height: 300px;
  width: 100%;
  float: left;
  position: relative;
}
.inputbox {
  position: relative;
  height: 120px;
  width: 100%;
  float: left;
  padding: 0em;
  background: #fff;
}
.inputdata {
  height: 60px;
  width: 100%;
  float: left;
  padding: 0em, 0em, 0em, 0em;
}
.surebox {
  height: 60px;
  float: right;
}

.messagelist {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 1.2em;
  border-radius: 0em;
  box-sizing: border-box;
  border: 1px solid #dcdfe6;
  outline: 0;
  padding: 0.3em 0.7em;
}
.inputdata {
  -webkit-appearance: none;
  background-color: #fff;
  background-image: none;
  font-size: 1.2em;
  border-radius: 0.3em;
  box-sizing: border-box;
  border: 0px;
  outline: 0;
  padding: 0.3em 0.7em;
}
::-webkit-input-placeholder {
  /* WebKit browsers */
  color: rgb(182, 181, 181);
}
/* height: 7em;
  width: 90%; */
  
input[type=text], select {
  width: 41%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.submit {
  width: 10%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background-color: #45a049;
}
div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>

