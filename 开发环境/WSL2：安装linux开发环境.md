1. 运行 Windows 10 **版本 18917** 或更高版本：
- 加入 [Windows 预览体验计划](https://insider.windows.com/en-us/)并选择“慢速”环形；
- 可以通过打开命令提示符并运行 `ver` 命令来检查 Windows 版本。

2. 在“Windows功能”中打开“适用于Linux的Windows子系统”和“虚拟机平台”；

3. 在应用商店中安装Ubuntu，或下载安装包安装（<https://docs.microsoft.com/en-us/windows/wsl/install-manual>），安装后创建用户；

4. 安装升级WSL2，在 `PowerShell` 中使用下面命令：
```
# 查看使用的WSL版本
wsl -l -v

# 将 <Distro> 换成你想要设置的发行版
wsl --set-version <Distro> 2

# 将默认的WSL发行版设置成 WSL2
wsl --set-default-version 2

# 验证使用的WSL版本
wsl -l -v
```
5. 设置root密码：
```
# 以管理员身份打开PowerShell，设置wsl默认用户为root
ubuntu1804.exe config --default-user root
# 进入Linux Shell，当前用户是root，设置密码
passwd

# 或者直接以root身份进入wsl
wsl -u root
```
6. `Windows Terminal` 是一款命令行工具，在应用商店里搜索并下载安装，或下载安装包安装（<https://github.com/microsoft/terminal/releases>），安装后进入Linux Shell；

![1588836531014](WSL2：安装linux开发环境.assets/1.png)

7. 更换国内源

备份原文件：
```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
```

替换source.list文件内容

清华源：

```
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
```

阿里源：

```
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```

更新

```
sudo apt update
```

升级

```
sudo apt upgrade
```

8. 安装zsh

```
# 安装 zsh
sudo apt install zsh

# 修改默认的 Shell 为 zsh
sudo chsh -s /bin/zsh root
sudo chsh -s /bin/zsh <username>
```

9. 安装oh-my-zsh

下载[install.sh](WSL2：安装linux开发环境.assets/install.sh)（https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh）执行：
```
sudo bash install.sh
```

下载插件：

```
cd $ZSH_CUSTOM/plugins
sudo git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
sudo git clone https://github.com/zsh-users/zsh-autosuggestions.git
```

修改配置文件：

```
cd ~
sudo vim .zshrc

# 修改主题
ZSH_THEME="ys"

# 在 plugins 一列中添加如下
plugins=(
         git
         zsh-syntax-highlighting
         zsh-autosuggestions
         )
         
# 在文件最后添加
source $ZSH_CUSTOM/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $ZSH_CUSTOM/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

source .zshrc
```

10. 路径问题

|  | Windows文件系统 | Linux文件系统 |
| ----------- | --------------- | ------------- |
| Linux路径   | /mnt/f/         | /home/user/   |
| Windows路径 | F:\             | `\\wsl$\Ubuntu-18.04\home\user\` |

使用file协议

|  | Windows文件系统 | Linux文件系统 |
| ----------- | --------------- | ------------- |
| Linux路径   | file:///mnt/f/  | file:///home/user/ |
| Windows路径 | file:///F:\     | `file://wsl$\Ubuntu-18.04\home\user\` |

Linux程序访问Windows文件系统和Linux文件系统没有区别，Windows程序访问Linux文件系统可能有路径错误，所以把项目文件放在Windows文件系统。

11. WSL1和Windows共用文件系统、网络，在局域网中可以使用IP进入WSL网络服务。而WSL2有独立的IP，而且WSL2的虚拟网卡网关是动态的，每次重新进入时IP会改变：
```
# 关闭wsl
wsl --shutdown
```

而且WSL2的IP在局域网中无法访问，只能在Windows中通过WSL2的IP或者localhost(127.0.0.1)访问。

如果要在局域网中访问WSL2里的服务，可以在CMD（以管理员身份运行）使用端口映射：

```
# 添加映射
netsh interface portproxy add v4tov4 listenport=<WSL2服务的端口> connectaddress=<WSL2的IP>
# 查看映射
netsh interface portproxy show v4tov4
# 删除映射
netsh interface portproxy delete v4tov4 listenport=<WSL2服务的端口>
```

然后添加Windows防火墙规则并启用：

> 1）防火墙和网络保护 -> 高级设置

> 2）入站规则 -> 新建规则

> 3）端口 -> 协议类型：TCP，特定本地端口：<WSL2服务的端口>

> 4）设置名称：WSL2，完成

> 5）规则已经自动启用