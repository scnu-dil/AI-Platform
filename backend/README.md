# AI-Platform 后台部分
> 更新于 manager.py

# 环境依赖
> 后台模块功能的展示需要依赖前端体现，前端相关操作请移步frontend

# 源码
>down下后，按以下命令执行

```
运行句法分析所需环境（不运行可以不理）
Python3.6及以上
Jdk1.8及以上
下载斯坦福StanfordNLP工具包
stanford-corenlp-full-2018-10-05 将该文件放到与manager.py文件同一个目录中
stanford-chinese-corenlp-2018-10-05-models.jar将该文件放进上一个文件目录中

//进入down后的AI-Platform/backend目录
~$ virtualenv --no-site-packages venv
//安装前期已有的依赖包
~$ source venv/bin/activate
~$ pip install -r ../requirement.txt
//直接运行manager.py
（venv）python manager.py

//开启另一终端，启动前端
具体操作移步至frontend阅读README
```

>开发新功能模块的文档说明请移步至wiki~
