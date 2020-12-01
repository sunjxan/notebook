[原网页](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)

|  | Windows文件系统 | Linux文件系统 |
| ----------- | --------------- | ------------- |
| Linux路径   | /mnt/f/         | /home/   |
| Windows路径 | F:\             | `\\wsl$\<子系统名>\home\` |

| 使用file协议 | Windows文件系统 | Linux文件系统 |
| ----------- | --------------- | ------------- |
| Linux路径   | file:///mnt/f/  | file:///home/ |
| Windows路径 | file:///F:\     | `file://wsl$\<子系统名>\home\` |




1. 运行 Windows 10 **版本 18362** 或更高版本：
- 可以通过打开命令提示符并运行 `ver` 命令来检查 Windows 版本

2. BIOS的Advanced -> CPU Configuration里的Virtualization设置为Enabled；

3. 以管理员身份打开 PowerShell 并运行：
```powershell
# 启用“适用于Linux的Windows子系统”
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
# 启用"虚拟机平台"
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
运行后重启电脑；

4. 下载 Linux 内核更新包并更新（https://docs.microsoft.com/zh-cn/windows/wsl/wsl2-kernel ）；

5. 将所有子系统设置为WSL版本2（WSL与WSL2的不同 https://docs.microsoft.com/zh-cn/windows/wsl/compare-versions ）：
```
wsl --set-default-version 2
```

其他命令：
```
# 列出所有子系统及版本
wsl -l -v

# 将子系统设置为WSL版本2
wsl --set-version <子系统名> 2

# 将所有子系统设置为WSL版本2
wsl --set-default-version 2

# 运行脚本
bash -c "<command>"
bash -c <file>

<安装程序>（如Ubuntu1804） run <command>
<安装程序>（如Ubuntu1804） run <file>

wsl -u root <command>
wsl -u root <file>
```

6. 在应用商店中安装Ubuntu 18.04 LTS，安装后创建用户；

7. 移动安装位置，WSL2虚拟磁盘会动态扩增，却不会缩小，要放到有足够存储空间的位置；

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

8. 设置用户：
```
# 以root身份进入wsl
wsl -d <子系统名> -u root
# 进入Linux Shell，当前用户是root，设置密码
passwd
```
9. `Windows Terminal` 是一款命令行工具，在应用商店里搜索并下载安装，或下载安装包安装（<https://github.com/microsoft/terminal/releases>），安装后打开进入Linux Shell，在设置里修改Linux Shell选项，添加：
```
# 默认终端
"defaultProfile": <WSL guid>

# 设置WSL终端
"commandline": "wsl cd ~ && /bin/bash"

# 如果"ctrl+shift+f"不能打开搜索框，则修改关键键为"ctrl+f"
"keybindings":
[
    { "command": "find", "keys": "ctrl+f" }
]
```
10. 更换国内源

查看Ubuntu版本，选择更换源版本：
```bash
cat /etc/lsb-release
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo vim /etc/apt/sources.list
```

替换source.list文件内容

[阿里云源](<https://developer.aliyun.com/mirror/ubuntu>)  20.04

```
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse

```
[清华源](<https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/>)  20.04

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
```

更新

```bash
sudo apt update
```

11. 从官方Ubuntu发行版复制软件包
```bash
# 原主机导出软件列表
dpkg --get-selections > packages-backup.list

# 新主机从软件列表安装
apt install dselect
dselect update
dpkg --set-selections < packages-backup.list
apt-get dselect-upgrade
```

12. 安装aptitude

```bash
sudo apt install aptitude -y
sudo aptitude upgrade -y
```

13. 安装zsh

```bash
# 安装 zsh
sudo aptitude install zsh -y

# 修改Windows Terminal设置文件
"commandline": "wsl cd ~ && /bin/zsh"

# 进入zsh，选择选项2，生成默认.zshrc文件
```

14. 安装oh-my-zsh

从 https://github.com/googlehosts/hosts/blob/master/hosts-files/hosts 中复制解析规则到 `/etc/hosts` 文件中。

下载 `install.sh` 并执行：
```bash
cd ~
wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
bash install.sh

# 安装完成后，退出root
exit
source ~/.zshrc

# 修改用户配置文件所有者
sudo chown -R <用户名>:<用户名> ~
# 修改默认Shell
sudo chsh -s /bin/zsh <用户名>
sudo chsh -s /bin/bash root
```

下载插件：

```bash
cd $ZSH_CUSTOM/plugins
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
git clone https://github.com/zsh-users/zsh-autosuggestions.git
```

修改配置文件：

```bash
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

# 重新打开zsh
exit
```
15. 设置系统语言

```bash
# 查看当前语言
echo $LANG

# 安装语言包
sudo aptitude install language-pack-zh-hans
# 查看安装结果
locale -a

# 开机设置
sudo vim /etc/bash.bashrc
sudo vim /etc/zsh/zshrc
# 追加
export LANG="zh_CN.utf8"
export LANGUAGE="zh_CN:zh"

source /etc/zsh/zshrc
```

16. 设置系统时间

```bash
# 设置时区
tzselect

# 同步时间
sudo aptitude install ntpdate
sudo ntpdate ntp.ntsc.ac.cn
```
17. 安装编译工具gcc、g++、make、cmake
18. 安装Node.js并配置
19. 安装python、pip、JupyterLab并配置
20. 安装Supervisor并配置JupyterLab任务
21. 安装mysql并配置
22. 安装cron
23. 安装docker并配置
24. 设置子系统配置文件`/etc/wsl.conf`（https://devblogs.microsoft.com/commandline/automatically-configuring-wsl/）
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
generateHosts=false
# 子系统是否生成DNS服务器列表文件/etc/resolv.conf
generateResolvConf=true

# 互操作，在wsl中使用Windows程序，如 explorer.exe
[interop]
# 允许在子系统中打开Windows程序
enabled=true
# 允许将Windows环境变量PATH加入到子系统
appendWindowsPath=true
```

25. 添加启动项

不需要root权限：

在`~/.zshrc`文件追加：

```bash
supervisord
```

需要root权限：

在WSL中创建启动加载文件 `/etc/init.sh`：

```bash
#!/bin/sh
service ssh start
```

在Windows中创建启动加载文件 `wsl2.ps1`

```powershell
wsl -u root bash /etc/init.sh
```

控制面板->管理工具->事件查看器，Windows日志->系统，在来源为“ Hyper-V-VmSwith”的事件中，搜索信息为“Port xxxxxxxxxx (Friendly Name: xxxxxxxxxx) successfully created on switch xxxxxxxxxx (Friendly Name: WSL).”的事件，右键该项，选择 将任务附加到该事件。

操作选择 启动程序，程序中填 `PowerShell`，参数填 `-File <wsl2.ps1的绝对地址>` ，后面加上`-WindowStyle Hidden` 可以在启动时隐藏 powershell 窗口，完成。

为了使ps1脚本成功执行，开始菜单->使用管理员身份运行PowerShell，输入 `set-ExecutionPolicy RemoteSigned`，选择 `Y`。

控制面板->管理工具->任务计划程序，任务计划程序库->事件查看器任务，找到刚创建的任务，右键属性，然后勾选下面的复选框：使用最高权限运行。

如果出现MMC管理单元错误，不能自动获取管理员身份，则手动获取：在 `wsl2.ps1` **开始处**检测如果不是管理员身份，则重新以管理员身份打开：

```powershell
$currentWi = [Security.Principal.WindowsIdentity]::GetCurrent()
$currentWp = [Security.Principal.WindowsPrincipal]$currentWi
 
if(-not $currentWp.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
  $boundPara = ($MyInvocation.BoundParameters.Keys | foreach{
     '-{0} {1}' -f  $_ ,$MyInvocation.BoundParameters[$_]} ) -join ' '
  $currentFile = (Resolve-Path  $MyInvocation.InvocationName).Path
  $fullPara = $boundPara + ' ' + $args -join ' '
  Start-Process -FilePath "PowerShell" -Verb runAs -Argumentlist "-File $currentFile $fullPara"
  return
}
```


26. WSL1和Windows共用文件系统、网络，在局域网中可以使用IP进入WSL网络服务。而WSL2有独立的IP，所有子系统使用同一个IP地址，而且WSL2的虚拟网卡网关是动态的，每次重新启动WSL2时IP会改变。

当使用远程 IP 地址连接到应用程序时，它们将被视为来自局域网 (LAN) 的连接。 这意味着你需要确保你的应用程序可以接受 LAN 连接。例如，你可能需要将应用程序绑定到 `0.0.0.0` 而非 `127.0.0.1`。进行这些更改时请注意安全性，因为这将允许来自你的 LAN 的连接。

https://lengthmin.me/posts/wsl2-network-tricks/

https://docs.microsoft.com/zh-cn/windows/wsl/compare-versions#accessing-network-applications

Windows可以访问WSL的程序，但WSL访问Windows的程序要通过防火墙，设置程序专用网络、公用网络都允许访问后即可访问。

```bash
# Windows IP
cat /etc/resolv.conf | grep 'nameserver' | cut -f 2 -d ' '
# WSL2 IP
ip addr show eth0 | grep 'inet ' | cut -f 6 -d ' ' | cut -f 1 -d '/'
```

修改WSL2 hosts文件添加域名映射，在 `/etc/init.sh`文件中添加：

```bash
host_path="/etc/hosts"
win_key="# WSL2 Win host"
win_hostname="windows"
win_ip=$(cat /etc/resolv.conf | grep 'nameserver' | cut -f 2 -d ' ')

sed -i "/${win_key}/d" ${host_path}
sed -i "\$a\\${win_ip}          ${win_hostname}                  ${win_key}" ${host_path}

wsl_key="# WSL2 host"
wsl_hostname="wsl"
wsl_ip=$(ip addr show eth0 | grep 'inet ' | cut -f 6 -d ' ' | cut -f 1 -d '/')

sed -i "/${wsl_key}/d" ${host_path}
sed -i "\$a\\${wsl_ip}          ${wsl_hostname}                  ${wsl_key}" ${host_path}
```

修改Windows hosts文件添加域名映射，在 `wsl2.ps1`文件中添加：

```powershell
$host_path = "$env:windir\System32\drivers\etc\hosts"
$wsl_key = "# WSL2 host"
$wsl_hostname = "master"
$wsl_ip = bash -c "ip addr show eth0 | grep 'inet ' | cut -f 6 -d ' ' | cut -f 1 -d '/'"

((Get-Content -Path $host_path | Select-String -Pattern $wsl_key -NotMatch | Out-String).Trim() + "`n$wsl_ip`t`t$wsl_hostname`t`t`t$wsl_key").Trim() | Out-File -FilePath $host_path -encoding ascii

$win_key = "# WSL2 Win host"
$win_hostname = "windows"
$win_ip = bash -c "cat /etc/resolv.conf | grep 'nameserver' | cut -f 2 -d ' '"

((Get-Content -Path $host_path | Select-String -Pattern $win_key -NotMatch | Out-String).Trim() + "`n$win_ip`t`t$win_hostname`t`t`t$win_key").Trim() | Out-File -FilePath $host_path -encoding ascii
```

如果要在局域网中访问WSL2里的服务，使用端口映射，在 `wsl2.ps1`文件中添加：

```powershell
$ports = @(80, 443, 8080, 9001, 8888)

$addr = '0.0.0.0'
$ports_a = $ports -join ","

iex "Remove-NetFireWallRule -DisplayName 'WSL2 Firewall Unlock'" | Out-Null

iex "New-NetFireWallRule -DisplayName 'WSL2 Firewall Unlock' -Direction Outbound -LocalPort $ports_a -Action Allow -Protocol TCP"  | Out-Null
iex "New-NetFireWallRule -DisplayName 'WSL2 Firewall Unlock' -Direction Inbound -LocalPort $ports_a -Action Allow -Protocol TCP"  | Out-Null

for ($i = 0; $i -lt $ports.length; $i++) {
  $port = $ports[$i]
  iex "netsh interface portproxy delete v4tov4 listenport=$port listenaddress=$addr"  | Out-Null
  iex "netsh interface portproxy add v4tov4 listenport=$port listenaddress=$addr connectport=$port connectaddress=$wsl_ip"  | Out-Null
}

ipconfig /flushdns | Out-Null
```

27. 在Windows安装X server并配置。设置开启WSL2时，启动X server，在 `wsl2.ps1` 文件中添加：

```powershell
$str = netstat -ano | findstr 0.0.0.0:6000
$target = $str.Split()[-1]
taskkill /pid $target -f

C:\Users\<user>\Desktop\config.xlaunch
```

安装 `Ubuntu` 自带的编辑器 `gedit` 用于编辑文本，但不能使用 `Windows` 的中文输入法输入中文。

安装字体设置 `fontconfig` ，使用命令 `fc-list :lang=zh` 查看系统支持的中文字体，如果没有，需要先安装：

```
# 复制字体
sudo mkdir /usr/share/fonts/opentype
sudo mkdir /usr/share/fonts/opentype/msyh
sudo cp /mnt/c/Windows/Fonts/msyh* /usr/share/fonts/opentype/msyh

# 生成字体缓存
fc-cache -fv

# 查看字体是否已支持
fc-list :lang=zh
```

