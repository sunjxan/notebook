[原网页](https://ubuntuqa.com/article/10488.html])

1. 识别NVIDIA VGA卡。以下命令将使您可以识别Nvidia卡型号：

   ```
   $ lspci -vnn | grep VGA
   ```

2. 根据Nvidia卡型号下载官方的[Nvidia驱动程序](https://www.nvidia.com/download/index.aspx?lang=cn) ，将文件保存到您的主目录：

   ```
   $ ls
   NVIDIA-Linux-x86_64-470.74.run
   ```

3. 安装先决条件。编译和安装Nvidia驱动程序需要开发工具和内核头文件。让我们从安装内核头开始。首先，我们需要检测当前加载的内核：

   ```
   $ uname -r
   5.13.19-2-MANJARO
   ```

   我们需要安装的内核头文件是`linux513-headers`：

   ```
   $ sudo pacman -S linux513-headers
   ```

   下一个任务是安装开发工具：

   ```
   $ sudo pacman -S base-devel dkms
   ```

4. 在此步骤中，我们将禁用默认`nouveau`驱动，打开并编辑Grub配置文件：

   ```
$ sudo nano /etc/default/grub
   ```

   改变`GRUB_CMDLINE_LINUX` 行：
   
   ```
GRUB_CMDLINE_LINUX="nouveau.modeset=0"
   ```

   进行更改后，更新GRUB：
   
   ```
$ sudo update-grub
   ```

   重新启动系统：
   
   ```
$ sudo reboot
   ```

5. 重启之后，由于没有显卡驱动的支持，可能会卡在 BIOS Logo 界面或者是黑屏。
   这个时候你需要按下 ALT + CTRL + F2 进入到 TTY 文本模式；
   
6. 安装驱动，遇到选项都使用默认项：

   ```
$ sudo sh NVIDIA-Linux-x86_64-470.74.run -no-opengl-files
   ```

7. 重新启动系统，正确输出信息即安装成功：

   ```
   $ nvidia-smi
   ```

   
