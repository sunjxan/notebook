1. 下载安装包并安装（https://sourceforge.net/projects/vcxsrv/）；
2. 打开CMD，查看端口是否被占用，如果被占用，根据行末的PID关闭该进程：
```
netstat -ano | findstr 0.0.0.0:6000

taskkill /pid <PID> -f
```
3. 打开XLaunch，依次设置：

Multiple windows

Display number  -1

Start no client

勾选 Disable access control

Save configuration  保存到桌面 "config.xlaunch"，以后从这里打开

取消  只保存，不继续打开

4. 防火墙设置，`VcXsrv windows xserver` 专用网络、公用网络都允许访问；
5. 在WSL2配置环境变量：
```
vim ~/.zshrc

export DISPLAY=$(cat /etc/resolv.conf | grep 'nameserver' | cut -f 2 -d ' '):0

source ~/.zshrc
```
7. 测试，在WSL2安装xclock，打开：
```
sudo apt install x11-apps
xclock
```