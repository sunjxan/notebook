[原网页](<http://dblab.xmu.edu.cn/blog/install-storm/>)

```
cd /usr/local
# 下载安装包（http://storm.apache.org/downloads.html）
sudo wget https://mirrors.tuna.tsinghua.edu.cn/apache/storm/apache-storm-2.1.0/apache-storm-2.1.0.tar.gz
# 解压
sudo tar -xvf apache-storm-2.1.0.tar.gz
sudo mv apache-storm-2.1.0 storm

# 设置环境变量，在~/.zshrc追加
export STORM_HOME="/usr/local/storm"
export PATH="${STORM_HOME}/bin:$PATH"

# 生效
source ~/.zshrc

# 查看版本
storm version

# 因为在storm中很多操作需要文件所有者权限，所以需要更改storm目录所有者
sudo chown -R <user>:<user> /usr/local/storm

# 修改配置
cd storm
# 修改conf/storm-env.sh，修改JAVA_HOME
export JAVA_HOME="/usr/local/jdk"

# 启动
storm nimbus
# 查看运行情况
storm list
```