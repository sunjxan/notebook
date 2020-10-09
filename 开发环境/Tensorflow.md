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
```

## 基础知识

### 生成张量

```
x = tf.zeros((3, 4))
y = tf.ones((3, 4))
z = tf.random.normal((3, 4))
x2 = tf.zeros_like(x)
y2 = tf.ones_like(y)
a = tf.fill((2,3), 5)
b = tf.range(0, 20)
```

### 张量属性

```
# 维数
x.ndim
# 维度
x.shape
# 数据
x.numpy()
# 数据类型
x.dtype
# 转置
tf.transpose(x)
```

### 改变形状

```
x2 = tf.reshape(x, (2, 6))
```

### 初始化函数

```
# 创建初始化器
initializer = keras.initializers.zeros()

# 初始化器生产张量
a = initializer(dtype=tf.float32, shape=(1,2))

initializer = keras.initializers.glorot_normal()
b= initializer(dtype=tf.float32, shape=(1,2))
```

### 创建张量

```
initializer = keras.initializers.zeros()
a = initializer(dtype=tf.float32, shape=(1,2))

# 常量
b = tf.constant(a, dtype=tf.float32, shape=(1,2))

# 变量
c = tf.Variable(a, dtype=tf.float32, shape=(1,2))
```

### 自动求导

```
# 变量能被自动求导机制求导
a = tf.Variable(initial_value=[[2, 3]], dtype=tf.float32, shape=(1,2))
b = tf.Variable(initial_value=[[5], [6]], dtype=tf.float32, shape=(2, 1))
# 记录计算过程
with tf.GradientTape() as tape:
    c = tf.matmul(a, b)
# 求导
d, e = tape.gradient(c, [a, b])
print(c, d ,e)
```

## 神经网络

```
import tensorflow.nn as nn
import tensorflow.keras as keras
keras.__version__
```

### 神经元层

```
# units 包含神经元数
# input_dim 每个神经元输入数
# use_bias 是否有偏置项
layer = keras.layers.Dense(units, input_dim, use_bias=True, name, activation=None, kernel_initializer='glorot_uniform', bias_initializer=keras.initializers.zeros)

# 计算
X = tf.constant([[1, 1, 1]])
y = layer(X)

# 权重和偏置（计算后生成）
layer.weights

# 激活
z = nn.sigmoid(y)
z = nn.softmax(y)
```

### 模型堆叠

```
model = keras.Sequential([
  keras.layers.Dense(2, input_dim=4, activation='sigmoid'),
  keras.layers.Dense(3, input_dim=2),
  keras.layers.Activation(nn.softmax)
])
X = tf.constant([[1, 1, 1, 1]])
y = model(X)
```

### 模型子类化

```
class MyModel(keras.Model):
  def __init__(self):
    super().__init__()
    self.dense1 = keras.layers.Dense(2, input_dim=4, activation='sigmoid', kernel_initializer='glorot_uniform', bias_initializer='glorot_uniform'
    self.dense2 = keras.layers.Dense(3, input_dim=2, activation='softmax', kernel_initializer='glorot_uniform', bias_initializer='glorot_uniform')

  def call(self, inputs):
    x = self.dense1(inputs)
    x = self.dense2(x)
    return x

model = MyModel()

X = tf.constant([[1, 1, 1, 1]])
y = model(X)

# 查看模型层
model.layers
# 查看模型权重和偏置
model.weights
```

### 损失函数

```
# 为批量计算的数据求损失，再平均
# 损失函数(标签值, 预测值)
loss = tf.reduce_mean(keras.losses.MSE(tf.constant([[1., 2.]]), tf.constant([[2., 4.]])))
```

### 反向传播

```
class MyModel(keras.Model):
  def __init__(self):
    super().__init__()
    self.dense = keras.layers.Dense(2, input_dim=3, kernel_initializer='zeros', bias_initializer='zeros')

  def call(self, inputs):
    return self.dense(inputs)

model = MyModel()

X = tf.constant([[1., 1., 1.], [2., 2., 2.]])
y = tf.constant([[2., 3.], [4., 6.]])

with tf.GradientTape() as tape:
  # 计算预测值
  y_pred = model(X)
  # 计算损失
  loss = tf.reduce_mean(keras.losses.MSE(y, y_pred))
# 计算梯度
grads = tape.gradient(loss, model.variables)

# 打印损失
print(loss)
# 打印梯度
for grad in grads:
  print(grad)
```

### 优化器

```
# 创建优化器
optimizer = keras.optimizers.SGD(5e-4)
# 计算梯度
grads = tape.gradient(loss, model.variables)
# 更新参数
optimizer.apply_gradients(zip(grads, model.variables))
```

### 迭代更新

```
optimizer = keras.optimizers.SGD(5e-4)

# 迭代次数
num_batches = 100
for batch_index in range(num_batches):
  with tf.GradientTape() as tape:
    y_pred = model(X)
    loss = tf.reduce_mean(keras.losses.MSE(y, y_pred))
  grads = tape.gradient(loss, model.variables)
  optimizer.apply_gradients(zip(grads, model.variables))

print(loss)
for grad in grads:
  print(grad)
```

### 评估器

```
# 创建准确度评估器
metrics = keras.metrics.Accuracy()
# 重置状态
metrics.reset_states()
# 评估函数(标签值, 预测值)
metrics.update_state([0, 1, 2], [0, 0, 2])
print('%.4f' % metrics.result())
```

### 基本流程

```
# 1.打印模型概要
model.summary()

# 2.编译
model.compile(optimizer=keras.optimizers.SGD(5e-4), loss=keras.losses.MSE, metrics=keras.metrics.MSE)

# 3.训练，返回历史信息model.history，包含params、epoch、history属性
# batch_size 每次批量计算，批量的大小，同一批次内数据不重复，一次计算，一个损失函数值，每个参数更新一次
# steps_per_epoch 从数据中顺序取批次，步骤的次数，各个步骤间数据不重复，最后一步数据可能小于batch_size
# epochs 遍历所有数据轮回数是epochs减去initial_epoch
# shuffle 每次遍历所有数据前，是否对数据随机排序
model.fit(X_train, y_train, batch_size=1, steps_per_epoch=None, initial_epoch=0, epochs=1, shuffle=True)

# 4.评估，返回loss函数值和metrics函数值
model.evaluate(X_test, y_test, batch_size=None, steps=None)

# 5.预测，返回预测值
model.predict(X, batch_size=None, steps=None)
```

### BatchNormalization

```
x = keras.layers.BatchNormalization(axis, epsilon=1e-5, momentum=.1)(x)
```

### Dropout

```
x = nn.dropout(x, rate=.2)
```

## 卷积神经网络CNN

### 加载数据

```
# 加载MNIST数据，训练数据60000张28*28的灰度值图片，测试数据10000张28*28的灰度值图片
(train_data, train_labels), (test_data, test_labels) = keras.datasets.mnist.load_data()

# 显示图片
import matplotlib.pyplot as plt
plt.imshow(train_data[0], cmap="gray")
plt.show()
```

### 数据分批

```
# 一个epoch内，不同batch间、一个batch内数据都不重复，所有数据都计算一次

import numpy as np

class MNISTLoader():
  def __init__(self, batch_size=1, shuffle=False, train=True):
    (self.train_data, self.train_labels), (self.test_data, self.test_labels) = keras.datasets.mnist.load_data()
    # MNIST中的图像默认为uint8（0-255的数字），以下代码将其归一化到0-1之间的浮点数，并在最后增加一维作为颜色通道
    if train:
      self.train_data = np.expand_dims(self.train_data.astype(np.float32) / 255.0, axis=-1)      # [60000, 28, 28, 1]
      self.train_labels = self.train_labels.astype(np.int32)      # [60000]
      self.X = self.train_data
      self.y = self.train_labels
    else:
      self.test_data = np.expand_dims(self.test_data.astype(np.float32) / 255.0, axis=-1)        # [10000, 28, 28, 1]
      self.test_labels = self.test_labels.astype(np.int32)      # [10000]
      self.X = self.test_data
      self.y = self.test_labels
    self.size = len(self.y)
    self.batch_size = batch_size
    self.shuffle = shuffle

  def __iter__(self):
    if self.shuffle:
      # 随机排序
      L = list(range(self.size))
      np.random.shuffle(L)
      self.X = self.X[L]
      self.y = self.y[L]
    # 返回生成器
    return self._get_batch()
    
  def _get_batch(self):
    # 将数据集切分成多个batch并返回
    index = 0
    while index < self.size:
        # 封装成对
        yield [self.X[index : index + self.batch_size], self.y[index : index + self.batch_size]]
        index += self.batch_size
    return

train_loader = MNISTLoader(batch_size=100, shuffle=True)
# 训练数据生成器
iter(train_loader)

test_loader = MNISTLoader(batch_size=100, shuffle=True, train=False)
# 测试数据生成器
iter(test_loader)
```

### 建立模型

```
class CNNModel(keras.Model):
  def __init__(self):
    super().__init__()
    self.conv1 = tf.keras.layers.Conv2D(filters=10, kernel_size=(5, 5), strides=(1, 1), padding='same', activation='relu')
    self.pool = tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2))
    self.conv2 = tf.keras.layers.Conv2D(filters=20, kernel_size=(5, 5), strides=(1, 1), padding='same', activation='relu')
    self.flatten = keras.layers.Flatten()
    # 经过两次池化后得到的矩阵大小为(28/2/2, 28/2/2)
    self.dense1 = keras.layers.Dense(50, input_dim=20*7*7, activation='relu')
    self.dense2 = keras.layers.Dense(10, input_dim=50, activation='softmax')

  def call(self, inputs):
    x = self.conv1(inputs)
    x = self.pool(x)
    x = self.conv2(x)
    x = self.pool(x)
    x = self.flatten(x)
    x = self.dense1(x)
    x = self.dense2(x)
    return x

# [batch_size, width, height, 1]
model = CNNModel()
```

### 交叉熵损失

```
# SparseCategoricalCrossentropy函数直接处理
criterion = keras.losses.SparseCategoricalCrossentropy()
criterion([0, 1], [[.5, .5], [.5, .5]])

# CategoricalCrossentropy函数需要先对数据做one hot编码
criterion = keras.losses.CategoricalCrossentropy()
criterion([[1, 0], [0, 1]], [[.5, .5], [.5, .5]])
criterion(tf.one_hot([0, 1], 2), [[.5, .5], [.5, .5]])
```

### 训练模型

```
criterion = keras.losses.SparseCategoricalCrossentropy()
optimizer = keras.optimizers.SGD(5e-4)

epochs = 10
for epoch_index in range(epochs):
  train_iter = iter(train_loader)
  for X, y in train_iter:
    with tf.GradientTape() as tape:
      y_pred = model(X)
      loss = criterion(y, y_pred)
    grads = tape.gradient(loss, model.variables)
    optimizer.apply_gradients(zip(grads, model.variables))
```

### 交叉熵评估

```
# SparseCategoricalCrossentropy评估器直接处理
metrics = keras.metrics.SparseCategoricalCrossentropy()
metrics.update_state([0, 1], [[.5, .5], [.5, .5]])
print('%.4f' % metrics.result())

# CategoricalCrossentropy评估器需要先对数据做one hot编码
metrics = keras.metrics.CategoricalCrossentropy()
metrics.update_state([[1, 0], [0, 1]], [[.5, .5], [.5, .5]])
print('%.4f' % metrics.result())

metrics.reset_states()
metrics.update_state(tf.one_hot([0, 1], 2), [[.5, .5], [.5, .5]])
print('%.4f' % metrics.result())
```

### 评估模型

```
# 交叉熵准确度评估器
metrics = keras.metrics.SparseCategoricalAccuracy()

test_iter = iter(test_loader)
for X, y in test_iter:
  y_pred = model(X)
  metrics.update_state(y, y_pred)

print('%.4f' % metrics.result())
```

### 使用封装流程

```
model.compile(optimizer=keras.optimizers.SGD(5e-4), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=keras.metrics.SparseCategoricalAccuracy())

model.fit(train_loader.train_data, train_loader.train_labels, batch_size=100, epochs=10, shuffle=True)

model.evaluate(test_loader.test_data, test_loader.test_labels, batch_size=100)
```

