<template>
  <div id="app">
    <home></home>
    <router-view/>
  </div>
</template>

<script>
import Home from "./components/Home";

export default [
  {
    path: "/",
    redirect: "/home",
    component: Home
  }
];
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
