```
cd ~
# 下载脚本（https://www.anaconda.com/products/individual）
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
# 安装到/usr/local/anaconda，不运行conda init
sudo bash Anaconda3-2020.02-Linux-x86_64.sh

# 为了不和系统的python和pip冲突，建议不修改环境变量
# 设置环境变量，在~/.zshrc追加
# export PATH="/usr/local/anaconda/bin:$PATH"
# 生效
# source ~/.zshrc

# 查看版本
/usr/local/anaconda/bin/conda -V
# 查看所有环境
/usr/local/anaconda/bin/conda env list

# 更换pip源到国内镜像，修改 ~/.pip/pip.conf
sudo mkdir ~/.pip
sudo vim ~/.pip/pip.conf

[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com

# 设置Anaconda 镜像
sudo vim ~/.condarc
# 清华源（https://mirror.tuna.tsinghua.edu.cn/help/anaconda/）
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

# 清除索引缓存，保证用的是镜像站提供的索引
/usr/local/anaconda/bin/conda clean -i

# 打开Jupyter服务器
/usr/local/anaconda/bin/jupyter notebook
# 获取token
/usr/local/anaconda/bin/jupyter notebook list
```

