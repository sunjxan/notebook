[原网页](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)
1. 运行 Windows 10 **版本 18917** 或更高版本：
- 加入 [Windows 预览体验计划](<https://insider.windows.com/zh-cn/>)并选择慢速更新；
- 可以通过打开命令提示符并运行 `ver` 命令来检查 Windows 版本。

2. 打开Wndows的【启用或关闭windows功能】，启用“适用于Linux的Windows子系统”和“虚拟机平台”；

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
5. 设置root密码的方法：
```
# 以管理员身份打开PowerShell，设置wsl默认用户为root
Ubuntu1804 config --default-user root
# 进入Linux Shell，当前用户是root，设置密码
passwd

# 或者直接以root身份进入wsl
wsl -u root
```
6. `Windows Terminal` 是一款命令行工具，在应用商店里搜索并下载安装，或下载安装包安装（<https://github.com/microsoft/terminal/releases>），安装后打开进入Linux Shell，在设置里修改Linux Shell选项，添加：
```
"commandline": "wsl.exe ~"
```
7. 更换国内源

备份原文件：
```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
```

替换source.list文件内容

[阿里云源](<https://developer.aliyun.com/mirror/ubuntu>)  18.04

```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```
[清华源](<https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/>)  18.04

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
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

https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh 下载 [install.sh](WSL2：安装Linux开发环境.assets/install.sh) 并执行：
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

11. 添加开机启动项
```
sudo vim /etc/init.wsl
# 输入启动项
#!/bin/sh
/etc/init.d/ssh start
/etc/init.d/mysql start

# 给予脚本执行权限
sudo chmod +x /etc/init.wsl

# Windows下Win+R输入shell:startup进入目录
# 创建文件linux-start.vbs，输入内容
Set ws = WScript.CreateObject("WScript.Shell")        
ws.run "wsl -d Ubuntu-18.04 -u root /etc/init.wsl"
```

12. WSL1和Windows共用文件系统、网络，在局域网中可以使用IP进入WSL网络服务。而WSL2有独立的IP，而且WSL2的虚拟网卡网关是动态的，每次重新进入时IP会改变：
```
# 关闭wsl
wsl --shutdown
# 查看ip
export WINIP=$(cat /etc/resolv.conf | grep 'nameserver' | cut -f 2 -d ' ') 
export WSLIP=$(ip addr show eth0 | grep 'inet ' | cut -f 6 -d ' ' | cut -f 1 -d '/')
```

而且WSL2的IP在局域网中无法访问，只能在Windows中通过WSL2的IP访问。Windows和WSL2各自有自身的localhost(127.0.0.1)，但是使用Windows的localhost自动解析到WSL2的IP。

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

