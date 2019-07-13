<template>
  <el-container>
    <el-main>
      <div class="contentbox">
        <div class="navbar">
          <h2 class="navbar-text">聊天机器人</h2>
        </div>

        <div class="content">
          <div>
            <ul class="message-content" ref="messageContent">
              <li v-for="(item, index) in showMsgDatas" :key="index">
                <chat-item :chatItemObj="item"></chat-item>
              </li>
            </ul>
          </div>

          <chat-feature
            :inputDisable="inputDisable"
            :rightDatas="rightDatas"
            @onRightSelectMsg="onRightSelectMsg"
          ></chat-feature>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import ChatItem from "../../components/ChatItem.vue";
import ChatFeature from "../../components/ChatFeature.vue";
import axios from "axios";

export default {
  components: {
    "chat-item": ChatItem,
    "chat-feature": ChatFeature
  },

  data: function() {
    return {
      inputDisable: true, // 是否正在输入
      chatDatas: [], // 所有的聊天数据
      selectMsgData: {}, // 选中的聊天数据
      showMsgDatas: [], // 展示出的聊天数据
      rightDatas: [] // 要说的话
    };
  },

  created: function() {
    this.loadChatData();
  },

  methods: {
    scrollContent: function() {
      this.$nextTick(function() {
        var msgContent = this.$refs.messageContent;
        msgContent.scrollTop = msgContent.scrollHeight;
      });
    },

    // 获取聊天数据
    loadChatData: function() {
      // Que1：
      // js特性 自动插入分号，若打开eslint，则在语句结尾带有‘;’的地方报错。报错内容为：extra semicolon。
      // 参考blog：http://inimino.org/~inimino/blog/javascript_semicolons
      var $this = this;
      this.$http.get("../../static/chatData.json").then(function(res) {
        $this.chatDatas = res.data.msgData;
        $this.setMsg("001");
      });
    },

    // 自动对话
    setMsg: function(selectId) {
      // 获取到指定的数据条目
      this.selectMsgData = this.chatDatas.filter(item => {
        return item.id === selectId;
      })[0];

      // 设置leftData
      this.setShowMsgDatas(this.selectMsgData.leftMsg, "left");

      // 获取到所有的rightData
      this.rightDatas = this.selectMsgData.rightData;
    },

    // 设置显示数据
    setShowMsgDatas: function(msgData, type) {
      var $this = this;
      // 已添加进展示数据的条目
      var i = 0;
      // 对数据的类型进行判断，是属于‘对方’还是‘我’
      if (type === "left") {
        // 修改我们的title，我们需要在data中定义我们的title
        $this.title = "LGD_Sunday正在输入...";
        // inputDisable，表示对方正在输入，这个时候‘我’是不可以进行选择的。
        $this.inputDisable = true;
        // 通过定时器来制造‘对方’输入的延迟
        var interval = setInterval(function() {
          $this.showMsgDatas.push({
            id: $this.selectMsgData.id,
            msg: msgData[i],
            type: type
          });
          // 添加完成之后判断当前的content是否需要滚动
          $this.scrollContent();
          // 展示数据条目自增
          i++;
          // 判断需要展示的数据是否已经全部展示完毕
          if (i >= msgData.length) {
            // 修改我们的title
            $this.title = "和LGD_Sunday聊天中";
            // 重置inputDisable
            $this.inputDisable = false;
            // 清掉定时器
            window.clearInterval(interval);
          }
        }, 1000);
      } else {
        // 如果是‘我’发送的消息，则直接push到showMsgDatas
        this.showMsgDatas.push({
          id: $this.selectMsgData.id,
          msg: msgData[0],
          type: type
        });
        // 执行页面滚动
        $this.scrollContent();
      }
    },

    // 选择要说的话
    onRightSelectMsg: function(item) {
      // 调用setShowMsgDatas放置我的聊天数据
      console.log("Chat.vue # onRightSelectMsg");
      this.setShowMsgDatas(item.rightMsg, "right");
      // 调用setMsg执行我的聊天信息的自动对话
      this.setMsg(item.id);
    }
  }
};
</script>

<style>
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
}

.message-content {
  position: relative;
  overflow-x: hidden;
  overflow-y: scroll;
}

.message-content li {
  padding: 6px 12px;
  list-style: none;
}

.animated {
  animation-duration: 0.4s;
}
</style>
