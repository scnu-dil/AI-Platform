<template>
  <div id="home">
    <el-container>
      <el-main>
        <!-- 第一列栅格布局 -->
        <el-row>
          <el-carousel :interval="4000" type="card" height="300px">
            <el-carousel-item v-for="item in 6" :key="item">
              <h3 class="medium">{{ item }}</h3>
            </el-carousel-item>
          </el-carousel>
          <!--第二列-->
          <el-col :span="24" class="col1"></el-col>
          <!--<el-col :span="12" class="col2"></el-col>-->
        </el-row>
        <el-row>
          <el-col :span="12" class="col3" height="300px"></el-col>
          <el-col :span="12" class="col4" height="300px"></el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
// import HeaderTop from "@/components/HeaderTop";
// import AsideMain from "@/components/AsideMain";
// import SpaceNLP from "./components/SpaceNLP.vue";

export default {
  name: 'App',
  components: {
    // headertop: HeaderTop,
    // asidemain: AsideMain
    // spacenlp: SpaceNLP
  }
}
</script>

<!--
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
}
</style>
-->
<style>
.col1 {
  background-color: #e0e7ee;
}
.col2 {
  background-color: rgb(189, 202, 202);
}
.col3 {
  background-color: #d3dce6;
}
.col4 {
  background-color: #99a9bf;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 570px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
