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
* –name ubuntu 表示Ubuntu镜像启动名称，如果没有指定，那么Docker将会随机分配一个名字；
* ubuntu 表示docker run启动的镜像文件；
```
# 查看创建的容器
docker ps -a
# 停止/删除容器
docker stop <容器ID>
docker rm <容器ID>
# 启动容器
docker start -i <容器ID>
# 保存容器为镜像
docker commit <容器ID> <镜像名>
```

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
apt update && apt upgrade
```

#### 2. 安装vim

#### 3. 安装SSH

设置开机自启，在~/.bashrc追加

```
/etc/init.d/ssh start
```

#### 4. 安装MySQL

#### 5. 安装JDK8

#### 6. 安装Maven

#### 7. 安装Hadoop3.2.1

#### 8. 安装HBase2.2.4

#### 9. 安装Hive3.1.2

#### 10. 安装Anaconda

#### 11. 编译安装Spark2.4.5

```
cd spark-2.4.5
export MAVEN_OPTS="-Xmx2g -XX:ReservedCodeCacheSize=1g"
./dev/make-distribution.sh --name hadoop3.2 --tgz -Phadoop-3.2 -Dhadoop.version=3.2.1 -Phive -Phive-thriftserver -Pmesos -Pyarn -Pkubernetes -DskipTests
```

#### 12.  配置Hadoop集群

接下来，我们来看下如何配置Hadoop集群；对一些文件的设置和之前教程一样，首先打开hadoop_env.sh文件，修改JAVA_HOME

```bash
cd /usr/local/hadoop
vim etc/hadoop/hadoop-env.sh
# 将export JAVA_HOME=${JAVA_HOME}替换成
export JAVA_HOME="/usr/local/jdk"
```

接着打开etc/hadoop/core-site.xml，输入一下内容:

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

加入可能缺失的jar包

```
cd share/hadoop/yarn/lib
wget https://repo1.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.jar
```

退出docker，保存这个镜像

```
# 查看当前容器ID
docker ps -a
docker commit <容器ID> ubuntu/hadoop
```

接下来，我们在三个终端上开启三个容器运行镜像，分别表示Hadoop集群中的master,slave01和slave02；

```bash
# 第一个终端
docker run -it -p 50070:50070 -p 9870:9870 -p 8088:8088 -h master --name master ubuntu/hadoop
# 第二个终端
docker run -it -h slave01 --name slave01 ubuntu/hadoop
# 第三个终端
docker run -it -h slave02 --name slave02 ubuntu/hadoop
```

接着配置master,slave01和slave02的地址信息，这样他们才能找到彼此，分别打开/etc/hosts可以查看本机的ip和主机名信息,最后得到三个ip和主机地址信息如下:

```
172.17.0.2      master
172.17.0.3      slave01
172.17.0.4      slave02
```

最后把上述三个地址信息分别复制到master,slave01和slave02的/etc/hosts即可，**每次开启容器hosts文件会自动改变，需要重新配置**

我们可以用如下命令来检测下是否master是否可以连上slave01和slave02

```
ssh slave01
ssh slave02
```

到这里，我们还差最后一个配置就要完成hadoop集群配置了，打开master上的slaves文件，输入两个slave的主机名:

```bash
# 默认为 localhost，所以在伪分布式配置时，节点即作为 NameNode 也作为 DataNode。分布式配置可以保留 localhost，也可以删掉，让 Master 节点仅作为 NameNode 使用
vim /usr/local/hadoop/etc/hadoop/slaves(或/usr/local/hadoop/etc/hadoop/workers)
# 将localhost替换成两个slave的主机名
slave01
slave02
```

ok，Hadoop集群已经配置完成，我们来启动集群；

在master终端上，首先进入/usr/local/hadoop，然后运行如下命令:

```bash
cd /usr/local/hadoop
bin/hdfs namenode -format
sbin/start-all.sh
```

> 如果遇到错误ERROR: but there is no HDFS_NAMENODE_USER defined
>
> 在start-dfs.sh和stop-dfs.sh开头加入：
>
> ```
> HDFS_DATANODE_USER=root
> HADOOP_SECURE_DN_USER=hdfs
> HDFS_NAMENODE_USER=root
> HDFS_SECONDARYNAMENODE_USER=root 
> ```
> 在start-yarn.sh和stop-yarn.sh开头加入：
> ```
> YARN_RESOURCEMANAGER_USER=root
> HADOOP_SECURE_DN_USER=yarn
> YARN_NODEMANAGER_USER=root
> ```

这时Hadoop集群就已经开启，我们可以在master,slave01和slave02上分别运行命令jps查看运行结果;
下面是运行结果图

![master运行结果](Docker搭建Hadoop分布式集群.assets/1.png)
![slave01运行结果](Docker搭建Hadoop分布式集群.assets/2.png)
![slave02运行结果](Docker搭建Hadoop分布式集群.assets/3.png)

#### 13. 运行Hadoop实例程序grep

到目前为止，我们已经成功启动hadoop分布式集群，接下来，我们通过运行hadoop自带的grep实例来查看下如何在hadoop分布式集群运行程序；这里我们运行的实例是hadoop自带的grep

因为要用到hdfs，所以我们先在hdfs上创建一个目录:

```bash
./bin/hdfs dfs -mkdir -p /user/hadoop/input
```

然后将/usr/local/hadoop/etc/hadoop/目录下的所有文件拷贝到hdfs上的目录:

```bash
./bin/hdfs dfs -put ./etc/hadoop/*.xml /user/hadoop/input
```

然后通过ls命令查看下是否正确将文件上传到hdfs下:

```bash
./bin/hdfs dfs -ls /user/hadoop/input
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
./bin/hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep /user/hadoop/input output 'dfs[a-z.]+'
```

过一会，等这个程序运行结束之后，就可以在hdfs上的output目录下查看到运行结果:

```bash
./bin/hdfs dfs -cat output/*

1   dfsadmin
1   dfs.replication
1   dfs.namenode.name.dir
1   dfs.datanode.data.dir
```

hdfs文件上的output目录下，输出程序正确的执行结果，hadoop分布式集群顺利执行grep程序