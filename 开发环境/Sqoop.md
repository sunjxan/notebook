```
cd /usr/local
# 下载安装包（http://www.apache.org/dyn/closer.lua/sqoop/）
sudo wget https://downloads.apache.org/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
# 解压
sudo tar -xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
sudo mv sqoop-1.4.7.bin__hadoop-2.6.0 sqoop

# 修改配置
cd sqoop/conf
sudo cat sqoop-env-template.sh  >> sqoop-env.sh
# 修改 sqoop-env.sh，追加
export HADOOP_COMMON_HOME=/usr/local/hadoop
export HADOOP_MAPRED_HOME=/usr/local/hadoop
export HBASE_HOME=/usr/local/hbase
export HIVE_HOME=/usr/local/hive
export ZOOCFGDIR=/usr/local/zookeeper

# 设置环境变量，在~/.zshrc追加
export SQOOP_HOME="/usr/local/sqoop"
export PATH="${SQOOP_HOME}/bin:$PATH"
export CLASSPATH="${SQOOP_HOME}/lib:$CLASSPATH"

# 生效
source .zshrc

#查看版本
sqoop version

# 因为在sqoop中很多操作需要文件所有者权限，所以需要更改sqoop目录所有者
sudo chown -R <user> /usr/local/sqoop
```

[原网页](<http://dblab.xmu.edu.cn/blog/install-sqoop1/>)

### 配置MySQL

下载jdbc驱动（<https://dev.mysql.com/downloads/connector/j/>）

```
cd /usr/local/sqoop
sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.20.tar.gz

# 解压
sudo tar -xvf mysql-connector-java-8.0.20.tar.gz
# 移动到lib目录
sudo mv mysql-connector-java-8.0.20/mysql-connector-java-8.0.20.jar lib

# 启动MySQL服务
sudo service mysql start
# 测试连接MySQL
sqoop list-databases --connect jdbc:mysql://127.0.0.1:3306/ --username root -P
```

[原网页](<http://dblab.xmu.edu.cn/blog/1059-2/>)

### 使用Sqoop将数据从Hive导入MySQL

1. 启动Hadoop、MySQL服务

2. 将前面生成的临时表数据从Hive导入到 MySQL 中


```bash
## export表示数据从 hive 复制到 mysql 中
sqoop export --connect jdbc:mysql://localhost:3306/<数据库> --username root --password <root密码> --table <相同结构的表> --export-dir '/user/hive/warehouse/word_count' --fields-terminated-by '\t';
```
