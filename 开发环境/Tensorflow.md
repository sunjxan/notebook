```
pip3 install tensorflow
```

```
# 查看版本
import tensorflow as tf
print(tf.__version__)

# 查看GPU和CUDA支持
print(tf.test.is_gpu_available())
print(tf.test.is_built_with_gpu_support())
print(tf.test.is_built_with_cuda())

# 查看电脑GPU和CPU
print(tf.config.list_logical_devices())
print(tf.config.list_physical_devices())
print(tf.config.get_visible_devices())
import os
from tensorflow.python.client import device_lib
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "99"
print(device_lib.list_local_devices())

# 示例
with tf.device('/CPU:0'):
    a = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0],shape=[2,3])
    b = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0],shape=[3,2])
    c = tf.matmul(a,b)
    print(c)
```

