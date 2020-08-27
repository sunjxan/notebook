```
cd /usr/local
# 下载安装包（http://www.apache.org/dyn/closer.lua/sqoop/）
sudo wget https://downloads.apache.org/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
# 解压
sudo tar -xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
sudo mv sqoop-1.4.7.bin__hadoop-2.6.0 sqoop

# 因为在sqoop中很多操作需要文件所有者权限，所以需要更改sqoop目录所有者
sudo chown -R <user>:<user> /usr/local/sqoop

# 复制jar包
cp /usr/local/hive/lib/hive-common-2.3.7.jar  /usr/local/sqoop/lib

# 修改配置
cd sqoop
cat conf/sqoop-env-template.sh  >> conf/sqoop-env.sh
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
source ~/.zshrc

# 查看版本
sqoop version
```

[原网页](<http://dblab.xmu.edu.cn/blog/install-sqoop1/>)

### 配置MySQL

下载jdbc驱动（<https://dev.mysql.com/downloads/connector/j/>  Platform Independent）

```
cd /usr/local/sqoop
sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.20.tar.gz

# 解压
sudo tar -xvf mysql-connector-java-8.0.20.tar.gz
# 移动到lib目录
sudo mv mysql-connector-java-8.0.20/mysql-connector-java-8.0.20.jar lib

# 启动MySQL服务
sudo service mysql start

# 登录mysql
# 创建远程访问用户（在mysql.user表）
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '<root密码>' WITH GRANT OPTION;
# 刷新权限，使其生效
FLUSH PRIVILEGES;

# 测试连接MySQL，服务器ip不可以写作localhost或127.0.0.1
sqoop list-databases --connect jdbc:mysql://<服务器IP>:3306/ --username root -P

# 登录mysql
# 创建远程访问用户（在mysql.user表）
GRANT ALL PRIVILEGES ON *.* TO 'hive'@'localhost' IDENTIFIED BY '<hive密码>' WITH GRANT OPTION;
# 刷新权限，使其生效
FLUSH PRIVILEGES;

# 测试连接MySQL，localhost不可以写作服务器IP
sqoop list-databases --connect jdbc:mysql://localhost:3306/ --username hive -P
```

[原网页](http://dblab.xmu.edu.cn/blog/1059-2/)

### 将数据从MySQL导入Hive

1. 启动Hadoop、MySQL服务
2. 从MySQL导入文件：
```
sqoop import --connect jdbc:mysql://<服务器IP>:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> -m 1 --target-dir '<hdfs路径>' --fields-terminated-by '<分割字符>'
```
3. 创建hive表：
```
CREATE TABLE <表名>(
)
row format delimited fields terminated by '<分割字符>';
```
4. 导入数据到hive表：
```
load data inpath '<hdfs路径>' overwrite into table <表名>;
```
5. 一条命令导入到hive表：
```
sqoop import --connect jdbc:mysql://<服务器IP>:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> -m 1 --fields-terminated-by '<分割字符>' --hive-import --hive-database <hive数据库名> --hive-table <hive表名>
```

### 将数据从Hive导入MySQL

1. 启动Hadoop、MySQL服务
2. 创建mysql表；
3. 从hdfs导出文件：
```
sqoop export --connect jdbc:mysql://<服务器IP>:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> --export-dir '<hdfs路径>'
```

### 将数据从MySQL导入HBase

1. 启动Hadoop、MySQL、HBase服务
2. 创建hbase表：
```
CREATE TABLE <表名>(
)
row format delimited fields terminated by '<分割字符>';
```
3. 导入到hbase表：
```
sqoop import --connect jdbc:mysql://<服务器IP>:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> -m 1 --hbase-table <hbase表名> --column-family <列族名> --hbase-row-key <行键名>
```

### 增量导入--append方式导入

```
# 用于自增的数字id列

--incremental append
--check-column <检查列名>
--last-value <不导入的数据该列的最大数值>
```

### 增量导入--lastmodified方式导入

```
# 用于更新的日期列

--incremental lastmodified
--append
--check-column <检查列名>
--last-value <不导入的数据该列的最新日期>


--incremental lastmodified
--merge-key <按照合并列名>
--check-column <检查列名>
--last-value <不导入的数据该列的最新日期>
# 先将之前导入的所有数据中，如果有被修改的数据行,按照指定的列名合并
# 然后将比指定日期新的数据中,之前没有导入的部分,插入表中
```