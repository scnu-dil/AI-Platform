# Preparation
You need to install node and git locally. The project is based on vue, vue-router, vue-cli, axios(later) and element-ui. 
```
  "engines": {     （本地自己安装）
    "node": ">= 6.0.0",
    "npm": ">= 3.0.0"
  },
"dependencies": {    （通过下面步骤npm install来安装）
    "axios": "^0.19.0",
    "element-ui": "^2.9.1",
    "vue": "^2.5.2",
    "vue-router": "^3.0.1"
  }
```
## Build Setup

#### 1、新建文件夹AI-Platform,cd,然后通过以下命令安装依赖,自动生成node_modules
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

开发页面的文档说明见Wiki~
