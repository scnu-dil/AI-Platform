<template>
  <div>
    <div class="chat-footer" @click="onTogglePop()">
      <el-input class="send-msg" placeholder v-model="input" clearable></el-input>
      <el-button class="send-sure">发送</el-button>
    </div>
    <!-- <div class="send-msg-pop animatd fast" :class="[togglePop ? 'slideInup' : 'slideOutDown']">
      <div class="chat-footer">
        <div class="send-msg">想要发送的内容...</div>
        <ul>
          <li
            v-for="(item, index) in rightDatas"
            :key="index"
            @click="onRightSelectMsg(item)"
          >{{item.rightMsg[0]}}</li>
        </ul>
      </div>
    </div>-->

    <!-- <div class="pop-bg animated" :class="[togglePop ? 'fadeIn' : 'fadeOut']" @click="onTogglePop()"></div> -->
  </div>
</template>

<script>
export default {
  props: {
    // 是否正在输入
    inputDisable: {
      type: Boolean,
      required: true,
      default: true
    },
    // '我'将要说的话
    rightDatas: {
      type: Array,
      required: true,
      default: function() {
        return {
          rightDatas: []
        };
      }
    }
  },
  // data: function() {
  //   return {
  //     togglePop: false // 展示浮窗
  //   };
  // },
  data() {
    return {
      input: ""
    };
  },
  methods: {
    // 控制pop的显示和隐藏
    onTogglePop: function() {
      // 当”对方“正在输入的时候，不允许点击
      if (this.inputDisable) {
        return;
      }
      this.togglePop = !this.togglePop;
    },
    // 选择要说的话
    onRightSelectMsg: function(item) {
      // 调用父组件（Chat.vue）中的onRightSelectMsg方法
      console.log("ChatFeature.vue # onRightSelectMsg");
      this.$emit("onRightSelectMsg", item);
      // 隐藏展示浮层
      this.togglePop = false;
    }
  }
};
</script>

<style>
.chat-footer {
  /* background: linear-gradient(to bottom, #f3f3f3, #e3e2e2); */
  height: 46px;
  position: absolute;
  bottom: 0;
  left: 0px;
  right: 0;
  z-index: 90;
  width: 100%;
}

.send-msg {
  position: float;
  display: inline-block;
  width: 80%;
  height: 30px;
  border-radius: 4px;
  float: left;
  color: #bbb;
  margin: 6px 0 0px 0px;
  text-align: left;
  line-height: 30px;
  padding-left: 0px;
}
.el-input {
  width: 80%;
}
.send-sure {
  display: inline-block;
  width: 12%;
  height: 40px;
  border: 1px solid rgb(236, 225, 225);
  border-radius: 6px;
  float: right;
  background-color: #fff;
  color: rgb(124, 124, 124);
  margin: 6px 0px 0px 0px;
  text-align: center;
  padding: 1px 1px 1px 1px;
  line-height: 30px;
  /* padding-left: 8px; */
}

.send-btn img {
  width: 32px;
  margin: 6px 18px 6px 6px;
  float: right;
}

.send-msg-pop {
  z-index: 100;
  position: absolute;
  width: 70%;
  bottom: 0px;
}

.send-msg-pop .chat-footer {
  position: relative;
}

.send-msg-pop .chat-footer img {
  transform: rotate(45deg);
}

.send-msg-pop ul {
  position: absolute;
  background-color: white;
  margin: 0;
  height: 32px;
  padding: 2px;
  right: 56px;
  bottom: 5px;
  overflow-x: hidden;
  overflow-y: scroll;
}

.send-msg-pop ul li {
  border-bottom: 1px solid rgba(187, 187, 187, 0.39);
  min-height: 22px;
  line-height: 22px;
  list-style: none;
}

.pop-bg {
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  background-color: rgba(43, 42, 42, 0.47);
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
