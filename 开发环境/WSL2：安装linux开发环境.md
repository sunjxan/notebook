1. 运行 Windows 10 **版本 18917** 或更高版本：
- 加入 [Windows 预览体验计划](https://insider.windows.com/en-us/)并选择“慢速”环形；
- 可以通过打开命令提示符并运行 `ver` 命令来检查 Windows 版本。

2. 在“Windows功能”中打开“适用于Linux的Windows子系统”和“虚拟机平台”；

3. 在应用商店中安装Ubuntu，创建用户；

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

# 以管理员身份打开PowerShell，重新设置wsl默认用户
ubuntu1804.exe config --default-user <username>
```
6. `Windows Terminal` 是一款命令行工具，在应用商店里搜索并下载安装，进入Linux Shell；

![1588836531014](WSL2：安装linux开发环境.assets/1.png)

7. 更换国内源

备份原文件：
```
sudo cp /etc/apt/sources.list /etc/apt/sourses.list.bak
```

将source.list文件内容替换成下面的：

```
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```

更新：

```
sudo apt update
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

下载[install.sh](https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)执行：
```
sudo sh install.sh
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

