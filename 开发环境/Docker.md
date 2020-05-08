1. 升级系统至64 位版本的 Windows 10 Pro；
2. 在BIOS的Advanced->CPU Configuration里的Virtualization设置为Enabled；
3. 打开windows的【启用或关闭windows功能】，安装Hyper-V；
4. 下载[Docker Desktop](https://www.docker.com/products/docker-desktop)并安装；
5. 打开Docker Desktop设置，勾选“Expose daemon on tcp://localhost:2375 without TLS”、“Enable the experimental WSL 2 based engine”，“Resources  WSL Integration”里选择安装的WSL2发行版；

6. 在WSL2里查看docker版本信息
```
docker version
```

7. 登录https://cr.console.aliyun.com/注册账号，得到一个专属的镜像加速地址；

8. 打开Docker Desktop设置，“Docker Engine”里编辑"registry-mirrors": ["<镜像加速地址>“]