1. 下载数据（https://grouplens.org/datasets/movielens/），并解压，得到一系列csv文件或者dat文件；
2. 修改配置my.cnf文件，添加文件目录：
```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

# 在[mysqld]后添加
secure_file_priv = <csv文件目录>
# 重启mysql服务即可生效
```
3. 启动mysql服务；
4. 创建数据库：
```
CREATE DATABASE movielens;
USE movielens;
```
5. 创建表：
```
CREATE TABLE movie(
  movieId INT,
  title VARCHAR(200),
  genres VARCHAR(200)
);

CREATE TABLE link(
  movieId INT,
  imdbId INT,
  tmdbId INT
);

CREATE TABLE rating(
  userId INT,
  movieId INT,
  rating FLOAT,
  timestamp INT
);

CREATE TABLE tag(
  userId INT,
  movieId INT,
  tag VARCHAR(1000),
  timestamp INT
);
```

6. 加载csv文件到MySQL：
```
LOAD DATA INFILE '<csv文件目录>/movies.csv'
INTO TABLE movie 
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE '<csv文件目录>/links.csv'
INTO TABLE link
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(movieId, imdbId, @tmdbId) SET tmdbId = NULLif(@tmdbId,'');

LOAD DATA INFILE '<csv文件目录>/ratings.csv'
INTO TABLE rating
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE '<csv文件目录>/tags.csv'
INTO TABLE tag
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
```

或者加载dat文件到MySQL：

```
LOAD DATA INFILE '<csv文件目录>/movies.dat'
INTO TABLE movie
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE '<csv文件目录>/links.dat'
INTO TABLE link
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n'
(movieId, imdbId, @tmdbId) SET tmdbId = NULLif(@tmdbId,'');

LOAD DATA INFILE '<csv文件目录>/ratings.dat'
INTO TABLE rating
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE '<csv文件目录>/tags.dat'
INTO TABLE tag
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';
```

7. 开启hadoop；
8. sqoop测试：
```
sqoop list-tables --connect jdbc:mysql://<服务器IP>:3306/movielens --username root -P
```
9. 在hive中创建数据库：
```
create database if not exists movielens;
```
10. 全量导入：
```
sqoop import --connect jdbc:mysql://<服务器IP>:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> -m 1 --fields-terminated-by '<分割字符>' --hive-import --hive-drop-import-delims --hive-database <hive数据库名> --hive-table <hive表名>
```

11. 增量导入：
```
sqoop import --connect jdbc:mysql://<服务器IP>:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> -m 1 --hive-import --hive-drop-import-delims --hive-database <hive数据库名> --hive-table <hive表名> --incremental append --check-column <递增列名> --last-value <不导入的数据该列的最大数值（首次导入写0）>
```

12. 使用脚本循环执行：
```
time=`date +"%Y-%m-%d %H:%M:%S"" -d "-1day"`
declare -A check
check=([<表名>]=<元组名> [<表名>]=<元组名> [<表名>]=<元组名>)
declare -A merge
merge=([<表名>]=<元组名> [<表名>]=<元组名> [<表名>]=<元组名>)

for k in ${!check[@]}
do
    sqoop import \
        ...
        --incremental lastmodified \
        --check-column ${check[$k]} \
        --merge-key ${merge[$k]} \
        --last-value ${time}
done
```

13. 设置定时执行：
```
# 安装cron
sudo apt install cron
# 启动
sudo service cron start
# 设置
crontab -e
```

输入的格式：

```python
* * * * * 要执行的命令
----------------
| | | | |
| | | | ---- 周当中的某天 (0 - 7) (周日为 0 或 7)
| | | ------ 月份 (1 - 12)
| | -------- 一月当中的某天 (1 - 31)
| ---------- 小时 (0 - 23)
------------ 分钟 (0 - 59)

# 如
### 每隔 5 分钟运行一次 backupscript 脚本 ##
*/5 * * * * /root/backupscript.sh
### 每天的凌晨 1 点运行 backupscript 脚本 ##
0 1 * * * /root/backupscript.sh
### 每月的第一个凌晨 3:15 运行 backupscript 脚本 ##
15 3 1 * * /root/backupscript.sh
```

我们在这里可以选择定时每隔半小时增量导入一次

```
*/30 * * * * /root/project/scripts/import.sh
```