1. 下载数据（https://grouplens.org/datasets/movielens/），并解压，得到一系列csv文件或者dat文件；
2. 修改配置my.cnf文件，添加文件目录：
```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

# 在[mysqld]后添加
secure_file_priv = <csv文件目录>
# 重启mysql服务即可生效
```
3. 创建表：
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

4. 加载csv文件到MySQL：
```
LOAD DATA INFILE 'movies.csv'
INTO TABLE movie CHARACTER SET latin1
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE 'links.csv'
INTO TABLE link CHARACTER SET latin1
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(movieId, imdbId, @tmdbId) SET tmdbId = NULLif(@tmdbId,'');

LOAD DATA INFILE 'ratings.csv'
INTO TABLE rating CHARACTER SET latin1
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE 'tags.csv'
INTO TABLE tag CHARACTER SET latin1
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
```

或者加载dat文件到MySQL：

```
LOAD DATA INFILE 'movies.dat'
INTO TABLE movie CHARACTER SET latin1
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'links.dat'
INTO TABLE link CHARACTER SET latin1
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n'
(movieId, imdbId, @tmdbId) SET tmdbId = NULLif(@tmdbId,'');

LOAD DATA INFILE 'ratings.dat'
INTO TABLE rating CHARACTER SET latin1
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'tags.dat'
INTO TABLE tag CHARACTER SET latin1
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';
```

6. 开启hadoop；
7. 启动mysql服务；
8. sqoop测试：
```
sqoop list-databases --connect jdbc:mysql://<服务器IP>:3306 --username root -P
```
9. 在hive中创建数据库：
```
create database if not exists movielens location '/user/hive/warehouse/movielens.db/';
```
10. 全量导入movie、link：
```
sqoop import --connect jdbc:mysql://<服务器IP>:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> -m 1 --hive-import --hive-database <hive数据库名> --hive-table <hive表名>
```

11. 增量导入rating、tag：
```
sqoop import --connect jdbc:mysql://<服务器IP>:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> --m 1 --target-dir /user/hive/warehouse/movielens.db/<hive表名> --incremental append --check-column <递增列名> --last-value <上次导入的最新值（首次导入写0）>
```

12. 设置定时执行：
```
# 安装cron
sudo apt install cron
# 设置
crontab -e

0 1 * * * /root/import.sh

# 启动
sudo service cron start
```

