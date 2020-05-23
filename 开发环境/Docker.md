###  Windows安装
1. 升级系统至64 位版本的 Windows 10 Pro；
2. 在BIOS的Advanced->CPU Configuration里的Virtualization设置为Enabled；
3. 打开Wndows的【启用或关闭windows功能】，启用“Hyper-V”；
4. 下载[Docker Desktop](https://www.docker.com/products/docker-desktop)并安装；
5. 打开Docker Desktop设置，勾选“Expose daemon on tcp://localhost:2375 without TLS”、“Enable the experimental WSL 2 based engine”，“Resources  WSL Integration”里选择安装的WSL2发行版；
6. 在WSL2里查看docker版本信息
```
docker version
```

7. 登录https://cr.console.aliyun.com/注册账号，得到一个专属的镜像加速地址；

8. 打开Docker Desktop设置，“Docker Engine”里编辑"registry-mirrors": ["<镜像加速地址>“]

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
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# 查看版本
docker version

# 启动
sudo service docker start
# 更换镜像地址，登录https://cr.console.aliyun.com/注册账号，得到一个专属的镜像加速地址
sudo vim /etc/docker/daemon.json
{
 "registry-mirrors": ["<镜像加速地址>"]
}
# 重启
sudo service docker restart

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