```
# 更换pip源到国内镜像，修改 ~/.pip/pip.conf
mkdir ~/.pip
vim ~/.pip/pip.conf
# 阿里云源
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com

# 从零安装python2
sudo apt install python
# 查看版本
python -V
# 升级python2
sudo apt upgrade python2.7

# 安装pip2
sudo apt install python-pip python-dev
pip2 install --upgrade pip

# 从零安装python3
sudo apt install python3
# 查看版本
python3 -V
# 升级python3
sudo apt upgrade python3.8

# 安装pip3
sudo apt install python3-pip python3-dev
pip3 install --upgrade pip

# 查看个版本
where python
where python3
# 查看优先使用的版本
command -v python python2 python3 pip pip2 pip3
ls -al /usr/bin/python* /usr/bin/pip* /usr/local/bin/pip*
# 不建议修改python软连接

# 生成requirements.txt文件
pip3 freeze > requirements.txt
# 安装requirements.txt依赖
pip3 install -r requirements.txt

# 设置环境变量，在~/.zshrc追加
export PYTHONPATH=.:..:$PYTHONPATH
export PATH=~/.local/bin:$PATH
# 生效
source ~/.zshrc
```

```
pip3 install jupyter

# 打开Jupyter服务器
jupyter notebook --ip=0.0.0.0 --allow-root >/dev/null 2>&1 &
# 获取token
jupyter notebook list
```

```
pip3 install jupyterlab

# 打开Jupyter服务器
jupyter-lab --ip=0.0.0.0 --allow-root >/dev/null 2>&1 &
# 获取token
jupyter notebook list
```

