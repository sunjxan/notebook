###  Windows安装

[原网页](https://docs.docker.com/docker-for-windows/wsl/)

1. 升级系统至64 位版本的 Windows 10 Pro；
2. 在BIOS的Advanced->CPU Configuration里的Virtualization设置为Enabled；
3. 打开Wndows的【启用或关闭windows功能】，启用“Hyper-V”；
4. 下载Docker Desktop并安装（https://www.docker.com/products/docker-desktop），勾选"Use the WSL 2 based engine"；
5. 移动安装位置，以管理员身份运行CMD：
```
# 进入用户主目录C:\Users\<用户名>

# 复制软件安装目录和虚拟磁盘目录，虚拟磁盘会动态扩增，却不会缩小，要放到有足够存储空间的位置
xcopy /E /H /K /X /Y /C "C:\Program Files\Docker" "D:\Docker"
xcopy /E /H /K /X /Y /C ".\AppData\Local\Docker\wsl" "G:\WSL_Docker"

# 关闭后台进程Docker.Service后删除原目录

# 创建符号链接
mklink /d  "C:\Program Files\Docker" "D:\Docker"
mklink /d ".\AppData\Local\Docker\wsl" "G:\WSL_Docker"
```
6. 打开Docker桌面客户端，并启动Docker服务；
7. 登录https://cr.console.aliyun.com/注册账号，得到一个专属的镜像加速地址；
8. Settings -> General，勾选"Expose daemon on tcp://localhost:2375 without TLS"；
9. Settings -> Resources -> WSL Integration，选择允许访问Docker的WSL2子系统；
11. Settings -> Docker Engine，编辑"registry-mirrors": ["<镜像加速地址>“]；
12. Settings -> Command Line，勾选“Enable experimental features”；
12. 保存设置，等待Docker重启；
13. 在WSL2中查看版本：
```
docker version
```


### Ubuntu安装

[原网页](<https://docs.docker.com/engine/install/ubuntu/>)

#### 查看Linux内核版本

```
uname -r
# 首先必须保证是64位Linux系统，其次内核版本必须大于3.10
```

#### 卸载旧版本

```
sudo apt remove --purge docker docker-engine docker.io containerd runc docker-ce docker-ce-cli containerd.io
sudo rm -rf /var/lib/docker/
```

#### 1）仓库安装

```
# 设置apt使用https
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

# 添加GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 添加仓库
sudo add-apt-repository  "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# 安装
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

# 查看版本
sudo docker version

# 更换镜像地址，登录https://cr.console.aliyun.com/注册账号，得到一个专属的镜像加速地址
sudo mkdir /etc/docker
sudo vim /etc/docker/daemon.json
{
  "registry-mirrors": ["https://prj2n5cu.mirror.aliyuncs.com"]
}

# 启动
sudo service docker start

# 查看信息，包含新镜像地址
sudo docker info

# 测试
docker run hello-world
```
#### 2）安装包安装（无法升级）

```
# 下载安装包（https://download.docker.com/linux/ubuntu/dists/）
# 以下两个命令都可以查看Ubuntu版本代号，Ubuntu18.04代号是Bionic Beaver
cat /etc/lsb-release
lsb_release -cs
sudo wget https://download.docker.com/linux/ubuntu/dists/bionic/pool/stable/amd64/docker-ce_19.03.9~3-0~ubuntu-bionic_amd64.deb
# 安装
sudo dpkg -i docker-ce_19.03.9~3-0~ubuntu-bionic_amd64.deb
```

#### 3）脚本安装（不适合生产环境）

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```