```
# 安装MySQL
sudo apt install mysql-server mysql-client

# 查看是否安装成功
sudo netstat -anp | grep mysql
# 或者
sudo ps aux | grep mysql

# 启动
sudo service mysql start
# 关闭
sudo service mysql stop
# 重启
sudo service mysql restart

# 登录MySQL（root初始密码为空）
sudo mysql -u root -p

# 修改root密码
sudo mysqladmin -u root -p password

# 取消本地监听
# 正常情况下，mysql占用的3306端口只是在IP 127.0.0.1上监听，拒绝了其他IP的访问（通过netstat可以查看到）。取消本地监听需要修改 my.cnf 文件（包含其引用的文件）
sudo vim /etc/mysql/my.cnf
# 找到如下内容，并注释
bind-address = 127.0.0.1
#设置字符集、排序规则等，在[mysqld]后添加
character-set-server = utf8
# 重启mysql服务即可生效

# 登录mysql
# 创建远程访问用户（在mysql.user表）
GRANT ALL PRIVILEGES ON *.* TO '<用户名>'@'%' IDENTIFIED BY '<访问密码>' WITH GRANT OPTION;
# 刷新权限，使其生效
FLUSH PRIVILEGES;
```