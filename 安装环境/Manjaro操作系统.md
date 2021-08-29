### 安装前的准备
下载 [Manjaro ISO 镜像](https://manjaro.org/download/)。

Windows用户使用 [Rufus](http://rufus.ie/) 制作 Manjaro 启动U盘，注意：需要使用DD模式。

Linux用户，可以使用DD命令进行制作。

```
# 查看U盘的dev路径
sudo fdisk -l

# 如果U盘还在挂载状态，卸载它
umount /dev/sdX

# 用dd命令将系统iso镜像文件直接写入U盘
sudo dd if=/path/to/manjaro.iso of=/dev/sdX bs=4M status=progress && sync
```

将启动盘插入电脑，开机时选择U盘启动，进入 Manjaro 安装界面。

### 安装

1. 连接网络；
2. 选择语言、时区；
3. 选择键盘布局为English(US) - Default；
4. 手动分区

- EFI系统分区（EFI system partition，ESP）300MB，FAT32文件系统，挂载到/boot/efi，设置标记为boot，建议设为第一块磁盘的第一个分区；

- 根分区 – ext4，20G，所有的目录都挂在这个目录下面；


- /usr –ext4，40G，用于存放程序以及数据的地方，涵盖了二进制文件，各种文档，各种头文件，还有各种库文件；
- /opt –ext4，10G， 这个目录往往被用于安装 Gnome 或 KDE 等大型软件，以免把大量文件塞进 /usr 目录树；
- /srv – ext4，5G，用于存储本机或本服务器提供服务的数据，主要用于配置服务器；
- /var – ext4，30G，包含缓存、一些临时文件以及日志文件；
- /home –ext4，硬盘剩余的可用空间；

- 交换 (Swap) 分区  linuxswap文件系统

一般来说，推荐采用两倍于物理内存的交换空间，然而这几乎没有必要。如果磁盘空间有限，可以创建不超过 2GB 的交换空间，并注意它的使用情况。

如果您希望使用 Linux 的休眠功能 (挂起到磁盘)，它会在关机前将内存内容写入到交换分区。这种情况下，交换分区的大小应该至少和系统内存相同。

交换到磁盘从来就不是一件好事。对于机械硬盘，通过听硬盘的工作噪声，同时观察系统的响应速度，就能说出系统是否在交换。对于 SSD，您无法听到工作噪声，但可以使用**top** 或 **free** 程序查看使用了多少交换空间。应该尽量避免使用 SSD 设备作为交换分区。一旦发生交换，首先检查是否输入了不合理的命令，例如试图编辑一个 5GB 的文件。如果交换时常发生，最好的办法是为你的系统添置内存。

5. 设置用户名、密码、root密码；

### 安装软件准备

```bash
sudo pacman-mirrors -i -c China -m rank
```

在弹出的框中选一个最快的源

更新系统

```bash
sudo pacman -Syyu
```

yay 是 AUR 助手，兼容 pacman，以后可以使用 yay 安装软件

```bash
sudo pacman -S yay

yay -S base-devel
# 全部安装
```

从 https://github.com/googlehosts/hosts/blob/master/hosts-files/hosts 中复制解析规则到 `/etc/hosts` 文件头部。

### 安装软件

1. 输入法

```
yay -S fcitx5-im fcitx5-chinese-addons fcitx5-pinyin-zhwiki fcitx5-material-color
```
环境变量
欲在程序中正常启用 Fcitx5, 须设置以下环境变量，并重新登陆：

```
~/.pam_environment

GTK_IM_MODULE DEFAULT=fcitx
QT_IM_MODULE  DEFAULT=fcitx
XMODIFIERS    DEFAULT=@im=fcitx
INPUT_METHOD  DEFAULT=fcitx
SDL_IM_MODULE DEFAULT=fcitx
```
`Fcitx5设置 -> 添加输入法` 添加 拼音 输入法

`Fcitx5设置 -> 配置附加组件 -> 经典用户界面 -> 主题` 设置主题

在拼音输入法（或者 Rime 输入法）的设置中，启用“ **在程序中显示预编辑文本** ”即可启用单行模式

2. 浏览器

```bash
yay -S google-chrome
```

3. v2ray
- 终端
```
yay -S v2ray

# 配置 /etc/v2ray/config.json 后测试
v2ray -test -config /etc/v2ray/config.json

# 开启服务
v2ray -config /etc/v2ray/config.json
```
在 系统设置 - 网络设置 - 代理，选择使用系统代理服务器配置，HTTP代理 和 SSL代理填 `http://localhost:1081` ，SOCKS代理填 `http://localhost:1080` 。

终端内配置：

```
#启用代理
export http_proxy=http://localhost:1081
export https_proxy=http://localhost:1081
# 关闭代理
unset http_proxy
unset https_proxy

# 通过运行proxy命令启用代理，运行unproxy命令关闭代理，这样就可以在代理与非代理之间切换自如
alias proxy="export http_proxy=http://localhost:1081;export https_proxy=http://localhost:1081" 
alias unproxy="unset http_proxy;unset https_proxy"
```

- UI客户端

```
# qv2ray
yay -S qv2ray

# v2raya
yay -S v2raya
```

4. 编辑类

```
yay -S vim
yay -S typora
yay -S sublime-text-4
```

5. oh-my-zsh

下载 `install.sh` 并执行：
```bash
cd ~
wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
bash install.sh
# 选择切换默认shell为zsh
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

6. 编程类

```
yay -S gitkraken
yay -S visual-studio-code-bin
yay -S pycharm-community-edition
yay -S codeblocks
yay -S dosbox
```

7. 阅读类

```
yay -S foxitreader
yay -S calibre
```

8. 办公类

```
yay -S libreoffice-fresh libreoffice-fresh-zh-cn
```

9. 通讯类

```
# qq
yay -S linuxqq
yay -S icalingua

# wechat
yay -S wechat-uos
yay -S electron-wechat

# feishu
yay -S electron-lark

# dingtalk
yay -S dingtalk-bin
```

10. 图像类

```
yay -S flameshot
yay -S gimp
```

11. 音乐类

```
yay -S qqmusic-bin
yay -S netease-cloud-music
```

12. 邮件类

```
yay -S thunderbird thunderbird-i18n-zh-cn
```

13. 下载类

```
yay -S uget
```

14. 网盘类

```
# 百度网盘
yay -S baidunetdisk-bin

# 坚果云
yay -S nutstore
```
15. 网络类

```
yay -S filezilla
yay -S insomnia-bin
yay -S fiddler
yay -S wireshark-qt
```

16. 工具类

```
yay -S mathpix-snipping-tool
yay -S edrawmax-cn
yay -S netron-bin
yay -S droidcam
```

### 安装虚拟机

为安装一些与系统不兼容的软件，可以安装虚拟机后在虚拟机中安装。

```
# 查看系统内核版本
uname -r

# 根据内核版本选择安装
yay virtualbox-host-modules

# 安装扩展包
yay -S virtualbox-ext-oracle
```

打开 virtualbox，新建一台虚拟机，设置启动光盘，选择虚拟光盘文件，然后启动。

### UI设置

1. 安装dock

```
yay -S latte-dock

# 启动
latte-dock
```

2. 在系统设置 - 外观 - 全局主题 - 获取新全局主题，搜索“macos”，选择最多下载在前，安装“whitesur”主题并使用，勾选“使用来自主题的桌面布局”，应用；
3. 在系统设置 - 外观 - 应用程序风格，选择“Breeze微风”，点击配置 - 透明度，设置为半透明；
4. 在系统设置 - 外观 - 应用程序风格 - 配置GNOME/GTK应用程序风格 - 获取新GNOME/GTK应用程序风格，搜索“bigsur”，选择最多下载在前，安装“bigsur-originals-gtk-blue-light”风格并使用；
5. 在系统设置 - 外观 - Plasma样式 - 获取新Plasma样式，搜索“macos”，选择最多下载在前，安装“whitesur-dark”样式并使用；
6. 在系统设置 - 外观 - 图标 - 获取新图标，搜索“bigsur”，选择最多下载在前，安装“bigsur icon theme”图标并使用；
7. 复制Windows系统 `C:\Windows\Fonts` 目录到 `/usr/share/fonts` ，重命名为 `Windows-Fonts` ，在同级创建目录 `MacOS-Fonts` ，存放苹方系列字体文件，在系统设置 - 外观 - 字体，调整所有字体，选择 苹方简体常规，固定宽度字体选择 `Consolas` ；
8. 在系统设置 - 开机与关机 -登陆屏幕（SDDM），选择“whitesur”使用；
9. 在桌面右键 - 配置桌面和壁纸 - 获取新壁纸，搜索“macos”，选择最多下载在前，安装壁纸，配置播放幻灯片；
10. 在桌面右键 - 配置桌面和壁纸 - 获取新壁纸，搜索“2560 x 1440”，选择最多下载在前，安装壁纸，在 `~/.local/share/wallpapers` 中选择壁纸复制，替换主题中的锁屏背景图片 `~/.local/share/wallpapers/WhiteSur/contents/images/2560x1440.png` 、  `/usr/share/sddm/themes/WhiteSur/background.png` ，调整大小为 `1920x1080` 并使用Gimp设置高斯模糊 (10,10) 导出为新图片，替换主题中的欢迎屏幕背景图片 `~/.local/share/plasma/look-and-feel/com.github.vinceliuiceWhiteSur/contents/splash/images/background.png` ，原有图片重命名为 `backup.png` ；
11. 设置顶栏，右键编辑面板，点击配置系统托盘，将面板间距设置可变大小，将 `Manjaro设置管理器` 、 `News available!` 、 `Yakuake` 、 `蓝牙` 、 `剪贴板` 设置总是隐藏，配置数字时钟，日期自适应位置，不显示秒，时间显示24小时制；
12. 编辑终端Konsole，设置-显示工具栏 都取消，右键编辑当前方案，常规 设置命令为 `/bin/zsh` ，外观 - 配色方案和字体 选择微风，点编辑，勾选模糊背景，设置背景透明度为40%，字体选择 `Consolas` ，外观 - 光标 设置为 I字型，闪烁已启用；
13. 在系统设置 - 显卡与显示器 - 显示器配置，设置全局缩放率，重启电脑；
14. 打开 Dolphin，在 设置 - 配置Dolphin - 右键菜单，勾选git，点击 下载新服务，搜索“terminal”，选择最多下载在前，安装“Your Terminal Menu - Open Terminal Here”，确定后重启 Dolphin；
15. 为了搭配 Dolphin 的git功能，在终端输入 ` git config --global core.editor "code --wait"` ，接下来打开配置文件  `git config --global -e` ，添加以下配置项：

```
[diff]
    tool = code
[difftool "code"]
    cmd = code --wait --diff $LOCAL $REMOTE

[merge]
    tool = code
[mergetool]
    keepBackup = false
[mergetool "code"]
    cmd = code --wait $MREGED
    trustExitCode = false
```

### 注意事项

每天要开机执行一遍 `sudo pacman -Syyu` ，及时更新。

卸载软件使用

```
sudo pacman -Rs <package>
```



