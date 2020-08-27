```
# 更换pip源到国内镜像，修改 ~/.pip/pip.conf
mkdir ~/.pip
vim ~/.pip/pip.conf
# 阿里云源
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com

# 设置Anaconda 镜像
vim ~/.condarc
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

cd ~
# 下载脚本（https://www.anaconda.com/products/individual）
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
# 安装
sudo bash Anaconda3-2020.07-Linux-x86_64.sh
# 安装到/usr/local/anaconda，运行conda init
# 如果conda init修改~/.bashrc
cat ~/.bashrc >> ~/.zshrc
# 重新打开该shell

# 因为在Anaconda中很多操作需要文件所有者权限，所以需要更改Anaconda目录所有者
sudo chown -R <user>:<user> /usr/local/anaconda

# 查看版本
conda -V
# 查看安装信息
conda info
# 更新Anaconda
conda update conda anaconda -y

# 查看python命令
command -v python
command -v python3

# 退出anaconda环境
conda deactivate

# 设置默认不进入base环境
conda config --set auto_activate_base false
```

```
# 查看所有环境
conda env list
# 创建环境
conda create -n python37  python=3.7
# 切换环境
conda activate python37
# 切换到base环境
conda activate
# 退出anaconda环境
conda deactivate
# 卸载环境
conda remove --name python37 --all
# 清除索引缓存，保证用的是镜像站提供的索引
conda clean -i

# 查看所有安装模块
conda list
# 安装模块
conda install <模块名>
# 更新模块
conda update <模块名>
# 卸载模块
conda remove <模块名>
# 导出安装模块信息
conda env export > environment.yaml
# 从yaml文件创建环境
conda env create -f environment.yaml

# 打开Jupyter服务器
jupyter notebook --ip=0.0.0.0 --no-browser --allow-root >/dev/null 2>&1 &
# 获取token
jupyter notebook list
```

