[原网页](<http://dblab.xmu.edu.cn/blog/1233/>)

## 在Docker安装Ubuntu系统

安装好Docker之后，接下来就要在Docker上安装Ubuntu，其实和安装其他镜像一样，只需运行一个命令足矣，如下:

```bash
docker pull ubuntu:18.04
```

docker pull命令表示从Docker hub上拉取Ubuntu镜像到本地；这时可以在终端运行以下命令查看是否安装成功

```bash
docker images
```

有如下输出则表示安装成功:

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              18.04              4ca3a192ff2a        11 days ago         128.2 MB
```

docker images表示列出Docker上所有的镜像；镜像也是一堆文件，我们需要在Docker上开启这Ubuntu系统；在启动Ubuntu镜像时，需要先在个人文件下创建一个目录，用于向Docker内部的Ubuntu系统传输文件；命令如下:

```bash
cd ~
mkdir docker_files
cp /etc/apt/sources.list ./docker_files
```

替换docker_files/source.list文件内容

[阿里云源](<https://developer.aliyun.com/mirror/ubuntu>)  18.04

```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

然后再在Docker上运行Ubuntu系统；

```bash
docker run -it -p 80:80 -v /home/<user>/docker_files:/root/docker_files --name ubuntu18.04 <镜像ID>
```

这里解析下这个命令参数：
* docker run 表示运行一个镜像；
* -i表示开启交互式；-t表示分配一个tty，可以理解为一个控制台；因此-it可以理解为在当前终端上与docker内部的ubuntu系统交互；
* -p 表示将容器内的端口映射出来，可同时映射多对；
* -v 表示docker内部的ubuntu系统`/root/docker_files`目录与本地`/home/<user>/docker_files`共享；这可以很方便将本地文件上传到Docker内部的Ubuntu系统；
* –-name ubuntu 表示Ubuntu镜像启动名称，如果没有指定，那么Docker将会随机分配一个名字；
* ubuntu 表示docker run启动的镜像文件；

## Ubuntu系统初始化

刚安装好的Ubuntu系统，是一个很纯净的系统，很多软件是没有安装的，所以我们需要先更新下Ubuntu系统的源以及安装一些必备的软件；

#### 1. 更新系统软件源

查看Ubuntu版本，选择更换源版本

```
cat /etc/lsb-release
cp /etc/apt/sources.list /etc/apt/sources.list.bak
cp /root/docker_files/sources.list /etc/apt/sources.list
```

更新系统源命令如下

```bash
apt update && apt upgrade -y
```

#### 2. 安装vim

#### 3. 安装net-tools

#### 4. 安装SSH

设置开机自启，在~/.bashrc追加

```
echo /etc/init.d/ssh start >> ~/.bashrc
```

#### 5. 安装MySQL

#### 6. 安装JDK8

#### 7. 安装Maven3.6.3

## 安装Hadoop软件

#### 1. 安装ZooKeeper3.6.1

#### 2. 安装Hadoop2.10.0

#### 3. 安装HBase1.6.0

#### 4. 安装Hive2.3.7

#### 5. 安装Anaconda3

#### 6. 编译Spark2.4.5-Hadoop2.10.0

#### 7. 安装Spark2.4.5

#### 8. 安装Sqoop1.4.7

## 配置分布式集群

#### 1. 配置ZooKeeper集群

在conf/zoo.cfg中追加

```
server.0=master:2888:3888
server.1=slave01:2888:3888
server.2=slave02:2888:3888
```

#### 2. 配置Hadoop集群

接下来，我们来看下如何配置Hadoop集群；对一些文件的设置和之前教程一样，首先打开etc/hadoop/hadoop_env.sh文件，修改JAVA_HOME

```bash
# 将export JAVA_HOME=${JAVA_HOME}替换成
export JAVA_HOME="/usr/local/jdk"
```

接着打开etc/hadoop/core-site.xml，输入以下内容:

```
<configuration>
      <property>
          <name>fs.defaultFS</name>
          <value>hdfs://master:9000</value>
      </property>
      <property>
          <name>hadoop.tmp.dir</name>
          <value>file:///usr/local/hadoop/tmp</value>
          <description>Abase for other temporary directories.</description>
      </property>
</configuration>
```

然后再打开etc/hadoop/hdfs-site.xml输入以下内容（dfs.replication设为 节点数）:

```
<configuration>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///usr/local/hadoop/namenode_dir</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///usr/local/hadoop/datanode_dir</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value>3</value>
    </property>
</configuration>
```

接下来修改etc/hadoop/mapred-site.xml（可能需要先重命名，默认文件名为 mapred-site.xml.template），输入以下内容:

```
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
      <name>yarn.app.mapreduce.am.env</name>
      <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
    </property>
    <property>
      <name>mapreduce.map.env</name>
      <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
    </property>
    <property>
      <name>mapreduce.reduce.env</name>
      <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
    </property>
</configuration>
```

最后修改etc/hadoop/yarn-site.xml文件，输入以下内容:

```
<configuration>
      <property>
          <name>yarn.resourcemanager.hostname</name>
          <value>master</value>
      </property>
      <property>
          <name>yarn.nodemanager.aux-services</name>
          <value>mapreduce_shuffle</value>
      </property>
</configuration>
```

如果缺失jar包，自行下载

```
cd share/hadoop/yarn/lib
wget https://repo1.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.jar
```

修改slaves列表
```
# 默认为 localhost，所以在伪分布式配置时，节点即作为 NameNode 也作为 DataNode。分布式配置可以保留 localhost，也可以删掉，让 Master 节点仅作为 NameNode 使用
vim /usr/local/hadoop/etc/hadoop/slaves(或/usr/local/hadoop/etc/hadoop/workers)
# 将localhost替换成两个slave的主机名

slave01
slave02
```

#### 3.   配置HBase集群

修改/usr/local/hbase/conf/hbase-env.sh，配置JAVA_HOME，HBASE_MANAGES_ZK设为false（不适用hbase自带zookeeper）

```shell
export JAVA_HOME="/usr/local/jdk"
export HBASE_MANAGES_ZK=false
```

配置/usr/local/hbase/conf/hbase-site.xml

修改hbase.rootdir，指定HBase数据在HDFS上的存储路径；将属性hbase.cluter.distributed设置为true。假设当前Hadoop集群运行在伪分布式模式下，在本机上运行，且NameNode运行在9000端口。

```xml
<configuration>
        <property>
                <name>hbase.rootdir</name>
                <value>hdfs://master:9000/hbase</value>
        </property>
        <property>
                <name>hbase.cluster.distributed</name>
                <value>true</value>
        </property>
        <property>
            <name>hbase.master.info.port</name>
            <value>16010</value>
        </property>
    	<property>
        	<name>hbase.unsafe.stream.capability.enforce</name>
        	<value>false</value>
        </property>
    	<property>
            <name>hbase.zookeeper.quorum</name>
            <value>master,slave01,slave02</value>
        </property>
        <property>
            <name>hbase.zookeeper.property.dataDir</name>
            <value>/usr/local/zookeeper/data</value>
        </property>
</configuration>
```

hbase.rootdir指定HBase的存储目录；hbase.cluster.distributed设置集群处于分布式模式

修改regionservers

```
vim conf/regionservers

master
slave01
slave02
```

#### 4.配置MySQL作为Hive元数据库

#### 5. 配置Spark集群

修改conf/spark-env.sh，追加

```
export JAVA_HOME="/usr/local/jdk"
export CLASSPATH="/usr/local/hive/lib:$CLASSPATH"
export HADOOP_CONF_DIR="/usr/local/hadoop/etc/hadoop"
export HIVE_CONF_DIR="/usr/local/hive/conf"
export SPARK_CLASSPATH="/usr/local/hive/lib/mysql-metadata-storage-0.9.2.jar:$SPARK_CLASSPATH"
export SPARK_MASTER_HOST=master
```

修改conf/slaves

```
cp conf/slaves.template conf/slaves
vim conf/slaves

slave01
slave02
```

#### 6. 配置SparkSQL连接Hive

#### 7. 保存镜像

退出docker，保存这个镜像

```
# 保存容器为镜像
docker commit ubuntu18.04 ubuntu/bigdata
# 导出镜像
docker save -o ubuntu_bigdata.tar ubuntu/bigdata
```

## 启动分布式集群

#### 1. 运行容器

接下来，我们在三个终端上开启三个容器运行镜像，分别表示Hadoop集群中的master,slave01和slave02；

```bash
docker run -it -p 50070:50070 -p 8088:8088 -p 16010:16010 -p 10002:10002 -p 8080:8080 -h master --name master ubuntu/bigdata

docker run -it -h slave01 --name slave01 ubuntu/bigdata

docker run -it -h slave02 --name slave02 ubuntu/bigdata
```

接着配置master,slave01和slave02的地址信息，这样他们才能找到彼此，分别打开/etc/hosts可以查看本机的ip和主机名信息,最后得到三个ip和主机地址信息如下:

```
172.17.0.2      master
172.17.0.3      slave01
172.17.0.4      slave02
```
修改每个结点的/etc/hosts
```
echo '172.17.0.3      slave01
172.17.0.4      slave02' >> /etc/hosts
scp /etc/hosts slave01:/etc
scp /etc/hosts slave02:/etc
```

最后把上述三个地址信息分别复制到master,slave01和slave02的/etc/hosts即可，**每次开启容器hosts文件会自动改变，需要重新配置**

我们可以用如下命令来检测下是否master是否可以连上slave01和slave02

```
ssh slave01
ssh slave02
```

#### 2. 启动ZooKeeper

在配置conf/zoo.cfg中dataDir的路径为每个结点创建myid文件，并启动zkServer

```
# 若显示 “Starting zookeeper … STARTED”表示启动成功
echo 0 >> /usr/local/zookeeper/data/myid
zkServer.sh start

echo 1 >> /usr/local/zookeeper/data/myid
zkServer.sh start

echo 2 >> /usr/local/zookeeper/data/myid
zkServer.sh start
```

#### 3. 启动hadoop

在master终端上，首先进入/usr/local/hadoop，然后运行如下命令:

```bash
hdfs namenode -format
start-dfs.sh && start-yarn.sh
```

> 如果遇到错误ERROR: but there is no HDFS_NAMENODE_USER defined
>
> 在sbin/start-dfs.sh和sbin/stop-dfs.sh开头加入：
>
> ```
> HDFS_DATANODE_USER=root
> HDFS_NAMENODE_USER=root
> HDFS_SECONDARYNAMENODE_USER=root 
> ```
> 在sbin/start-yarn.sh和sbin/stop-yarn.sh开头加入：
> ```
> YARN_RESOURCEMANAGER_USER=root
> YARN_NODEMANAGER_USER=root
> ```

这时Hadoop集群就已经开启，我们可以在master,slave01和slave02上分别运行命令jps查看运行结果;
下面是运行结果图

![master运行结果](Docker搭建Hadoop分布式集群.assets/1.png)

![slave01运行结果](Docker搭建Hadoop分布式集群.assets/2.png)

![slave02运行结果](Docker搭建Hadoop分布式集群.assets/3.png)

#### 4. 启动HBase

```bash
start-hbase.sh
```

启动成功，输入命令jps，看到以下界面说明hbase启动成功

![hbase jps](Docker搭建Hadoop分布式集群.assets/4.png)

进入shell界面：

```bash
hbase shell
```

注意：如果在操作HBase的过程中发生错误，可以通过{HBASE_HOME}目录（/usr/local/hbase）下的logs子目录中的日志文件查看错误原因。
这里启动关闭Hadoop和HBase的顺序一定是：
启动Hadoop—>启动HBase—>关闭HBase—>关闭Hadoop

#### 5. 启动MySQL

#### 6. 启动Hive

```
hive --service hiveserver2 >/dev/null 2>&1 &
```

#### 7. 启动Spark

```
/usr/local/spark/sbin/start-all.sh
```

#### 8. WebUI

HDFS  http://localhost:50070/dfshealth.html  hadoop3+端口改为9870

yarn  http://localhost:8088/cluster

hbase  http://localhost:16010/master-status

hive  http://localhost:10002

spark  http://localhost:8080

在WSL2中要使用子系统的ip来访问

```
export WSLIP=$(ip addr show eth0 | grep 'inet ' | cut -f 6 -d ' ' | cut -f 1 -d '/')
```

## 实例程序

#### 1. 运行Hadoop实例程序grep

到目前为止，我们已经成功启动hadoop分布式集群，接下来，我们通过运行hadoop自带的grep实例来查看下如何在hadoop分布式集群运行程序；这里我们运行的实例是hadoop自带的grep

因为要用到hdfs，所以我们先在hdfs上创建一个目录/user/root/user

```bash
hdfs dfs -mkdir -p input
```

然后将/usr/local/hadoop/etc/hadoop/目录下的所有文件拷贝到hdfs上的目录:

```bash
hdfs dfs -put /usr/local/hadoop/etc/hadoop/*.xml input
```

然后通过ls命令查看下是否正确将文件上传到hdfs下:

```bash
hdfs dfs -ls input
```

输出如下:

```
Found 9 items
-rw-r--r--   3 root supergroup       4436 2016-12-26 07:40 /user/hadoop/input/capacity-scheduler.xml
-rw-r--r--   3 root supergroup       1090 2016-12-26 07:40 /user/hadoop/input/core-site.xml
-rw-r--r--   3 root supergroup       9683 2016-12-26 07:40 /user/hadoop/input/hadoop-policy.xml
-rw-r--r--   3 root supergroup       1133 2016-12-26 07:40 /user/hadoop/input/hdfs-site.xml
-rw-r--r--   3 root supergroup        620 2016-12-26 07:40 /user/hadoop/input/httpfs-site.xml
-rw-r--r--   3 root supergroup       3518 2016-12-26 07:40 /user/hadoop/input/kms-acls.xml
-rw-r--r--   3 root supergroup       5511 2016-12-26 07:40 /user/hadoop/input/kms-site.xml
-rw-r--r--   3 root supergroup        866 2016-12-26 07:40 /user/hadoop/input/mapred-site.xml
-rw-r--r--   3 root supergroup        947 2016-12-26 07:40 /user/hadoop/input/yarn-site.xml
```

接下来，通过运行下面命令执行实例程序:

```bash
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep input output 'dfs[a-z.]+'
```

过一会，等这个程序运行结束之后，就可以在hdfs上的output目录下查看到运行结果:

```bash
hdfs dfs -cat output/*

1   dfsadmin
1   dfs.replication
1   dfs.namenode.name.dir
1   dfs.datanode.data.dir
```

hdfs文件上的output目录下，输出程序正确的执行结果，hadoop分布式集群顺利执行grep程序

#### 2. Spark加载HDFS文件

   任务：编写一个Spark应用程序，对某个文件中的单词进行词频统计。
   准备工作：请进入Linux系统，打开“终端”，进入Shell命令提示符状态，然后，执行如下命令新建目录：

   ```bash
mkdir /usr/local/spark/input
vim /usr/local/spark/input/word
   ```

   你可以在文本文件中随意输入一些单词，用空格隔开，我们会编写Spark程序对该文件进行单词词频统计。

   下面，我们把本地文件系统中的“/usr/local/spark/input/word”上传到分布式文件系统HDFS中：

   ```bash
hdfs dfs -put /usr/local/spark/input/word input
   ```

   在pyspark输入如下代码：

   ```python
textFile = sc.textFile("input/word")
# 这句与以下两句是等价的
# textFile = sc.textFile("/user/root/input/word")
# textFile = sc.textFile("hdfs://localhost:9000/user/root/input/word")
wordCount = textFile.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a, b : a + b)
print(wordCount.collect())

# 或者一行一行输出
# wordCount.foreach(print)
   ```

#### 3. SparkSQL连接Hive读写数据

现在我们看如何使用Spark读写Hive中的数据，先启动Hadoop和MySQL。

在pyspark（包含Hive支持）中执行以下命令从Hive中读取数据：

```python
from pyspark.sql import HiveContext
hive_context = HiveContext(sc)
hive_context.sql('use default')
hive_context.sql('select * from student').show()
 
+---+--------+------+---+
| id|    name|gender|age|
+---+--------+------+---+
|  1| Xueqian|     F| 23|
|  2|Weiliang|     M| 24|
+---+--------+------+---+
```

使用spark-sql命令行可以直接使用SQL语句

```bash
spark-sql
```

