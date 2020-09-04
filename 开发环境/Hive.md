[原网页](<http://dblab.xmu.edu.cn/blog/install-hive/>)

```
cd /usr/local
# 下载安装包（https://hive.apache.org/downloads.html）
sudo wget https://downloads.apache.org/hive/hive-2.3.7/apache-hive-2.3.7-bin.tar.gz
# 解压
sudo tar -xvf apache-hive-2.3.7-bin.tar.gz
sudo mv apache-hive-2.3.7-bin hive

# 设置环境变量，在~/.zshrc追加
export HIVE_HOME="/usr/local/hive"
export PATH="${HIVE_HOME}/bin:$PATH"

# 生效
source ~/.zshrc

# 查看版本
hive --version

# 因为在hive中很多操作需要文件所有者权限，所以需要更改hive目录所有者
sudo chown -R <user>:<user> /usr/local/hive
```

### 配置MySQL作为元数据库

1. 创建/usr/local/hive/conf/hive-site.xml

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://localhost:3306/hive?createDatabaseIfNotExist=true</value>
    <description>JDBC connect string for a JDBC metastore</description>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.cj.jdbc.Driver</value>
    <description>Driver class name for a JDBC metastore</description>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>hive</value>
    <description>username to use against metastore database</description>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>hive</value>
    <description>password to use against metastore database</description>
  </property>
</configuration>
```

2. 下载jdbc驱动（<https://dev.mysql.com/downloads/connector/j/>  Platform Independent）

```
cd /usr/local/hive
sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.20.tar.gz

# 解压
sudo tar -xvf mysql-connector-java-8.0.20.tar.gz
# 移动到lib目录
sudo mv mysql-connector-java-8.0.20/mysql-connector-java-8.0.20.jar lib
```

3. 创建hive数据库
```
sudo service mysql start
# 登录MySQL
sudo mysql -u root -p

# 创建hive数据库
CREATE DATABASE hive;
```

4. 配置mysql允许hive接入
```
# 将所有数据库的所有表的所有权限赋给hive用户，后面的hive是配置hive-site.xml中配置的连接密码
GRANT ALL PRIVILEGES ON *.* TO 'hive'@'localhost' IDENTIFIED BY 'hive' WITH GRANT OPTION;
# 刷新mysql系统权限关系表，使其生效
FLUSH PRIVILEGES;

# 初始化当前 Hive 版本的 Metastore 架构，还可处理从较旧版本到新版本的架构升级
schematool -dbType mysql -initSchema

# 如果hadoop(/usr/local/hadoop/share/hadoop/common/lib/)和hive(/usr/local/hive/lib/)有两个不同版本的guava jar包，会报错，应该删除低版本，并拷贝高版本
```
5. 启动hadoop

6. 启动hive

```
# 1.使用的本地metastore，直接通过hive命令启动
hive
# 相当于以下命令
hive --service cli

# 2.使用远程的metastore，服务器开启metastore服务（端口号默认9083）
hive --service metastore >/dev/null 2>&1 &
# 客户端修改配置，然后启动cli即可
<property>
  <name>hive.metastore.uris</name>
  <value>thrift://<metastore_server_ip>:9083</value>
</property>

# 3.启动hiveserver2，使其他服务可以通过thrift接入hive
# 在hadoop的core-site.xml文件中配置hadoop代理用户，configuration中添加
<property>
  <name>hadoop.proxyuser.<用户名>.groups</name>
  <value>*</value>
</property>
<property>
  <name>hadoop.proxyuser.<用户名>.hosts</name>
  <value>*</value>
</property>
# 设置完后，需要重启hadoop
# 启动hiveserver2
hive --service hiveserver2 >/dev/null 2>&1 &
# beeline工具测试使用jdbc方式连接
beeline -u jdbc:hive2://localhost:10000 -n <用户名>
# 同时启动一个webui（端口号默认10002），可以通过http://localhost:10002/访问
```

#### 简单编程实践

下面我们以词频统计算法为例，来介绍怎么在具体应用中使用Hive。词频统计算法又是最能体现MapReduce思想的算法之一，这里我们可以对比它在MapReduce中的实现，来说明使用Hive后的优势。

MapReduce实现词频统计的代码可以通过下载Hadoop源码后，在 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.1.jar 包中找到(wordcount类)，wordcount类由63行Java代码编写而成。下面首先简单介绍一下怎么使用MapReduce中wordcount类来统计单词出现的次数，具体步骤如下：

1）创建input目录，output目录会自动生成。其中input为输入目录，output目录为输出目录。命令如下：

```shell
cd /usr/local/hadoop
mkdir input
```

2）然后，在input文件夹中创建两个测试文件file1.txt和file2.txt，命令如下：

```shell
cd  /usr/local/hadoop/input
echo "hello world" > file1.txt
echo "hello hadoop" > file2.txt
```

3）启动hadoop，执行如下hadoop命令：

```shell
cd  ..
hdfs dfs -put input/* input
hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount input output
```

4）我们可以到output文件夹中查看结果：

```bash
rm -r ./output    # 先删除本地的 output 文件夹（如果存在）
hdfs dfs -get output ./output     # 将 HDFS 上的 output 文件夹拷贝到本机
cat ./output/*
```

下面我们通过HiveQL实现词频统计功能，此时只要编写下面7行代码，而且不需要进行编译生成jar来执行。HiveQL实现命令如下：

```sql
create table docs(line string);
load data inpath 'input' overwrite into table docs;

create table word_count as
select word, count(1) as count from (select explode(split(line,' ')) as word from docs) w
group by word
order by word;
```

执行后，用select语句查看，结果如下：

![img](Hive.assets/1.png)

由上可知，采用Hive实现最大的优势是，对于非程序员，不用学习编写Java MapReduce代码了，只需要用户学习使用HiveQL就可以了，而这对于有SQL基础的用户而言是非常容易的。

创建的数据库文件保存至hdfs目录/user/hive/warehouse里，同时创建的数据库和表记录在mysql数据库hive的表DBS和TBLS里