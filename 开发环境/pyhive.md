1. 启动hiveserver2，使其他服务可以通过thrift接入hive
```
# 在hadoop的core-site.xml文件中配置hadoop代理用户，configuration中添加
<property>
  <name>hadoop.proxyuser.root.groups</name>
  <value>*</value>
</property>
<property>
  <name>hadoop.proxyuser.root.hosts</name>
  <value>*</value>
</property>
# 设置完后，需要重启hadoop
# 启动hiveserver2
hive --service hiveserver2 >/dev/null 2>&1 &
```

2. 安装pyhive

```
sudo apt install libsasl2-dev

pip3 install thrift-sasl
pip3 install pyhive
```

3. 使用python操作pyhive
```
from pyhive import hive

conn = hive.Connection(host='localhost', port=10000, username='root', password='root', database='test', auth="CUSTOM")
cursor = conn.cursor()
cursor.execute('show tables')
for result in cursor.fetchall():
    print(result)
conn.close()
```