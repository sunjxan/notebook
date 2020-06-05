1.  安装PyCharm专业版；
2. 打开Windows文件系统下的项目目录；
3. File->Settings->Tools->Terminal，修改Shell path为wsl.exe；
4. 配置WSL解释器：File->Settings->Project->Project Interpreter，添加解释器，在WSL中选择wsl发行版和Python解释器路径；
5. 配置远程解释器：在WSL中创建一个用户所有的目录作为项目目录；File->Settings->Project->Project Interpreter，添加解释器，选择SSH Interpreter，连接<该用户>@localhost:22，选择ssh密钥文件（默认位置在Windows用户主目录下的.ssh目录），选择Python解释器路径，设置项目同步目录，勾选自动同步（手动同步在Tools->Deployment->Upload to）；
6. 新建或打开一个项目，Run->Edit Configurations，新建一个Python运行配置，修改名字，选择项目目录、入口文件和解释器；
7. 由于无法配置WSL版anaconda，所以使用Jupyter需要手动开启服务器
```
# 打开Jupyter服务器
jupyter notebook
# 获取token
jupyter notebook list
```

File->Settings->Build->Jupyter->Jupyter Servers，选择Configured Server，输入刚刚获取的带token的URL；

8. File->Settings->Languages->Node.js，添加解释器，在WSL中选择wsl发行版和Node解释器路径

