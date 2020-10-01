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

# 安装python包
pip3 install redis
```

```
import redis

# 连接
r = redis.StrictRedis(host='localhost', port=6379)
# 兼容连接
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# 连接池
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# 键值对
r.set('foo', 'bar')
r.get('foo')

# 添加列表
r.lpush('list', 1, 2, 3)
r.llen('list')
r.lrange('list', 0, -1)

# 添加集合
r.sadd('set', 1, 2, 3)
r.scard('set')
r.smembers('set')

# 添加字典
r.zadd('dict', {'a': 1, 'b': 2, 'c': 3})
r.zcard('dict')
r.zrange('dict', 0, -1, withscores=True)
```

