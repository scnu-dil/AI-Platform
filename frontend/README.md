# AI-Platform

> A Vue.js project

# Preparation
You need to install node and git locally. The project is based on vue, vue-router, vue-cli, axios(later) and element-ui. 
```
  "engines": {
    "node": ">= 6.0.0",
    "npm": ">= 3.0.0"
  },
```
## Build Setup

#### 1、新建文件夹AI-Platform,cd,然后安装依赖,自动生成node_modules
``` bash
# install dependencies
npm install
```
#### 或者可通过安装TB镜像提升下载速度
``` 
# install dependencies
npm install cnpm -g --registry=https://registry.npm.taobao.org
cnpm install
```
#### 2、启动项目at localhost:8080（端口号根据自己的进行修改）
``` 
npm run dev
```

## Update log

#### 20190606第一次更新：
目前写好了主界面以及自然语言处理的极简页面。（字体大小及位置、图片、内容都会继续添加和修改）
#### 20190609 第二次更新：
主要将SpaceNLP界面进行调整优化，添加了导航栏（顶栏）以及修改了背景和布局；将Home界面的链接调整修改了样式。
#### 20190610 第三次更新：
增加了前后端交互部分，采用的是axios方式的ajax请求。


