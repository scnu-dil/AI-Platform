<template>
  <el-main>
    <div class="contentbox">
      <div class="navbar">
        <h2 class="navbar-text">聊天机器人</h2>
      </div>
      <!-- 这是消息框的容器 -->
      <div class="content">
        <ul class="message-content">
          <li v-for="(item, index) in showMsgDatas" :key="index">
            <chat-item :chatItemObj="item"></chat-item>
          </li>
        </ul>

        <!--           <chat-feature
            :inputDisable="inputDisable"
            :rightDatas="rightDatas"
            @onRightSelectMsg="onRightSelectMsg"
        ></chat-feature>-->
        <!-- ----------------Lijuce add------------------------------- -->

        <!-- --------------------------------------------------------- -->
      </div>
      <div class="chat-footer" ref="messageContent">
        <el-input placeholder="请输入内容" v-model="input_text" class="send-msg" clearable></el-input>
        <!-- <el-input class="send-msg" placeholder="请输入消息内容" v-model="input_text" clearable></el-input> -->
        <el-button class="send-sure" @click="onSubmit">发送</el-button>
      </div>
    </div>
  </el-main>
</template>

<script scoped>
import ChatItem from "../../components/ChatItem.vue";
// import  from "../../components/ChatFeature.vue";
import axios from "axios";

export default {
  data() {
    return {
      input_text: ""
    };
  },
  components: {
    "chat-item": ChatItem
    // "chat-feature": ChatFeature
  },
  // mounted() {
  //   this.scrollToBottom();
  // },
  // //每次页面渲染完之后滚动条在最底部
  // updated: function() {
  //   this.scrollToBottom();
  // },

  // watch: {
  //   processData: "scrollToBottom"
  // },
  // scrollToBottom: function() {
  //   this.$nextTick(() => {
  //     var div = this.$el.querySelector("message-content");
  //     div.scrollTop = div.scrollHeight;
  //   });
  // },
  data: function() {
    return {
      inputDisable: true, // 是否正在输入
      chatDatas: [], // 所有的聊天数据
      selectMsgData: {}, // 选中的聊天数据
      showMsgDatas: [], // 展示出的聊天数据
      rightDatas: [], // 要说的话
      input_text: "",
      id: "123",
      message: "111"
    };
  },
  // created: function() {
  //   this.loadChatData();
  // },
  methods: {
    // 滚动条判断
    scrollContent: function() {
      this.$nextTick(function() {
        var msgContent = this.$refs.messageContent;
        // var msgContent = document.querySelector("messageContent");
        msgContent.scrollTop = msgContent.scrollHeight;
        // msgContent.scrollIntoView();
      });
    },
    // scrollToBottom() {
    //   this.$nextTick(() => {
    //     var div = this.$el.querySelector("message-content");
    //     div.scrollTop = div.scrollHeight;
    //   });
    // },

    // 获取聊天数据
    loadChatData: function() {
      var $this = this;

      axios
        .get("api/medical", {
          params: {
            q: this.input_text,
            id: "123"
          }
        })
        .then(function(res) {
          $this.showMsgDatas.push({
            msg: $this.input_text,
            type: "left"
          });
          $this.showMsgDatas.push({
            msg: res.data.bot_response,
            type: "right"
          });
        });
    },
    // 选择要说的话
    onSubmit() {
      console.log("Chat.vue # loadChatData");
      this.loadChatData();
      this.scrollContent();
    }
  }
};
</script>

<style scoped>
.contentbox {
  position: relative;
  width: 80%;
  padding: 0em 5em 0em 7em;
}
.navbar {
  height: 44px;
  display: flex;
}

.navbar-text {
  margin: 0px auto;
  line-height: 44px;
}

.content {
  position: relative;
  height: 500px;
  background: linear-gradient(to bottom, #57b1ff, #c0e2ff);
  overflow-x: hidden;
  overflow-y: scroll;
}
/*position: relative;*/
/* .message-content ul {

  overflow-x: hidden;
  overflow-y: scroll;
} */

.message-content li {
  padding: 6px 12px;
  list-style: none;
}
.send-btn img {
  width: 32px;
  margin: 6px 18px 6px 6px;
  float: right;
}

.animated {
  animation-duration: 0.4s;
}

.chat-footer {
  /* background: linear-gradient(to bottom, #f3f3f3, #e3e2e2); */
  height: 46px;
  position: relative;
  bottom: 0;
  left: 0px;
  right: 0;
  z-index: 90;
  width: 100%;
}

.send-msg {
  position: float;
  display: inline-block;
  width: 88%;
  height: 30px;
  border-radius: 4px;
  float: left;
  color: #bbb;
  margin: 6px 0 0px 0px;
  text-align: left;
  line-height: 30px;
  padding-left: 0px;
}

.send-sure {
  display: inline-block;
  width: 12%;
  height: 40px;
  border: 1px solid rgb(236, 225, 225);
  border-radius: 6px;
  /* float: right; */
  background-color: #fff;
  color: rgb(124, 124, 124);
  margin: 6px 0px 0px 0px;
  text-align: center;
  padding: 1px 1px 1px 1px;
  line-height: 30px;
  /* padding-left: 8px; */
}

.fast {
  animation-duration: 0.2s;
}

.fadeIn {
  display: block;
}

.fadeOut {
  display: none;
}
</style>
