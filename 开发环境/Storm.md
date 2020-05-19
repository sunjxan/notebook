### 安装Zookeeper

```
cd /usr/local
# 下载安装包（https://zookeeper.apache.org/releases.html）
sudo wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/zookeeper-3.6.1/apache-zookeeper-3.6.1-bin.tar.gz
# 解压
sudo tar -xvf apache-zookeeper-3.6.1-bin.tar.gz
sudo mv apache-zookeeper-3.6.1-bin zookeeper

cd zookeeper
sudo mkdir tmp
sudo cp conf/zoo_sample.cfg conf/zoo.cfg
sudo vim conf/zoo.cfg
# 修改配置
将 dataDir=/tmp/zookeeper 更改为 dataDir=/usr/local/zookeeper/tmp 

# 设置环境变量，在~/.zshrc追加
export ZOOKEEPER_HOME="/usr/local/zookeeper"
export PATH="${ZOOKEEPER_HOME}/bin:$PATH"

# 生效
source .zshrc

#查看版本
zkServer.sh version

# 因为在zookeeper中很多操作需要文件所有者权限，所以需要更改zookeeper目录所有者
sudo chown -R <user> /usr/local/zookeeper

# 启动
zkServer.sh start
# 若显示 “Starting zookeeper … STARTED”表示启动成功
```

### 安装Storm

```
cd /usr/local
# 下载安装包（http://storm.apache.org/downloads.html）
sudo wget https://downloads.apache.org/storm/apache-storm-2.1.0/apache-storm-2.1.0.tar.gz
# 解压
sudo tar -xvf apache-storm-2.1.0.tar.gz
sudo mv apache-storm-2.1.0 storm

# 设置环境变量，在~/.zshrc追加
export STORM_HOME="/usr/local/storm"
export PATH="${STORM_HOME}/bin:$PATH"

# 生效
source .zshrc

#查看版本
storm version

# 因为在storm中很多操作需要文件所有者权限，所以需要更改storm目录所有者
sudo chown -R <user> /usr/local/storm

# 修改配置conf/storm.yaml，修改storm.zookeeper.servers和nimbus.host
storm.zookeeper.servers:
    -"127.0.0.1"
#     - "server1"
#     - "server2"
#
nimbus.host:
    -"127.0.0.1"
# nimbus.seeds:["host1", "host2", "host3"]

# 启动
storm nimbus
# 查看运行情况
storm list
```