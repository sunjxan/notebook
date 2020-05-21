```
cd /usr/local
# 下载脚本（https://www.anaconda.com/products/individual）
sudo wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
# 安装
sudo bash Anaconda3-2020.02-Linux-x86_64.sh
sudo mv anaconda3 anaconda

# 设置环境变量，在~/.zshrc追加
export PATH="/usr/local/anaconda/bin:$PATH"
# 生效
source ~/.zshrc

#查看版本
conda -V

# 更换pip源到国内镜像，修改 ~/.pip/pip.conf (没有就创建一个)
cd ~/.pip
sudo touch pip.conf
sudo vim pip.conf

[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com

# 设置Anaconda 镜像
cd ~
sudo touch .condarc
sudo vim .condarc

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
conda clean -i

# 打开Jupyter服务器
jupyter notebook
# 获取token
jupyter notebook list
```

