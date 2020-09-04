[原网页](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

1. 运行 Windows 10 **版本 19041** 或更高版本：
- 加入 [Windows 预览体验计划](<https://insider.windows.com/zh-cn/>)并选择慢速更新；
- 可以通过打开命令提示符并运行 `ver` 命令来检查 Windows 版本。

2. OS的Advanced->CPU Configuration里的Virtualization设置为Enabled；

3. 以管理员身份打开 PowerShell 并运行：
```
# 启用“适用于Linux的Windows子系统”
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
# 启用"虚拟机平台"
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
运行后重启电脑；

4. 在应用商店中安装Ubuntu，或下载安装包安装（<https://docs.microsoft.com/en-us/windows/wsl/install-manual>），安装后创建用户；

5. 安装升级WSL2（WSL与WSL2的不同 https://docs.microsoft.com/zh-cn/windows/wsl/compare-versions），在 `PowerShell` 中使用下面命令：
```
# 列出所有子系统及版本
wsl -l -v

# 将子系统设置为WSL版本2
wsl --set-version <子系统名> 2

# 将所有子系统设置为WSL版本2
wsl --set-default-version 2
```
6. 移动安装位置，WSL2虚拟磁盘会动态扩增，却不会缩小，要放到有足够存储空间的位置；

```
# 关闭子系统
wsl -t <子系统名>
# 或关闭所有子系统（所有子系统使用同一个IP地址，每次shutdown后重启会变化）
wsl --shutdown

# 导出子系统
wsl --export <子系统名> wsl.tar
# 删除子系统
wsl --unregister <子系统名>
# 导入子系统（不要修改子系统名）
wsl --import <子系统名> G:\WSL_<子系统名> wsl.tar
# 设置默认子系统
wsl -s <子系统名>

# 删除文件
del wsl.tar

# 使用安装程序（如Ubuntu1804）设置默认用户
<安装程序> config --default-user <用户名>
```

7. 设置用户：
```
# 以root身份进入wsl
wsl -d <子系统名> -u root
# 进入Linux Shell，当前用户是root，设置密码
passwd
```
8. `Windows Terminal` 是一款命令行工具，在应用商店里搜索并下载安装，或下载安装包安装（<https://github.com/microsoft/terminal/releases>），安装后打开进入Linux Shell，在设置里修改Linux Shell选项，添加：
```
# 默认终端
"defaultProfile": <WSL guid>

# 设置WSL终端
"commandline": "wsl cd ~ && /bin/bash"
```
9. 更换国内源

备份原文件：
```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo vim /etc/apt/sources.list
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

更新升级

```
sudo apt update && sudo apt upgrade -y
```

10. 从官方Ubuntu发行版复制软件包
```
# 原主机导出软件列表
dpkg --get-selections > packages-backup.list

# 新主机从软件列表安装
apt install dselect
dselect update
dpkg --set-selections < packages-backup.list
apt-get dselect-upgrade
```

11. 安装aptitude

```
sudo apt install aptitude
```

12. 安装zsh

```
# 安装 zsh
sudo aptitude install zsh

# 修改Windows Terminal设置文件
"commandline": "wsl cd ~ && /bin/zsh"
```

13. 安装oh-my-zsh

下载 [install.sh](WSL.assets/install.sh) 并执行（https://github.com/ohmyzsh/ohmyzsh/tree/master/tools）：
```
sudo bash install.sh
# 修改用户配置文件所有者
sudo chown -R <用户名>:<用户名> /home/<用户名>
# 切换用户
su -s /bin/zsh <用户名>

# 修改默认Shell
sudo chsh -s /bin/zsh <用户名>
sudo chsh -s /bin/bash root
```

下载插件：

```
cd $ZSH_CUSTOM/plugins
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
git clone https://github.com/zsh-users/zsh-autosuggestions.git
```

修改配置文件：

```
vim ~/.zshrc

# 修改主题
ZSH_THEME="ys"

# 在 plugins 一列中添加如下
plugins=(
         z
         git
         docker
         zsh-syntax-highlighting
         zsh-autosuggestions
         )
         
# 在文件最后添加
source $ZSH_CUSTOM/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $ZSH_CUSTOM/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

source ~/.zshrc
```

14. 安装python、pip并配置
15. 安装mysql并配置
16. 安装docker并配置
17. 路径问题

|  | Windows文件系统 | Linux文件系统 |
| ----------- | --------------- | ------------- |
| Linux路径   | /mnt/f/         | /home/   |
| Windows路径 | F:\             | `\\wsl$\<子系统名>\home\` |

使用file协议

|  | Windows文件系统 | Linux文件系统 |
| ----------- | --------------- | ------------- |
| Linux路径   | file:///mnt/f/  | file:///home/ |
| Windows路径 | file:///F:\     | `file://wsl$\<子系统名>\home\` |

Linux程序访问Windows文件系统和Linux文件系统没有区别，Windows程序访问Linux文件系统可能有路径错误，所以把项目文件放在Windows文件系统。

18. 添加开机启动项
```
sudo vim /etc/init.wsl
# 输入启动项

#!/bin/sh
/etc/init.d/ssh start

# 给予脚本执行权限
sudo chmod +x /etc/init.wsl

# Windows下Win+R输入shell:startup进入目录
# 创建文件linux-start.vbs，输入内容
Set ws = WScript.CreateObject("WScript.Shell")        
ws.run "wsl -u root /etc/init.wsl"
```

19. WSL1和Windows共用文件系统、网络，在局域网中可以使用IP进入WSL网络服务。而WSL2有独立的IP，所有子系统使用同一个IP地址，而且WSL2的虚拟网卡网关是动态的，每次重新启动WSL2时IP会改变（https://docs.microsoft.com/zh-cn/windows/wsl/compare-versions#accessing-network-applications）：
```
# 查看ip
export WINIP=$(cat /etc/resolv.conf | grep 'nameserver' | cut -f 2 -d ' ') 
export WSLIP=$(ip addr show eth0 | grep 'inet ' | cut -f 6 -d ' ' | cut -f 1 -d '/')
```

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

20. 子系统配置文件`/etc/wsl.conf`（https://devblogs.microsoft.com/commandline/automatically-configuring-wsl/）
```
# 自动挂载
[automount]
# 自动挂载Windows磁盘为DrvFs文件系统
enabled=true
# 挂载其他文件系统
mountFsTab=true
# 挂载根目录
root="/mnt/"
# 设置Windows磁盘文件所有者和权限，如"metadata,uid=1000,gid=1000,umask=22,fmask=111"，具体配置在文件/etc/fstab
options=""

# 网络
[network]
# 子系统是否生成静态域名映射文件/etc/hosts
generateHosts=true
# 子系统是否生成DNS服务器列表文件/etc/resolv.conf
generateResolvConf=true

# 互操作
[interop]
# 允许在子系统中打开Windows程序
enabled=true
# 允许将Windows环境变量PATH加入到子系统
appendWindowsPath=true
```