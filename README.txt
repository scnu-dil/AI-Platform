环境搭建:
	1、安装显卡驱动和cuda
  		https://blog.csdn.net/qq_41493990/article/details/82183035

	2、安装python3.7以上
		SSL解决方案
		https://blog.csdn.net/chief_victo/article/details/80425431

	3、pip install virtualenv

	4、安装cmake
		https://blog.csdn.net/qq_38378235/article/details/80839693

	5、 进入AI-Platform/backend目录
		~$ virtualenv --no-site-packages venv
		//安装前期已有的依赖包
		~$ source venv/bin/activate
		~ $ pip install - r.. / requirement.txt
		//直接运行manager.py
		python manager.py

	6、安装node  npm
		https://www.cnblogs.com/betx/p/10347797.html

	7、 进入AI-Platform/frontend目录
		npm install cnpm -g --registry=https://registry.npm.taobao.org
		cnpm install
		npm run dev

人面识别模块:
	1、首先测试图要放三张，点击上传，上传到服务器，图片左上角出现绿色的勾，代表上传成功
	2、检测图放一张，点击上传，上传到服务器，图片左上角出现绿色的勾，代表上传成功
	3、上面两组图片都上传成功后，才可以点击开始检测，点击后过一小会，检测结果图会自动出现在最下方，等待检测时间长短取决于GPU性能
