<template>
  <el-container>
    <el-main>
      <div id="chatrobotbox">
        <div class="chatheader">
          <h2>聊天机器人</h2>
        </div>
        <div class="messagebox">
          <div class="messagelist"></div>
          <!-- <textarea type="text" class="messagelist" placeholder="消息显示" readonly="readonly"></textarea> -->
          <ul>
            <!-- <li v-for="item in message_array">{{item}}</li> -->
          </ul>
        </div>
        <div class="inputbox">
          <textarea
            type="text"
            v-model="message"
            class="inputdata"
            placeholder="请输入"
            readonly="readonly"
          ></textarea>
          <div class="surebox">
            <el-button v-on:click="dealMessage">确认</el-button>
          </div>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: "chatrobot",
  data: {
    message_array: [],
    message: ""
  },
  methods: {
    dealMessage: function() {
      this.message_array.push(this.message);
      this.message = "";
    }
  },
  directives: {
    // 发送消息后滚动到底部
    "scroll-bottom"() {
      this.vm.$nextTick(() => {
        this.el.scrollTop = this.el.scrollHeight - this.el.clientHeight;
      });
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
#chatrobotbox {
  height: 500px;
  width: 80%;
  padding: 0em 5.2em 0em 7em;
  position: relative;
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
</style>

