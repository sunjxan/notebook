```
# 升级python2和python3
sudo apt upgrade python2.7
sudo apt upgrade python3.8

# 修改软连接
sudo ln -snf /usr/bin/python2.7 /usr/bin/python
sudo ln -snf /usr/bin/python2.7 /usr/bin/python2
sudo ln -snf /usr/bin/python3.8 /usr/bin/python3

# 安装pip2和pip3
sudo apt-get install python-pip python-dev
sudo pip2 install --upgrade pip
sudo apt-get install python3-pip python3-dev
sudo pip3 install --upgrade pip

# 更换pip源到国内镜像，修改 ~/.pip/pip.conf (没有就创建一个)
cd ~/.pip
sudo touch pip.conf
sudo vim pip.conf

[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

