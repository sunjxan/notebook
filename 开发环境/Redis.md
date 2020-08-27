[原网页](<http://dblab.xmu.edu.cn/blog/1513/>)

```
cd /usr/local
# 下载安装包（https://redis.io/download）
sudo wget http://download.redis.io/releases/redis-6.0.6.tar.gz?_ga=2.29894655.1724214317.1597470186-1104984266.1597182549
# 解压
sudo tar -xvf redis-6.0.6.tar.gz
sudo mv redis-6.0.6 redis

# 因为在redis中很多操作需要文件所有者权限，所以需要更改redis目录所有者
sudo chown -R <user>:<user> /usr/local/redis

# 编译
cd redis
sudo make
sudo make install

# 查看版本
redis-server --version

# 启动服务器
redis-server >/dev/null 2>&1 &
# 打开客户端
redis-cli
```