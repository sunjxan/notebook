### 编写Spark程序使用Flume数据源

1. 在flume/conf目录下创建 avro.conf 配置文件

```
a1.sources = r1
a1.sinks = k1
a1.channels = c1

a1.sources.r1.type = exec
a1.sources.r1.command = tail -F <日志文件路径>
 
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100

a1.sinks.k1.type = avro
a1.sinks.k1.hostname = localhost
a1.sinks.k1.port = 9091
 
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1
```

2. 启动flume

```
flume-ng agent -c flume/conf -f flume/conf/avro.conf -n a1 -Dflume.root.logger=INFO,console >/dev/null 2>&1 &
```

3. 在 https://search.maven.org 搜索spark-streaming-flume-assembly包下载，放到spark/jars目录下，版本号与spark-streaming.jar相应

4. 新建以下python文件并执行：

```python
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

spark = SparkSession.builder.master("yarn").appName("test").enableHiveSupport().getOrCreate()
sc = spark.sparkContext
ssc = StreamingContext(sc, 2)

stream = FlumeUtils.createStream(ssc, 'localhost', 9091)
lines = stream.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint()

ssc.start()
ssc.awaitTermination()
```


### 编写Spark程序使用Kafka数据源

1. 在 https://search.maven.org 搜索spark-streaming-kafka-0-8-assembly包下载，放到spark/jars目录下，版本号与spark-streaming.jar相应
2. 新建以下python文件并执行：

```python
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

spark = SparkSession.builder.master("yarn").appName("test").enableHiveSupport().getOrCreate()
sc = spark.sparkContext
ssc=StreamingContext(sc, 2)

stream = KafkaUtils.createDirectStream(ssc, ["<topic名>"], {"metadata.broker.list": "localhost:9092"})
lines = stream.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint()

ssc.start()
ssc.awaitTermination()
```

