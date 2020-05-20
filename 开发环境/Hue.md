[原网页](<http://dblab.xmu.edu.cn/blog/1892/>)

```
# 确保hadoop,hive,mysql,python,git,maven,java的安装
# 安装依赖库和依赖工具
sudo apt install aptitude
# 使用aptitude安装
sudo aptitude install libkrb5-dev libxml2-dev libffi-dev libxslt-dev libsqlite3-dev libssl-dev libldap2-dev libkrb5-dev libmysqlclient-dev libmysql-java libsasl2-dev libsasl2-modules-gssapi-mit libtidy-dev libgmp3-dev

# 安装
cd /usr/local
# 下载安装包（https://docs.gethue.com/releases/）
sudo wget https://cdn.gethue.com/downloads/hue-4.7.0.tgz
# 解压
sudo tar -xvf hue-4.7.0.tgz
sudo mv hue-4.7.0 hue

# 编译
cd hue
make apps

# 查看版本
build/env/bin/hue version

# 因为在hue中很多操作需要文件所有者权限，所以需要更改hue目录所有者
sudo chown -R <user> /usr/local/hue

# 启动hadoop和hive
start-dfs.sh
hive --service hiveserver2
# 启动服务（http://localhost:8000）,创建账号
build/env/bin/hue runserver
```


