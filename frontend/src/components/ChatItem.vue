<template>
  <div :class="[chatItemObj.type === 'left' ? 'left fadeInLeft' : 'right faseInRight']">
    <img
      class="avater"
      :src="[chatItemObj.type === 'left' ? require('../assets/img/avatar-left.jpg') : require('../assets/img/avatar-right.jpg')]"
      alt
    />
    <p class="msg">{{chatItemObj.msg}}</p>
  </div>
</template>

<script>
export default {
  props: {
    chatItemObj: {
      type: Object,
      required: true,
      default: function() {
        return {};
      }
    }
  }
};
</script>

<style>
.left {
  width: 100%;
  float: left;
  margin-top: 12px;
  margin-left: 14px;
}

.left .avater {
  height: 44px;
  border-radius: 22px;
  vertical-align: top;
}

.left .msg {
  background-color: white;
  padding: 0px 14px;
  border-radius: 8px;
  display: inline-block;
  max-width: 66%;
}

.right {
  width: 100%;
  float: right;
  margin-top: 12px;
  margin-right: 14px;
}

.right .avater {
  height: 44px;
  border-radius: 22px;
  float: right;
}

.right .msg {
  background-color: #05c10a;
  color: white;
  padding: 0px 14px;
  border-radius: 8px;
  float: right;
  margin-right: 4px;
  max-width: 66%;
}
</style>
