1.  安装PyCharm专业版；

2.  安装rsync
```
sudo apt install rsync
```

3. File->Settings->Project->Project Interpreter，添加解释器，在WSL中选择wsl发行版和Python解释器路径；
4. 新建或打开一个项目，Run->Edit Configurations，新建一个Python运行配置，修改名字，选择项目目录、入口文件和解释器；
5. File->Settings->Tools->Terminal，修改Shell path为wsl.exe；

6. 由于无法配置WSL版anaconda，所以使用Jupyter需要手动开启服务器
```
# 打开Jupyter服务器
jupyter notebook
# 获取token
jupyter notebook list
```

File->Settings->Build->Jupyter->Jupyter Servers，选择Configured Server，输入刚刚获取的带token的URL；

7. File->Settings->Languages->Node.js，添加解释器，在WSL中选择wsl发行版和Node解释器路径

