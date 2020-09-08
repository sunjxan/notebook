### 连接MySQL

[原网页](<http://dblab.xmu.edu.cn/blog/1724-2/>)

1. 下载jdbc驱动（<https://dev.mysql.com/downloads/connector/j/>）

```
cd /usr/local/spark
sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.20.tar.gz

# 解压
sudo tar -xvf mysql-connector-java-8.0.20.tar.gz
# 移动到lib目录
sudo mv mysql-connector-java-8.0.20/mysql-connector-java-8.0.20.jar jars
```

2. 启动pyspark
```
pyspark
```

3. 连接数据库
```
# 获取整张表
jdbcDF = spark.read.format("jdbc").option("url", "jdbc:mysql://<服务器IP>:3306/<数据库名>").option("driver","com.mysql.cj.jdbc.Driver").option("user", "root").option("password", "<root密码>").option("dbtable", "<表名>").load()

# 执行查询语句
jdbcDF = spark.read.format("jdbc").option("url", "jdbc:mysql://<服务器IP>:3306/<数据库名>").option("driver","com.mysql.cj.jdbc.Driver").option("user", "root").option("password", "<root密码>").option("query", "select * from <表名>").load()
```

### 编译安装Spark添加Hive支持

[原网页](<http://dblab.xmu.edu.cn/blog/1729-2/>)

为了让Spark能够访问Hive，必须为Spark添加Hive支持。Spark官方提供的预编译版本，通常是不包含Hive支持的，需要采用源码编译，编译得到一个包含Hive支持的Spark版本。

#### 测试已经安装的Spark版本是否支持Hive

```
spark-shell
```

输入scala代码

```
import org.apache.spark.sql.hive.HiveContext
```

如果返回错误

```
error: object hive is not a member of package org.apache.spark.sql
```

也就是spark无法识别org.apache.spark.sql.hive.HiveContext，这就说明你当前电脑上的Spark版本不包含Hive支持。

#### 下载源码编译

```
cd ~
# 下载源码（http://spark.apache.org/downloads.html）
wget http://www.trieuvan.com/apache/spark/spark-2.4.5/spark-2.4.5.tgz
# 解压
tar -xvf spark-2.4.5.tgz

cd spark-2.4.5
# 编译（https://spark.apache.org/docs/latest/building-spark.html）
# 配置Maven内存限制
export MAVEN_OPTS="-Xmx2g -XX:ReservedCodeCacheSize=1g"
# 编译
./dev/make-distribution.sh --name hadoop2.10 --tgz -Phadoop-2.10 -Dhadoop.version=2.10.0 -Phive -Phive-thriftserver -Pmesos -Pyarn -Pkubernetes -DskipTests
# -Phadoop-2.10 -Dhadoop.version=2.10.0 指定安装spark时的hadoop版本，一定要对应，这个hadoop版本是你当前电脑上已经安装的Hadoop的版本
# -Phive -Phive-thriftserver 这两个选项让其支持Hive
# -DskipTests 能避免测试不通过时发生的错误
```

#### 安装

```
# 解压
sudo tar -xvf spark-2.4.5-bin-hadoop2.10.tgz -C /usr/local
cd /usr/local
sudo mv spark-2.4.5-bin-hadoop2.10 spark

# 设置环境变量，在~/.zshrc追加
# PYTHONPATH环境变量主要是为了在Python3中引入pyspark库，PYSPARK_PYTHON变量主要是设置pyspark运行的python版本
# 为避免与hadoop脚本冲突，不要把sbin目录加入PATH
export SPARK_HOME="/usr/local/spark"
export PYSPARK_PYTHON="/usr/local/anaconda/bin/python"
export PYTHONPATH="${SPARK_HOME}/python:${SPARK_HOME}/python/lib/pyspark.zip:${SPARK_HOME}/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH"
export PATH="${SPARK_HOME}/bin:$PATH"

# 生效
source ~/.zshrc

# 查看版本
pyspark --version

# 因为在spark中很多操作需要文件所有者权限，所以需要更改spark目录所有者
sudo chown -R <user>:<user> /usr/local/spark

# 如果安装的是without hadoop的版本，加入hadoop中的依赖包
cd /usr/local/spark
cp ./conf/spark-env.sh.template ./conf/spark-env.sh
echo export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath) >> ./conf/spark-env.sh

# 设置hive引擎为spark
# 修改hive的hive-site.xml配置文件，configuration中添加
<property>
  <name>hive.execution.engine</name>
  <value>spark</value>
</property>
<property>
  <name>hive.metastore.schema.verification</name>
  <value>false</value>
</property>
```

有了上面的配置信息以后，Spark就可以把数据存储到Hadoop分布式文件系统HDFS中，也可以从HDFS中读取数据。如果没有配置上面信息，Spark就只能读写本地数据，无法读写HDFS数据。配置完成后就可以直接使用，不需要像Hadoop运行启动命令。

验证Spark是否安装成功

```
run-example SparkPi 2>&1 | grep "Pi is"

# 如果如果安装的是包含hadoop的版本,且hadoop(/usr/local/hadoop/share/hadoop/common/lib/)和spark(/usr/local/spark/jars/)有两个不同版本的guava jar包，会报错，应该删除低版本，并拷贝高版本
```

### 连接Hive读写数据

现在我们看如何使用Spark读写Hive中的数据，先启动Hadoop和MySQL。

修改“/usr/local/sparkwithhive/conf/spark-env.sh”这个配置文件：

```
export JAVA_HOME="/usr/local/jdk"
export CLASSPATH="/usr/local/hive/lib:$CLASSPATH"
export HADOOP_CONF_DIR="/usr/local/hadoop/etc/hadoop"
export HIVE_CONF_DIR="/usr/local/hive/conf"
export SPARK_CLASSPATH="/usr/local/hive/lib/mysql-metadata-storage-0.9.2.jar:$SPARK_CLASSPATH"
```

复制hive配置文件：

```
cp /usr/local/hive/conf/hive-site.xml /usr/local/spark/conf
```

下载jdbc驱动（<https://dev.mysql.com/downloads/connector/j/>  Platform Independent）：

```
cd /usr/local/spark
sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.20.tar.gz

# 解压
sudo tar -xvf mysql-connector-java-8.0.20.tar.gz
# 移动到jars目录
sudo mv mysql-connector-java-8.0.20/mysql-connector-java-8.0.20.jar jars
```

使用Spark SQL命令行可以直接使用SQL语句

```bash
spark-sql
```

在python中使用Spark SQL：

```python
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext, HiveContext, SQLContext

# 直接获取SparkContext
sc = SparkContext('yarn', 'test')

# 先获取SparkSession
spark = SparkSession.builder.master("mesos://master:5050").appName("test").enableHiveSupport().getOrCreate()
sc = ss.sparkContext

# 使用SQLContext获取数据
sqlCtx = SQLContext(sc)
sqlCtx.sql('use default')
sqlCtx.sql('select * from student').show()

# HiveContext继承自SQLContext
hc = HiveContext(sc)
hc.sql('use default')
hc.sql('select * from student').show()

# SparkSession其实是封装了SQLContext和HiveContext
spark.sql('use default')
spark.sql('select * from student').show()
```

```python
SparkSession.builder.master("mesos://master:5050").appName("test").enableHiveSupport()
# 等价于
SparkSession.builder.config('spark.master', 'yarn').config('spark.app.name', 'test').config('spark.sql.catalogImplementation', 'hive')
```

建立基类

```python
import sys
sys.path.extend(['/usr/local/spark/python', '/usr/local/spark/python/lib/pyspark.zip', '/usr/local/spark/python/lib/py4j-0.10.7-src.zip'])

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext, HiveContext, SQLContext

class SparkSessionBase:

    SPARK_APP_NAME = "test"
    SPARK_MASTER = "mesos://master:5050"
    SPARK_EXECUTOR_MEMORY = "2g"
    SPARK_EXECUTOR_CORES = 2
    SPARK_EXECUTOR_INSTANCES = 2

    ENABLE_HIVE_SUPPORT = False

    def _create_spark_session(self):

        conf = SparkConf()  # 创建spark config对象
        config = (
            ("spark.app.name", self.SPARK_APP_NAME),  # 设置启动的spark的app名称，没有提供，将随机产生一个名称
            ("spark.master", self.SPARK_MASTER),  # spark master的地址
            ("spark.executor.memory", self.SPARK_EXECUTOR_MEMORY),  # 设置该app启动时占用的内存用量，默认2g
            ("spark.executor.cores", self.SPARK_EXECUTOR_CORES),  # 设置spark executor使用的CPU核心数，默认是1核心
            ("spark.executor.instances", self.SPARK_EXECUTOR_INSTANCES)
        )
        conf.setAll(config)

        # 利用config对象，创建spark session
        if self.ENABLE_HIVE_SUPPORT:
            return SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()
        else:
            return SparkSession.builder.config(conf=conf).getOrCreate()
```
继承基类
```
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from offline import SparkSessionBase
class MySparkSession(SparkSessionBase):

    SPARK_APP_NAME = "mySpark"

    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()
        self.sc = self.spark.sparkContext
```

