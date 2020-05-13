```
cd /usr/local
# 下载安装包（https://hadoop.apache.org/releases.html）
sudo wget https://archive.apache.org/dist/hadoop/common/hadoop-2.10.0/hadoop-2.10.0.tar.gz
# 解压
sudo tar -xvf hadoop-2.10.0.tar.gz
sudo mv hadoop-2.10.0 hadoop

# 设置环境变量，在~/.zshrc追加
export HADOOP_HOME="/usr/local/hadoop"
export HADOOP_COMMON_LIB_NATIVE_DIR="${HADOOP_HOME}/lib/native"
export PATH="${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:$PATH"

# 生效
source .zshrc

#查看版本
hadoop version

# 因为在hadoop中很多操作需要文件所有者权限，所以需要更改hadoop目录所有者
sudo chown -R <user> /usr/local/hadoop
```

***

[原网页](<http://dblab.xmu.edu.cn/blog/install-hadoop/>)

## Hadoop单机配置(非分布式)

Hadoop 默认模式为非分布式模式（本地模式），无需进行其他配置即可运行。非分布式即单 Java 进程，方便进行调试。

现在我们可以执行例子来感受下 Hadoop 的运行。Hadoop 附带了丰富的例子（运行 `./bin/hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar` 可以看到所有例子），包括 wordcount、terasort、join、grep 等。

在此我们选择运行 grep 例子，我们将 input 文件夹中的所有文件作为输入，筛选当中符合正则表达式 dfs[a-z.]+ 的单词并统计出现的次数，最后输出结果到 output 文件夹中。

```bash
cd /usr/local/hadoop
mkdir ./input
cp ./etc/hadoop/*.xml ./input   # 将配置文件作为输入文件
hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep ./input ./output 'dfs[a-z.]+'
cat ./output/*          # 查看运行结果
```

执行成功后如下所示，输出了作业的相关信息，输出的结果是符合正则的单词 dfsadmin 出现了1次

![Hadoop单机模式运行grep的输出结果](Hadoop.assets/1.png)Hadoop单机模式运行grep的输出结果

**注意**，Hadoop 默认不会覆盖结果文件，因此再次运行上面实例会提示出错，需要先将 `./output` 删除。

```bash
rm -r ./output
```

## Hadoop伪分布式配置

Hadoop 可以在单节点上以伪分布式的方式运行，Hadoop 进程以分离的 Java 进程来运行，节点既作为 NameNode 也作为 DataNode，同时，读取的是 HDFS 中的文件。

Hadoop 的配置文件位于 /usr/local/hadoop/etc/hadoop/ 中，伪分布式需要修改2个配置文件 **core-site.xml** 和 **hdfs-site.xml** 。Hadoop的配置文件是 xml 格式，每个配置以声明 property 的 name 和 value 的方式来实现。

修改配置文件 **core-site.xml**，将当中的

```xml
<configuration>
</configuration>
```

修改为下面配置：

```xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:///usr/local/hadoop/tmp</value>
        <description>Abase for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

同样的，修改配置文件 **hdfs-site.xml**：

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///usr/local/hadoop/tmp/dfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///usr/local/hadoop/tmp/dfs/data</value>
    </property>
</configuration>
```


> #### Hadoop配置文件说明
>
> Hadoop 的运行方式是由配置文件决定的（运行 Hadoop 时会读取配置文件），因此如果需要从伪分布式模式切换回非分布式模式，需要删除 core-site.xml 中的配置项。
>
> 此外，伪分布式虽然只需要配置 fs.defaultFS 和 dfs.replication 就可以运行（官方教程如此），不过若没有配置 hadoop.tmp.dir 参数，则默认使用的临时目录为 /tmp/hadoo-hadoop，而这个目录在重启时有可能被系统清理掉，导致必须重新执行 format 才行。所以我们进行了设置，同时也指定 dfs.namenode.name.dir 和 dfs.datanode.data.dir，否则在接下来的步骤中可能会出错。
>

配置完成后，执行 NameNode 的格式化:

```bash
hdfs namenode -format
```

成功的话，会看到 “successfully formatted” 和 “Exitting with status 0” 的提示，若为 “Exitting with status 1” 则是出错。

![执行namenode格式化](Hadoop.assets/2.png)执行namenode格式化

接着开启 NameNode 和 DataNode 守护进程（需要先开启ssh服务器）。

```bash
start-dfs.sh  #start-dfs.sh是个完整的可执行文件，中间没有空格
```

若出现如下SSH提示，输入yes即可。

![启动Hadoop时的SSH提示](Hadoop.assets/3.png)启动Hadoop时的SSH提示

> 启动时可能会出现如下 WARN 提示：WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform… using builtin-java classes where applicable WARN 提示可以忽略，并不会影响正常使用。
>

> 如果在这一步时提示 **Error: JAVA_HOME is not set and could not be found.** 的错误，先检查JAVA_HOME 环境变量有没有设置。
>
> ```
> echo $JAVA_HOME
> ```
>
> 如果已经设置，那么到hadoop的安装目录修改配置文件“/usr/local/hadoop/etc/hadoop/hadoop-env.sh”，在里面找到“export JAVA_HOME=${JAVA_HOME}”，然后，把它修改成JAVA安装路径的具体地址即可。

启动完成后，可以通过命令 `jps` 来判断是否成功启动，若成功启动则会列出如下进程: “NameNode”、”DataNode” 和 “SecondaryNameNode”（如果 SecondaryNameNode 没有启动，请运行 sbin/stop-dfs.sh 关闭进程，然后再次尝试启动尝试）。如果没有 NameNode 或 DataNode ，那就是配置不成功，请仔细检查之前步骤，或通过查看启动日志排查原因。

![通过jps查看启动的Hadoop进程](Hadoop.assets/4.png)通过jps查看启动的Hadoop进程



> #### Hadoop无法正常启动的解决方法
>
> 一般可以查看启动日志来排查原因，注意几点：
>
> - 启动时会提示形如 “DBLab-XMU: starting namenode, logging to /usr/local/hadoop/logs/hadoop-hadoop-namenode-DBLab-XMU.out”，其中 DBLab-XMU 对应你的机器名，但其实启动日志信息是记录在 /usr/local/hadoop/logs/hadoop-hadoop-namenode-DBLab-XMU.log 中，所以应该查看这个后缀为 **.log** 的文件；
> - 每一次的启动日志都是追加在日志文件之后，所以得拉到最后面看，对比下记录的时间就知道了。
> - 一般出错的提示在最后面，通常是写着 Fatal、Error、Warning 或者 Java Exception 的地方。
> - 可以在网上搜索一下出错信息，看能否找到一些相关的解决方法。
>
> 此外，**若是 DataNode 没有启动**，可尝试如下的方法（注意这会删除 HDFS 中原有的所有数据，如果原有的数据很重要请不要这样做）：
>
> ```bash
> # 针对 DataNode 没法启动的解决方法
> stop-dfs.sh   # 关闭
> rm -r ./tmp     # 删除 tmp 文件，注意这会删除 HDFS 中原有的所有数据
> hdfs namenode -format   # 重新格式化 NameNode
> start-dfs.sh  # 重启
> ```
>
> 成功启动后，可以访问 Web 界面 [http://localhost:50070](http://localhost:50070/) 查看 NameNode 和 Datanode 信息，还可以在线查看 HDFS 中的文件。
>



![Hadoop的Web界面](Hadoop.assets/5.png)Hadoop的Web界面

## 运行Hadoop伪分布式实例

上面的单机模式，grep 例子读取的是本地数据，伪分布式读取的则是 HDFS 上的数据。要使用 HDFS，首先需要在 HDFS 中创建用户目录：

```bash
hdfs dfs -mkdir -p /user/<user>
```

> #### 注意
>
> 教材《大数据技术原理与应用》的命令是以”./bin/hadoop dfs”开头的Shell命令方式，实际上有三种shell命令方式。
>
> 1. hadoop fs
> 2. hadoop dfs
> 3. hdfs dfs
>
> hadoop fs适用于任何不同的文件系统，比如本地文件系统和HDFS文件系统
> hadoop dfs只能适用于HDFS文件系统
> hdfs dfs跟hadoop dfs的命令作用一样，也只能适用于HDFS文件系统

接着将 ./etc/hadoop 中的 xml 文件作为输入文件复制到分布式文件系统中，即将 /usr/local/hadoop/etc/hadoop 复制到分布式文件系统中的 `/user/<user>/input` 中。hadoop文件系统默认工作目录就是 `/user/<user>`，因此在命令中就可以使用相对路径如 input，其对应的绝对路径就是 /user/hadoop/input:

```bash
hdfs dfs -mkdir input
hdfs dfs -put ./etc/hadoop/*.xml input
```

复制完成后，可以通过如下命令查看文件列表：

```bash
hdfs dfs -ls input
```

伪分布式运行 MapReduce 作业的方式跟单机模式相同，区别在于伪分布式读取的是HDFS中的文件（可以将单机步骤中创建的本地 input 文件夹，输出结果 output 文件夹都删掉来验证这一点）。

```bash
hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep input output 'dfs[a-z.]+'
```

查看运行结果的命令（查看的是位于 HDFS 中的输出结果）：

```bash
hdfs dfs -ls output    # 查看输出文件名
hdfs dfs -cat output/part-r-00000    # 查看输出文件内容
```

结果如下，注意到刚才我们已经更改了配置文件，所以运行结果不同。

![Hadoop伪分布式运行grep结果](Hadoop.assets/6.png)Hadoop伪分布式运行grep结果

我们也可以将运行结果取回到本地：

```bash
rm -r ./output    # 先删除本地的 output 文件夹（如果存在）
hdfs dfs -get output ./output     # 将 HDFS 上的 output 文件夹拷贝到本机
cat ./output/*
```

Hadoop 运行程序时，输出目录不能存在，否则会提示错误 “org.apache.hadoop.mapred.FileAlreadyExistsException: Output directory hdfs://localhost:9000/user/hadoop/output already exists” ，因此若要再次执行，需要执行如下命令删除 output 文件夹:

```bash
hdfs dfs -rm -r output    # 删除 output 文件夹
```

> #### 运行程序时，输出目录不能存在
>
> 运行 Hadoop 程序时，为了防止覆盖结果，程序指定的输出目录（如 output）不能存在，否则会提示错误，因此运行前需要先删除输出目录。在实际开发应用程序时，可考虑在程序中加上如下代码，能在每次运行时自动删除输出目录，避免繁琐的命令行操作：
>
> ```java
> Configuration conf = new Configuration();
> Job job = new Job(conf); 
> 
> /* 删除输出目录 */
> Path outputPath = new Path(args[1]);
> outputPath.getFileSystem(conf).delete(outputPath, true);
> ```
>

若要关闭 Hadoop，则运行

```bash
stop-dfs.sh
```

> #### 注意
>
> 下次启动 hadoop 时，无需进行 NameNode 的初始化，只需要运行 `start-dfs.sh` 就可以！