[原网页](<http://dblab.xmu.edu.cn/blog/install-storm/>)

```
cd /usr/local
# 下载安装包（https://zookeeper.apache.org/releases.html）
sudo wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/zookeeper-3.6.1/apache-zookeeper-3.6.1-bin.tar.gz
# 解压
sudo tar -xvf apache-zookeeper-3.6.1-bin.tar.gz
sudo mv apache-zookeeper-3.6.1-bin zookeeper

# 因为在zookeeper中很多操作需要文件所有者权限，所以需要更改zookeeper目录所有者
sudo chown -R <user>:<user> /usr/local/zookeeper

mkdir /usr/local/zookeeper/data

# 修改配置
cp /usr/local/zookeeper/conf/zoo_sample.cfg /usr/local/zookeeper/conf/zoo.cfg
vim /usr/local/zookeeper/conf/zoo.cfg

dataDir=/usr/local/zookeeper/data 
admin.serverPort=8081

# 设置环境变量，在~/.zshrc追加
export ZK_HOME="/usr/local/zookeeper"
export PATH="${ZK_HOME}/bin:$PATH"

# 生效
source ~/.zshrc

# 查看版本
zkServer.sh version

# 启动
zkServer.sh start
# 若显示 “Starting zookeeper … STARTED”表示启动成功
```
