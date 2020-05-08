```
# 下载脚本
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
# 安装
sudo sh Anaconda3-2020.02-Linux-x86_64.sh

# 设置环境变量，在~/.zshrc追加
__conda_setup="$('/home/sunjxan/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/sunjxan/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/sunjxan/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/sunjxan/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup

# 生效
source .zshrc

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
```

