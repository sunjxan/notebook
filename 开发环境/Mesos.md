[原网页](https://docs.huihoo.com/apache/mesos/mesos-cn/primer/Mesos-of-Getting-Started.html)

```
cd /usr/local
# 下载安装包（http://mesos.apache.org/downloads/）
sudo wget https://mirrors.tuna.tsinghua.edu.cn/apache/mesos/1.9.0/mesos-1.9.0.tar.gz
# 解压
sudo tar -xvf mesos-1.9.0.tar.gz
sudo mkdir mesos /var/lib/mesos

# 因为在mesos中很多操作需要文件所有者权限，所以需要更改mesos目录所有者
sudo chown -R <user>:<user> /usr/local/mesos-1.9.0 /usr/local/mesos /var/lib/mesos

# 确保你的主机名可以通过 DNS 或 /etc/hosts 解析，从而可以完全支持 Docker 的 host-networking 功能。这在一些 Mesos 测试中会被用到。如有疑问，请确认 /etc/hosts 中包含你的主机名。

# 安装tar、wget、git、jdk、maven后，再安装依赖
sudo aptitude update
sudo aptitude install tar wget git autoconf libtool build-essential python-dev python-boto libcurl4-nss-dev libsasl2-dev libsasl2-modules libapr1-dev libsvn-dev zlib1g-dev -y

# 构建
cd mesos-1.9.0
mkdir build
cd build
../configure --prefix=/usr/local/mesos
make -j8
make -j8 install
# 安装完成可以删除编译目录

# 设置环境变量，在~/.zshrc追加
export MESOS_HOME="/usr/local/mesos"
export PATH="${MESOS_HOME}/bin:${MESOS_HOME}/sbin:$PATH"

# 生效
source ~/.zshrc

# 查看版本
mesos-master --version

# 启动master
mesos-master --ip=0.0.0.0 --work_dir=/var/lib/mesos >/dev/null 2>&1 &
# 启动slave
mesos-slave --ip=0.0.0.0 --master=<master IP>:5050 --work_dir=/var/lib/mesos --no-systemd_enable_support >/dev/null 2>&1 &
```

