```
cd /usr/local
# 下载安装包（https://kafka.apache.org/downloads.html）
sudo wget http://mirror.metrocast.net/apache/kafka/2.5.0/kafka_2.13-2.5.0.tgz
# 解压
sudo tar -xvf kafka_2.13-2.5.0.tgz
sudo mv kafka_2.13-2.5.0 kafka

# 设置环境变量，在~/.zshrc追加
export KAFKA_HOME="/usr/local/kafka"
export PATH="${KAFKA_HOME}/bin:$PATH"

# 生效
source .zshrc

# 查看版本
kafka-server-start.sh --version

# 因为在kafka中很多操作需要文件所有者权限，所以需要更改kafka目录所有者
sudo chown -R <user> /usr/local/kafka
```

[原网页](<http://dblab.xmu.edu.cn/blog/1743-2/>)

### 测试简单实例

按顺序执行如下命令：

```bash
cd /usr/local/kafka
zookeeper-server-start.sh config/zookeeper.properties
```

命令执行后不会返回Shell命令输入状态，zookeeper就会按照默认的配置文件启动服务，请千万不要关闭当前终端，启动新的终端，输入如下命令：

```bash
kafka-server-start.sh config/server.properties
```

kafka服务端就启动了,请千万不要关闭当前终端，启动另外一个终端,输入如下命令:

```bash
# 这个topic叫dblab，2181是zookeeper默认的端口号，partition是topic里面的分区数，replication-factor是备份的数量，在kafka集群中使用，这里单机版就不用备份了
kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic dblab
```

topic是发布消息发布的category，以单节点的配置创建了一个叫dblab的topic，可以用list列出所有创建的topics，来查看刚才创建的主题是否存在。

```bash
kafka-topics.sh --list --zookeeper localhost:2181
```

可以在结果中查看到dblab这个topic存在。接下来用producer生产点数据：

```bash
kafka-console-producer.sh --broker-list localhost:9092 --topic dblab
```

并尝试输入如下信息：

```
hello hadoop
hello xmu
hadoop world
```

然后再次开启新的终端或者直接按CTRL+C退出。然后使用consumer来接收数据,输入如下命令：

```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic dblab --from-beginning
```

便可以看到刚才产生的三条信息。说明kafka安装成功。