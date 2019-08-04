<template>
  <!-- <div class="nlp-textsum textsum">文本摘要</div> -->
  <!-- <el-container> -->
  <el-main>
    <div id="intext">
      <h2>Subtitle</h2>
      <div class="summarization">
        <input placeholder="请输入标题" class="subinput" v-model="sub_input"/>
      </div>
      <div class="stext">
        <textarea type="submit" placeholder="请输入正文" class="textinput" v-model="text_input"></textarea>
        <!-- <div class="surebutton"> -->
        <el-button type="primary" name="submit" @click="onSubmit" round>生成摘要</el-button>
        <!-- </div> -->
      </div>
    </div>
    <div id="outtext">
      <h2>Text Summarization</h2>
      <div class="oputtext">
        <textarea placeholder="结果显示" class="from_input">{{ summary_result }}</textarea>
        <!-- <input type="text" class="from_input" placeholder="结果显示"> -->
      </div>
    </div>
  </el-main>
  <!-- </el-container> -->
</template>

<script>
import HeaderTop from "../../Layout/HeaderTop.vue";
import axios from 'axios';
export default {
  name: "textsum",
  data() {
    return {
      input: "",
      summary_result: "",
      sub_input: "美联储10年来首次降息",
      text_input: "\
　　中新社纽约7月31日电 美国联邦储备委员会31日宣布将联邦储备基金利率下调至2%-2.25%区间。这是2008年12月以来美联储首次降息。\
\n　　为期两天的货币政策例会于31日结束。美联储会后发布声明称，6月以来，美国劳动力市场保持强劲，经济温和增长。近几个月就业岗位增长稳定，失业率维持在低位。尽管家庭开支比年初有所增加，但商业固定资产投资仍疲软。总体通货膨胀率和除食品、能源之外的各类商品通胀率仍低于美联储设置的2%政策目标。\
\n　　美联储主席鲍威尔在当天的记者会上说，相信降息有利于美国经济，不仅可以降低短期借贷的成本，也能在增强信心方面发挥作用。他称此次降息是'周期中政策调整'，美联储认为目前没有必要进入长时间的降息周期。\
\n　　鲍威尔同时表示，降息确实有防范风险方面的考虑。他说目前贸易问题已经给美国经济带来冲击，近期商业及制造业投资疲软就是表现。他说，美联储缺乏应对贸易问题的经验，需要探索应对之策。他同时强调美国经济本身仍然健康，风险主要来自外部。\
\n　　美国总统特朗普近期多次批评美联储的货币政策，称应当降息。鲍威尔31日在记者会上说，此次降息与特朗普的言论无关，美联储围绕实现充分就业和物价稳定的目标制定政策，不会因政治压力或'为证明自身独立性'而调整政策。\
\n　　由于降息可以为市场提供更充足的流动性，一般被认为是股市的利好消息。但当天纽约股市三大股指仍然收跌，跌幅均超过1%。《华尔街日报》援引分析人士观点称，市场原本希望鲍威尔会采取更为'鸽派'的姿态，但他否认进入降息周期的言论令市场期望落空。\
\n　　为应对金融危机，美联储于2008年12月17日将联邦储备基金利率降至0-0.25%，并维持至2015年12月启动加息周期。截至2018年年底，美联储共加息9次，其中4次在2018年。"
    };
  },
  components: {
    headertop: HeaderTop
  },
  mounted() {
    this.onSubmit()
  },
  methods: {
    onSubmit() {
      const path = '/split/api/summary';
      axios.get(path,
      {params: {sub_input: this.sub_input,
		text_input: this.text_input}})
        .then(response => {
          this.summary_result = response.data.result
        })
        .catch(error => {
          console.log(error)
        })
    }
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
  margin: -20px;
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
