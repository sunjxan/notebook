```
cd /usr/local
# 下载安装包（https://flink.apache.org/downloads.html）
sudo wget http://www.trieuvan.com/apache/flink/flink-1.10.1/flink-1.10.1-bin-scala_2.12.tgz
# 解压
sudo tar -xvf flink-1.10.1-bin-scala_2.12.tgz
sudo mv flink-1.10.1 flink

# 设置环境变量，在~/.zshrc追加
export FLINK_HOME="/usr/local/flink"
export PATH="${FLINK_HOME}/bin:$PATH"

# 生效
source ~/.zshrc

# 查看版本
flink -v

# 因为在flink中很多操作需要文件所有者权限，所以需要更改flink目录所有者
sudo chown -R <user>:<user> /usr/local/flink
```

[原网页](<http://dblab.xmu.edu.cn/blog/2507-2/>)

使用如下命令启动Flink：

```bash
start-cluster.sh
```

使用jps命令查看进程：

```
$ jps
17942 TaskManagerRunner
18022 Jps
17503 StandaloneSessionClusterEntrypoint
```

如果能够看到TaskManagerRunner和StandaloneSessionClusterEntrypoint这两个进程，就说明启动成功。
Flink的JobManager同时会在8081端口上启动一个Web前端，可以在浏览器中输入“http://localhost:8081”来访问。
Flink安装包中自带了测试样例，这里可以运行WordCount样例程序来测试Flink的运行效果，具体命令如下：

```bash
flink run /usr/local/flink/examples/batch/WordCount.jar
```

执行上述命令以后，如果执行成功，应该可以看到类似如下的屏幕信息：

```
Starting execution of program
Executing WordCount example with default input data set.
Use --input to specify file input.
Printing result to stdout. Use --output to specify output path.
(a,5)
(action,1)
(after,1)
(against,1)
(all,2)
……
```