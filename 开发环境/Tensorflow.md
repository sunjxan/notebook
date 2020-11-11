```
pip3 install tensorflow
```

```
# 查看版本
import tensorflow as tf
print(tf.__version__)

# 查看GPU和CUDA支持
print(tf.test.is_built_with_gpu_support())
print(tf.test.is_built_with_cuda())

# 查看电脑CPU和GPU
print(tf.config.list_physical_devices())
print(tf.config.list_physical_devices('GPU'))

a = tf.constant(1)
# 打印张量的设备
print(a.device)
# /job:localhost/replica:0/task:0/device:CPU:0

# 系统将运算分配给设备时优先使用 GPU 设备，如果系统上有多个 GPU，则默认情况下会选择具有最小 ID 的 GPU
b = a * 1
print(b.device)
# /job:localhost/replica:0/task:0/device:GPU:0
```

```
import tensorflow as tf

# 启用设备放置记录将导致任何张量分配或运算被打印
tf.debugging.set_log_device_placement(True)

# 指定运行设备
with tf.device('/GPU:0'):
  a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
  b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
  c = tf.matmul(a, b)
# 结果会打印记录
# Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0

print(a.device, b.device, c.device)
# /job:localhost/replica:0/task:0/device:CPU:0 /job:localhost/replica:0/task:0/device:CPU:0 /job:localhost/replica:0/task:0/device:GPU:0
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
b = tf.range(0, 20, 3)
c = tf.linspace(1, 9, 5)
```

### 张量属性

```
# 维数
x.ndim
# 维度
x.shape
x.size()
# 数据
x.numpy()
# 数据类型
x.dtype
# 转置
tf.transpose(x)
```

### 改变类型

```
tf.cast(x, tf.float32)
tf.cast(x, tf.double)
```

### 改变形状

```
# 压缩
tf.squeeze(x)

# 扩展维度
tf.expand_dims(x, axis=0)

# 指定形状
tf.reshape(x, (2, 6))
```

### 索引

```
x[0, :]
x[1, ...]

# 对数组使用布尔运算，并使用位运算符表示逻辑运算
~(x > 1)
(x > 1) & (x < 3)
(x < 1) | (x > 3)
# 运算结果可以作为数组的索引，结果为符合条件的筛选数据
a[a > 1]
```

### 初始化函数

```
# 创建初始化器
initializer = keras.initializers.zeros()
initializer = keras.initializers.glorot_normal()

# 初始化器生产张量
a = initializer(dtype=tf.float32, shape=(1,2))
```

### 创建张量

```
# 初始化器创建常量
initializer = keras.initializers.zeros()
a = initializer(dtype=tf.float32, shape=(1,2))

# 常量
b = tf.constant([[2, 3]], dtype=tf.float32, shape=(1,2))

# 变量
c = tf.Variable([[2, 3]], dtype=tf.float32, shape=(1,2))
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

## 神经网络 Neural Networks

```
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow import nn

keras.__version__
```

### 神经元层

```
# units 包含神经元数
# input_dim 每个神经元输入数
# use_bias 是否有偏置项
layer = keras.layers.Dense(units, input_dim, use_bias=True, name, activation=None, kernel_initializer='glorot_uniform', bias_initializer=keras.initializers.zeros)

# 计算
x = tf.constant([[1, 1, 1]])
logits = layer(x)

# 权重和偏置（计算后生成）
layer.weights

# 激活
y = nn.sigmoid(logits)
y = nn.softmax(logits)
```

### 模型堆叠

```
model = keras.Sequential([
  keras.layers.Dense(2, input_dim=4, activation='sigmoid'),
  keras.layers.Dense(3, input_dim=2),
  keras.layers.Activation(nn.softmax)
])

x = tf.constant([[1, 1, 1, 1]])
y = model(x)
```

### 模型子类化

```
class MyModel(keras.Model):
  def __init__(self):
    super().__init__()
    self.dense1 = keras.layers.Dense(2, input_dim=4, activation='sigmoid', kernel_initializer='glorot_uniform', bias_initializer='glorot_uniform')
    self.dense2 = keras.layers.Dense(3, input_dim=2, activation='softmax', kernel_initializer='glorot_uniform', bias_initializer='glorot_uniform')

  def call(self, inputs):
    x = self.dense1(inputs)
    x = self.dense2(x)
    return x

model = MyModel()

x = tf.constant([[1, 1, 1, 1]])
y = model(x)

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

x = tf.constant([[1., 1., 1.], [2., 2., 2.]])
y = tf.constant([[2., 3.], [4., 6.]])

with tf.GradientTape() as tape:
  # 计算预测值
  y_pred = model(x)
  # 计算损失
  loss = tf.reduce_mean(keras.losses.MSE(y, y_pred))
# 计算梯度
grads = tape.gradient(loss, model.trainable_variables)

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
grads = tape.gradient(loss, model.trainable_variables)
# 更新参数
optimizer.apply_gradients(zip(grads, model.trainable_variables))
```

### 迭代更新

```
optimizer = keras.optimizers.SGD(5e-4)

# 迭代次数
num_batches = 100
for batch_index in range(num_batches):
  with tf.GradientTape() as tape:
    y_pred = model(x)
    loss = tf.reduce_mean(keras.losses.MSE(y, y_pred))
  grads = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(grads, model.trainable_variables))
```

### 评估器

```
# 创建准确度评估器
metric = keras.metrics.Accuracy()
# 重置状态
metric.reset_states()
# 评估函数(标签值, 预测值)
metric.update_state([0, 1, 2], [0, 0, 2])
print('%.4f' % metric.result())
```

### 流水线

```
# 1.打印模型概要
model.summary()

# 2.编译
model.compile(optimizer=keras.optimizers.SGD(5e-4), loss=keras.losses.MSE, metrics=[keras.metrics.MSE])

# 3.训练，返回历史信息model.history，包含params、epoch、history属性
# batch_size 每次批量计算，批量的大小，同一批次内数据不重复，一次计算，一个损失函数值，每个参数更新一次
# steps_per_epoch 从数据中顺序取批次，步骤的次数，各个步骤间数据不重复，最后一步数据可能小于batch_size
# epochs 遍历所有数据轮回数是epochs减去initial_epoch
# shuffle 每次遍历所有数据前，是否对数据随机排序
model.fit(x_train, y_train, batch_size=1, steps_per_epoch=None, initial_epoch=0, epochs=1, shuffle=True)

# 4.评估，返回loss函数值和metrics函数值
model.evaluate(x_test, y_test, batch_size=None, steps=None)

# 5.预测，返回预测值
model.predict(x, batch_size=None, steps=None)
```

### BatchNormalization

```
x = keras.layers.BatchNormalization(axis, epsilon=1e-5, momentum=.1)(x)
```

### Dropout

```
x = keras.layers.Dropout(rate=.2)(x)
```

### estimator

```
# 定义特征列，age 连续、relationship 离散
age = tf.feature_column.numeric_column('age')
relationship = tf.feature_column.categorical_column_with_vocabulary_list(
    'relationship',
    ['Husband', 'Not-in-family', 'Wife', 'Own-child', 'Unmarried', 'Other-relative'])

# 示例化模型
model = tf.estimator.LinearRegressor(feature_columns=[age, relationship], model_dir='./my_model/', label_dimension=1, weight_column=None, optimizer='Ftrl', config=None, warm_start_from=None, loss_reduction='sum_over_batch_size', sparse_combiner='sum')

# 准备训练、评估、预测的数据集
import functools

def train_loader(shuffle=True, batch_size=1):
    dataset = tf.data.Dataset.from_tensor_slices(({
      'age': [1, 2, 3, 4, 5, 6],
      'relationship': ['Husband', 'Not-in-family', 'Wife', 'Own-child', 'Unmarried', 'Other-relative']
    }, [3, 5, 7, 9, 11, 13]))
    if shuffle:
        dataset = dataset.shuffle(buffer_size=1024)
    return dataset.batch(batch_size)

train_inpf = functools.partial(train_loader, shuffle=True, batch_size=2)

def evaluate_loader():
    dataset = tf.data.Dataset.from_tensors(({
      'age': [6, 5, 4, 3, 2, 1],
      'relationship': ['Husband', 'Not-in-family', 'Wife', 'Own-child', 'Unmarried', 'Other-relative']
    }, [8, 8, 8, 8, 8, 8]))
    return dataset

def predict_loader():
  return tf.data.Dataset.from_tensors({
      'age': [1, 2, 3, 4, 5, 6],
      'relationship': ['Husband', 'Not-in-family', 'Wife', 'Own-child', 'Unmarried', 'Other-relative']
})

# 训练
print('-' * 20 + ' train ' + '-' * 20)
model.train(train_inpf)

# 评估
print('-' * 20 + ' evaluate ' + '-' * 20)
eval_res = model.evaluate(evaluate_loader)
for key, value in eval_res.items():
  print('%s: %s' % (key, value))

# 预测
print('-' * 20 + ' predict ' + '-' * 20)
pred_res = model.predict(predict_loader)
for item in pred_res:
     print(item['predictions'])
```

## 卷积神经网络 Convolutional Neural Networks

### 加载数据

```
# 加载MNIST数据，训练数据60000张28*28的灰度值图片，测试数据10000张28*28的灰度值图片
train_set, test_set = keras.datasets.mnist.load_data()

# 显示图片
import matplotlib.pyplot as plt
plt.imshow(train_set[0][0], cmap=plt.get_cmap('gray'))
plt.show()
```

### 数据分批

```
# 一个epoch内，不同batch间、一个batch内数据都不重复，所有数据都计算一次

import numpy as np

class DataLoader():
  def __init__(self, batch_size=1, shuffle=False, train=True):
    train_set, test_set = keras.datasets.mnist.load_data()
    # MNIST中的图像默认为uint8（0-255的数字），以下代码将其归一化到0-1之间的浮点数，并在最后增加一维作为颜色通道
    if train:
      x = np.expand_dims(train_set[0].astype(np.float32) / 255, axis=-1)      # [60000, 28, 28, 1]
      y = train_set[1].astype(np.int32)      # [60000]
    else:
      x = np.expand_dims(test_set[0].astype(np.float32) / 255, axis=-1)        # [10000, 28, 28, 1]
      y = test_set[1].astype(np.int32)      # [10000]
    self.dataset = tf.data.Dataset.from_tensor_slices((x, y))
    self.batch_size = batch_size
    self.shuffle = shuffle

  def __iter__(self):
    if self.shuffle:
      return iter(self.dataset.shuffle(buffer_size=1024).batch(self.batch_size))
    return iter(self.dataset.batch(self.batch_size))

# 训练数据生成器
train_loader = DataLoader(batch_size=9999, shuffle=True)

# 测试数据生成器
test_loader = DataLoader(batch_size=100, shuffle=True, train=False)
```

### 建立模型

```
class CNNModel(keras.Model):
  def __init__(self):
    super().__init__()
    # 卷积层1
    self.conv1 = keras.layers.Conv2D(filters=10, kernel_size=(5, 5), strides=(1, 1), padding='same', activation='relu')
    # 池化层
    self.pool = keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2))
    # 卷积层2
    self.conv2 = keras.layers.Conv2D(filters=20, kernel_size=(5, 5), strides=(1, 1), padding='same', activation='relu')
    # 展平层
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
  for x, y in train_loader:
    with tf.GradientTape() as tape:
      y_pred = model(x)
      loss = criterion(y, y_pred)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
```

### 交叉熵评估

```
# SparseCategoricalCrossentropy评估器直接处理
metric = keras.metrics.SparseCategoricalCrossentropy()
metric.update_state([0, 1], [[.5, .5], [.5, .5]])
print('%.4f' % metric.result())

# CategoricalCrossentropy评估器需要先对数据做one hot编码
metric = keras.metrics.CategoricalCrossentropy()
metric.update_state([[1, 0], [0, 1]], [[.5, .5], [.5, .5]])
print('%.4f' % metric.result())

metric.reset_states()
metric.update_state(tf.one_hot([0, 1], 2), [[.5, .5], [.5, .5]])
print('%.4f' % metric.result())
```

### 评估模型

```
# 交叉熵准确度评估器
metric = keras.metrics.SparseCategoricalAccuracy()

for x, y in test_loader:
  y_pred = model(x)
  metric.update_state(y, y_pred)

print('%.4f' % metric.result())
```

### 使用封装流程

```
model.compile(optimizer=keras.optimizers.SGD(5e-4), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=[keras.metrics.SparseCategoricalAccuracy()])

model.fit(x_train, y_train, batch_size=100, epochs=10, shuffle=True)

model.evaluate(x_test, y_test, batch_size=100)
```

## 循环神经网络 Recurrent Neural Networks

### SimpleRNNCell

```
# units 神经元个数，每个神经元状态数
# input_dim 每个神经元输入数
# kernel_initializer 输入权重初始化函数
# recurrent_initializer 状态权重初始化函数
# bias_initializer 偏置初始化函数
cell = keras.layers.SimpleRNNCell(units, input_dim, use_bias=True, activation='tanh', kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros')

# 输入和状态
inputs = tf.ones((batch, input_dim))
states = tf.ones((batch, units))

# 输入和输入权重矩阵乘，状态和状态权重矩阵乘，相加后再加上偏置，激活函数激活
# 返回(batch, units)
cell(inputs, states)

# kernel 输入权重(input_dim, units)
# recurrent_kernel 状态权重(units, units)
# bias 偏置(units,)
cell.weights
```

### SimpleRNN

```
# 一个SimpleRNN是一个SimpleRNNCell自身进行多次循环
rnn = keras.layers.SimpleRNN(units, input_dim, use_bias=True, activation='tanh', kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros')

# 输入和初始状态
# inputs的一个batch包含每个循环的输入数据，timesteps次循环
inputs = tf.ones((batch, timesteps, input_dim))
initial_state = tf.ones((batch, units))

# 在一次循环中：
# 输入和输入权重矩阵乘，状态和状态权重矩阵乘，相加后再加上偏置，激活函数激活
# 将循环的结果作为下一次循环的状态，并取对应的输入数据，进入下一次循环
# 返回最后一次循环的结果(batch, units)
rnn(inputs, initial_state)

# kernel 输入权重(input_dim, units)
# recurrent_kernel 状态权重(units, units)
# bias 偏置(units,)
rnn.weights
```

### RNN

```
# 一个RNN是多个SimpleRNN首尾相连

cell_0 = keras.layers.SimpleRNNCell(units_0, input_dim)
cell_1 = keras.layers.SimpleRNNCell(units_1, units_0)

# 将一个RNNCell队列首尾相连构成一个RNN
rnn = keras.layers.RNN([cell_0, cell_1])

# 输入和初始状态
# inputs的一个batch包含第一个cell每次循环的的输入数据，timesteps次循环
inputs = tf.ones((batch, timesteps, input_dim))
# RNNCell队列对应的初始状态队列
initial_state = [tf.ones((batch, units_0)), tf.ones((batch, units_1))]

# 每个SimpleRNNCell生成一个SimpleRNN，经过多次循环得到结果(batch, unit)
# 前一个SimpleRNN的结果作为后一个SimpleRNN的输入数据，再从initial_state中获取后一个SimpleRNN的初始状态
# 返回最后一个SimpleRNN的结果(batch, units_1)
rnn(inputs, initial_state)

# 每个RNNCell的kernel, recurrent_kernel, bias
rnn.weights
```

## 可视化

```
pip3 install tensorboard

tensorboard --logdir=./tensorboard --bind_all >/dev/null 2>&1 &

# 浏览器打开http://localhost:6006/
```

### 记录数值

```
# 指定日志目录
log_dir = './tensorboard'
# 创建日志文件句柄
summary_writer = tf.summary.create_file_writer(log_dir)
# 横坐标
step = 0

for epoch_index in range(epochs):
  for x_train, y_train in train_loader:
    with tf.GradientTape() as tape:
      y_pred = model(x_train)
      loss = criterion(y_train, y_pred) 
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

    # 希望使用的记录器
    with summary_writer.as_default():
      tf.summary.scalar("model_loss", loss, step=step)
    step += 1
```

### 流水线

```
log_dir = './tensorboard'
# # 定义TensorBoard对象为回调
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x_train, y_train, batch_size=1, epochs=1, callbacks=[tensorboard_callback])
```

## 保存与读取

### TFRecord 文件

```
tfrecord_file = './train.tfrecords'

# 导出 TFRecord 文件
with tf.io.TFRecordWriter(tfrecord_file) as writer:
  for i in range(10):
      # 建立 tf.train.Feature 字典
      feature = {                            
        'a': tf.train.Feature(int64_list=tf.train.Int64List(value=[i, i + 1, i + 2, i + 3])),  #  Int 列表
        'b': tf.train.Feature(float_list=tf.train.FloatList(value=[i, i * i])),  # Float 列表
        'c': tf.train.Feature(bytes_list=tf.train.BytesList(value=[str(i).encode()]))   # Bytes列表
      }
      # 通过字典建立 Example
      example = tf.train.Example(features=tf.train.Features(feature=feature))
      # 写数据
      writer.write(example.SerializeToString())  


# 读取 TFRecord 文件
raw_dataset = tf.data.TFRecordDataset(tfrecord_file)

# 定义Feature结构，告诉解码器每个Feature的类型是什么
feature_description = {
  'a': tf.io.FixedLenFeature((2, 2), tf.int64),
  'b': tf.io.FixedLenFeature((1, 2), tf.float32),
  'c': tf.io.FixedLenFeature((1,), tf.string),
}

# 将 TFRecord 文件中的每一个序列化的 tf.train.Example 解码
def parse_example(example_string):
    feature_dict = tf.io.parse_single_example(example_string, feature_description)
    return feature_dict['a'], feature_dict['b'], feature_dict['c']
dataset = raw_dataset.map(parse_example)

# 打印数据
for a, b, c in dataset:
    print(a.numpy(), b.numpy(), c.numpy())
```

### 保存模型参数

```
model.save_weights('./my_model/weights/weights')

model.load_weights('./my_model/weights/weights')
```

### 保存模型

```
# SavedModel 导出模型目录结构
/saved_model_files
    /1      # 版本号为1的模型文件
        /assets
        /variables
        saved_model.pb
    ...
    /N      # 版本号为N的模型文件
        /assets
        /variables
        saved_model.pb

# 版本号
version = 1

# SavedModel 导出模型
tf.saved_model.save(model, './my_model/saved_models/{}'.format(version))
model = tf.saved_model.load('./my_model/saved_models/{}'.format(version))

# Keras Sequential 导出模型
keras.models.save_model(model, ./my_model/HDF5/model.h5')
model = keras.models.load_model('./my_model/HDF5/model.h5'')
```

### 保存Checkpoint

```
# 使用自定义键值对创建Checkpoint对象
ckpt = tf.train.Checkpoint(step=tf.Variable(1), model=model, optimizer=optimizer, dataset=dataset)
# 在新的Checkpoint恢复键值对的值
new_ckpt = tf.train.Checkpoint(step=tf.Variable(1), model=model, optimizer=optimizer, dataset=dataset)

# 1.直接保存
ckpt.write('./my_model/ckpts/ckpt')
new_ckpt.read('./my_model/ckpts/ckpt')

# 2.前缀后加'-1'保存为一个版本，版本号递增
ckpt.save('./my_model/ckpts/ckpt')
new_ckpt.restore('./my_model/ckpts/ckpt-1')

# 返回最新路径
tf.train.latest_checkpoint('./my_model/ckpts')

# 查看保存键值对
tf.train.list_variables('./my_model/ckpts/ckpt-1')
# 获取变量
tf.train.load_variable('./my_model/ckpts/ckpt-1', '<变量名>')

# Checkpoint管理，max_to_keep表示只保存最新的个数
manager = tf.train.CheckpointManager(ckpt, './my_model/ckpts', max_to_keep=3)
manager.save()
# Checkpoint历史和最新的路径
manager.checkpoints
manager.latest_checkpoint
```

### Hub 模型

```
# 官方网站
# https://tfhub.dev
# 国内镜像
# https://hub.tensorflow.google.cn

# 安装模块
pip3 install tensorflow-hub

# 导入模块，查看版本
import tensorflow_hub as hub
print(hub.__version__)

# 加载模型
hub_handle = 'https://hub.tensorflow.google.cn/google/magenta/arbitrary-image-stylization-v1-256/2'
hub_module = hub.load(hub_handle)

# 也可以在网站下载tar模型包，解压后将目录修改为模型名，使用keras.models.load_model加载
```

### 模型使用

```
# 该模型将输入图片按照给定样本图片风格重绘

import numpy as np
import matplotlib.pyplot as plt

# 输入图片
content_image = plt.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Golden_Gate_Bridge_from_Battery_Spencer.jpg/640px-Golden_Gate_Bridge_from_Battery_Spencer.jpg', 'jpg')
# 样本图片
style_image = plt.imread('https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg', 'jpg')

# 打印输入图片和样本图片
plt.imshow(content_image)
plt.imshow(style_image)
plt.show()

# 将图片转换为[batch_size, image_height, image_width, 3]大小的[0, 255]上的浮点数
content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255
style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255

# 加载模型
hub_handle = 'https://hub.tensorflow.google.cn/google/magenta/arbitrary-image-stylization-v1-256/2'
hub_module = hub.load(hub_handle)

# 通过模型转换
outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
stylized_images = outputs[0]
stylized_image = stylized_images[0]

# 打印结果
plt.imshow(stylized_image)
plt.show()
```

### 模型再训练

```
# 使用 hub.KerasLayer 组件待训练模型
new_model = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/4", output_shape=[2048], trainable=False),
    tf.keras.layers.Dense(10, activation='softmax')
])
new_model.build([None, 299, 299, 3])
```

## 部署模型

### 部署服务 TensorFlow Serving

apt安装

```
# 添加GPG key
curl -fsSL https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -

# 添加仓库
echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list

# 安装
sudo apt update
sudo apt install tensorflow-model-server

# 模型导出

# 开启服务，可以使用Supervisor配置
tensorflow_model_server  --rest_api_port=8501  --model_name=<模型名> --model_base_path=<导出模型绝对路径> >server.log 2>&1 &
```

Docker安装

```
docker pull tensorflow/serving
git clone https://github.com/tensorflow/serving

# demo模型位置
TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"

# 开启服务，可以使用Supervisor配置
docker run -t --rm -p 8501:8501 \
    -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" \
    -e MODEL_NAME=half_plus_two \
    tensorflow/serving &

# 请求
curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://localhost:8501/v1/models/half_plus_two:predict

# 响应
{ "predictions": [2.5, 3.0, 4.5] }
```

使用

```
import json
import requests

# 准备数据
data = json.dumps({
  "signature_name": "serving_default",
  "instances": <x_predict>
})

headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/my_model:predict', data=data, headers=headers)
result = json.loads(json_response.text)
if 'error' in result:
  print(result['error'])
else:
  print(result['predictions'])

# 成功返回值
{
    "predictions": <y_predict>
}
```

### 轻量级 TensorFlow Lite

在移动端（mobile）、嵌入式（embeded）和物联网（IoT）设备上运行 TensorFlow 模型

```
# 先导出模型，再转换为tflite模型

# SavedModel 导出模型转换
tflite_convert --saved_model_dir=my_model --output_file=my_model.tflite

# Keras Sequential 导出模型转换
tflite_convert --keras_model_file=my_model.h5 --output_file=my_model.tflite
```

### TENSORFLOW.JS

TensorFlow.js 支持在浏览器或Node.js中构建、训练、使用和部署模型

```
# 浏览器
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script>

# Node.js
# 安装 tfjs 库，纯 JavaScript 版本
npm install @tensorflow/tfjs

# 安装 tfjs-node 库，C Binding 版本
npm install @tensorflow/tfjs-node

# 安装 tfjs-node-gpu 库，支持 CUDA GPU 加速
npm install @tensorflow/tfjs-node-gpu
```

先导出模型，转换为TENSORFLOW.JS模型

```
# pip3 install tensorflowjs

# Keras Sequential 导出模型转换
tensorflowjs_converter --input_format keras \
                       path/to/my_model.h5 \
                       path/to/tfjs_target_dir

# SavedModel 导出模型转换
tensorflowjs_converter \
    --input_format=tf_saved_model \
    --output_node_names='MobilenetV1/Predictions/Reshape_1' \
    --saved_model_tags=serve \
    /mobilenet/saved_model \
    /mobilenet/tfjs_model
    
# Tensorflow Hub 模型转换
tensorflowjs_converter \
    --input_format=tf_hub \
    'https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/classification/1' \
    /mobilenet/web_model
```

TENSORFLOW.JS加载模型

```
import * as tf from '@tensorflow/tfjs';
import {loadGraphModel} from '@tensorflow/tfjs-converter';

const MODEL_URL = 'model_directory/model.json';

const model = await loadGraphModel(MODEL_URL);
const cat = document.getElementById('cat');
model.execute(tf.fromPixels(cat));
```

