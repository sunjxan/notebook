```
# 升级python2和python3
sudo apt upgrade python2.7
sudo apt upgrade python3.8

# 安装pip2和pip3
sudo apt install python-pip python-dev
sudo pip2 install --upgrade pip
sudo apt install python3-pip python3-dev
sudo pip3 install --upgrade pip

# 设置环境变量，在~/.zshrc追加
export PATH="/home/<user>/.local/bin:$PATH"
# 生效
source ~/.zshrc

# 查看命令位置
command -v python python2 python3
command -v pip pip2 pip3
# 查看软连接
ls -al /usr/bin/python*
# 修改软连接
sudo ln -snf /usr/bin/python2.7 /usr/bin/python
sudo ln -snf /usr/bin/python2.7 /usr/bin/python2
sudo ln -snf /usr/bin/python3.8 /usr/bin/python3

# 更换pip源到国内镜像，修改 ~/.pip/pip.conf (没有就创建一个)
cd ~/.pip
sudo touch pip.conf
sudo vim pip.conf

[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

