1. 启动hbase

2. 开启thrift通讯端口

```
hbase thrift start >/dev/null 2>&1 &
```

3.  安装happybase

```
pip3 install happybase
```

4. 使用python操作hbase
```
import happybase

# 创建连接
hostname = 'localhost'
tablename = 'test'
rowname = 'x'
columnname = 'y'

conn = happybase.Connection(hostname)

# 读取表列表
print(conn.tables())

# 获取表
table = conn.table(tablename)

# 获取行，得到一个字典
row = table.row(rowname)

# 获取值
print(table.cells(rowname, columnname))

conn.close()
```