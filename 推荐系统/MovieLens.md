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

CREATE TABLE user(
  userId INT,
  gender CHAR(1),
  age INT,
  occupation INT,
  zip_code VARCHAR(20)
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

CREATE TABLE genome_score(
  movieId INT,
  tagId INT,
  relevance FLOAT
);

CREATE TABLE genome_tag(
  tagId INT,
  tag VARCHAR(1000)
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

LOAD DATA INFILE 'genome-scores.csv'
INTO TABLE genome_score CHARACTER SET latin1
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE 'genome-tags.csv'
INTO TABLE genome_tag CHARACTER SET latin1
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
```

5. 加载dat文件到MySQL：
```
LOAD DATA INFILE 'movies.dat'
INTO TABLE movie CHARACTER SET latin1
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'users.dat'
INTO TABLE user CHARACTER SET latin1
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'ratings.dat'
INTO TABLE rating CHARACTER SET latin1
FIELDS TERMINATED BY '::' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\n';
```

6. 开启hadoop；
7. 启动mysql服务；
8. 从mysql导入表到hive中：
```
sqoop import --connect jdbc:mysql://localhost:3306/<数据库> --driver com.mysql.cj.jdbc.Driver --username root --password <root密码> --table <表名> --hive-import --create-hive-table --num-mappers 1 --fields-terminated-by '\t';
```

9. 在pyspark中读取表