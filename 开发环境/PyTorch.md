```
# https://pytorch.org/get-started/locally/
# CPU版
pip3 install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
# CUDA10.1版
pip3 install torch==1.7.0+cu101 torchvision==0.8.1+cu101 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
```

```
# 查看版本
import torch
print(torch.__version__)

# 查看CUDA和cudnn支持
print(torch.cuda.is_available())
print(torch.backends.cudnn.enabled)

# 查看电脑GPU
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name('cuda'))

a = torch.tensor(1)
print(a.device)
# cpu

# 或 b = a.cuda()
b = a.to('cuda')
print(b.device)
# cuda:0

# 直接在GPU上创建tensor
a = torch.tensor([[1., 2., 3.], [4., 5., 6.]], device=torch.device('cuda'))
# 使用to方法移动tensor到任何设备（默认是CPU），也能在移动时改变dtype
b = torch.tensor([[1, 2], [3, 4], [5, 6]]).to('cuda', torch.float32)
c = torch.matmul(a, b)

print(a.device, b.device, c.device)
# cuda:0 cuda:0 cuda:0
```

## 基础知识

### 生成张量

```
x = torch.zeros((3, 4))
y = torch.ones((3, 4))
z = torch.rand((3, 4))
x2 = torch.zeros_like(x)
y2 = torch.ones_like(y)
a = torch.full((2,3), 5.)
a2 = torch.full_like(a, 3.)
b = torch.arange(0, 20, 3)
c = torch.linspace(1, 9, 5)
```

### 张量属性

```
# 维数
x.ndim
# 维度
x.shape
# 数据
x.data
x.numpy()
# 数据类型
x.dtype
# 复制
x.clone()
# 转置
x.T
```

### 改变类型

```
x.float()
x.double()
```

### 改变形状

```
# 展平
x.flatten()

# 压缩
x.squeeze()

# 在原有维度基础上复制数据进行扩展
x.expand((2, 3, -1, -1))

# 指定形状
x.view((2, -1))
x.reshape((-1, 6))
```

### 索引

```
x[0, :]
x[1, ...]

# 在索引中需要传递数字的地方，传入一个包含多个数字的tuple，表示选中的下标
# 可以任意调换顺序，也可以重复数字
# 当一个索引中多个位置使用tuple时，它们的长度要保持一致
# 用于筛选数据
x[:, :, (0, 1)]
# 用于调换数据顺序
x[:, :, (2, 1, 0)]
# 用于复制数据
x[:, (0, 0), :]

# 对数组使用布尔运算，并使用位运算符表示逻辑运算
~(x > 1)
(x > 1) & (x < 3)
(x < 1) | (x > 3)
# 运算结果可以作为数组的索引，结果为符合条件的筛选数据
a[a > 1]
```

### 赋值

```
x[0, :] = 1
x[1, ...] = 2
```

### 初始化函数

```
nn.init.zeros_(a)

# xavier_normal_只能对多维数据初始化
nn.init.xavier_normal_(a)
```

### 创建张量

```
a = torch.empty((2, 3))
nn.init.xavier_normal_(a)

b = torch.tensor([[2, 3]], dtype=torch.float32)
```

### 自动求导

```
# 创建张量，追踪对于该张量的所有操作
a = torch.tensor([[2, 3]], dtype=torch.float32, requires_grad=True)
b = torch.tensor([[5], [6]], dtype=torch.float32, requires_grad=True)
# 计算得到结果
c = a.matmul(b)
# 进行反向传播
c.backward(torch.ones(c.shape))
print(c, a.grad, b.grad)
```

## 神经网络 Neural Networks

```
import torch.nn as nn
```

### 神经元层

```
# in_features 每个神经元输入数
# out_features 包含神经元数
# bias 是否有偏置项
layer = nn.Linear(in_features, out_features, bias=True)

# 权重和偏置（计算前生成）
layer.weight
layer.bias

# 初始化权重和偏置
nn.init.xavier_normal_(layer.weight)
nn.init.xavier_normal_(layer.bias.view((1, -1)))

# 计算
x = torch.tensor([[1, 1, 1]], dtype=torch.float32)
logits = layer(x)

# 激活
f1 = nn.Sigmoid()
y = f1(logits)
f2 = nn.Softmax(dim=-1)
y = f2(logits)
```

### 模型堆叠

```
model = nn.Sequential(
  nn.Linear(2, 2),
  nn.Sigmoid(),
  nn.Linear(2, 3),
  nn.Softmax(-1)
)

print(model)

x = torch.tensor([[1, 1]], dtype=torch.float32)
y = model(x)
```

### 模型子类化

```
class MyModel(nn.Module):
  def __init__(self):
    super().__init__()
    self.fc1 = nn.Linear(2, 2)
    nn.init.xavier_normal_(self.fc1.weight)
    nn.init.xavier_normal_(self.fc1.bias.view((1, -1)))
    self.f1 = nn.Sigmoid()
    self.fc2 = nn.Linear(2, 3)
    nn.init.xavier_normal_(self.fc2.weight)
    nn.init.xavier_normal_(self.fc2.bias.view((1, -1)))
    self.f2 = nn.Softmax(-1)

  def forward(self, inputs):
    x = self.fc1(inputs)
    x = self.f1(x)
    x = self.fc2(x)
    x = self.f2(x)
    return x

model = MyModel()

x = torch.tensor([[1, 1]], dtype=torch.float32)
y = model(x)

# 查看模型层
list(model.children())
# 查看模型权重和偏置
list(model.parameters())
model.state_dict()
```

### 损失函数

```
# 为批量计算的数据求损失，再平均
criterion = nn.MSELoss()
# 损失函数(预测值，标签值)
loss = criterion(torch.tensor([[1.,2.]]), torch.tensor([[2., 4.]]))
```

### 反向传播

```
class MyModel(nn.Module):
  def __init__(self):
    super().__init__()
    self.fc = nn.Linear(3, 2)
    nn.init.zeros_(self.fc.weight)
    nn.init.zeros_(self.fc.bias)

  def forward(self, inputs):
    return self.fc(inputs)

model = MyModel()

x = torch.tensor([[1., 1., 1.], [2., 2., 2.]])
y = torch.tensor([[2., 3.], [4., 6.]])

# 计算预测值
y_pred = model(x)
# 计算损失
criterion = nn.MSELoss()
loss = criterion(y_pred, y)

# 清零所有参数(parameter）的梯度缓存
model.zero_grad()
# 计算梯度
loss.backward()

# 打印损失
print(loss)
# 打印梯度
for param in model.parameters():
  print(param.grad)
```

### 优化器

```
# 创建优化器
optimizer = torch.optim.SGD(model.parameters(), 5e-4)
# 清零梯度缓存
optimizer.zero_grad()
# 计算梯度
loss.backward()
# 更新参数
optimizer.step()
```

### 迭代更新

```
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), 5e-4)

# 迭代次数
num_batches = 100
for batch_index in range(num_batches):
  optimizer.zero_grad()
  y_pred = model(x)
  loss = criterion(y_pred, y)
  loss.backward()
  optimizer.step()
```

### BatchNormalization

```
x = nn.BatchNorm1d(num_features, eps=1e-5, momentum=.1)(x)
```

### Dropout

```
x = nn.Dropout(p=.2)(x)
```

### 多设备并行

```python
if torch.cuda.device_count() > 1: 
  model = nn.DataParallel(model)
```

## 卷积神经网络 Convolutional Neural Networks

### 卷积层

```
layer_padding = nn.Conv2d(in_channels=3, out_channels=10, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), padding_mode='zeros')
layer_no_padding = nn.Conv2d(in_channels=3, out_channels=10, kernel_size=(5, 5), stride=(1, 1))

# (batch, channels, height, width)
x = torch.tensor(train_data / 255, dtype=torch.float32)

# (batch, out_channels, height, width)
y = layer_padding(x)
# (batch, out_channels,  (height - kernel_size_height) // strides_y + 1, (width - kernel_size_width) // strides_x + 1)
y = layer_no_padding(x)
```

### 加载数据

```
# 导入视觉包
import torchvision as tv

# 加载MNIST数据，训练数据60000张28*28的灰度值图片，测试数据10000张28*28的灰度值图片
# 加载训练数据，得到PIL.Image.Image类型的图片
train_set = tv.datasets.MNIST(root='./data', train=True, download=True)      # (60000, 2, 28, 28)
# 显示图片
import matplotlib.pyplot as plt
plt.imshow(train_set[0][0], cmap='gray')
plt.show()

transform = tv.transforms.Compose([tv.transforms.ToTensor()])
# 加载测试数据，将PIL Image转换为Tensor
test_set = tv.datasets.MNIST(root='./data', train=False, download=True, transform=transform)      # (10000, 2, 1, 28, 28)
# 显示图片
plt.imshow(test_set[0][0][0], cmap='gray')
plt.show()
```

### 数据分批

```
# 一个epoch内，不同batch间、一个batch内数据都不重复，所有数据都计算一次

# 要进行计算，必须将PIL Image转换为Tensor
transform = tv.transforms.Compose([tv.transforms.ToTensor()])
train_set = tv.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_set = tv.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# 训练数据生成器
train_loader = torch.utils.data.DataLoader(train_set, batch_size=100, shuffle=True)

# 测试数据生成器
test_loader = torch.utils.data.DataLoader(test_set, batch_size=100, shuffle=True)
```

### 建立模型

```
class CNNModel(nn.Module):
  def __init__(self):
    super().__init__()
    # 卷积层1
    self.conv1 = nn.Conv2d(in_channels=1, out_channels=10, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), padding_mode='zeros')
    # 池化层
    self.pool = nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))
    self.relu = nn.ReLU()
    # 卷积层2
    self.conv2 = nn.Conv2d(in_channels=10, out_channels=20, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), padding_mode='zeros')
    # 展平层
    self.flatten = nn.Flatten()
    # 经过两次池化后得到的矩阵大小为(28/2/2, 28/2/2)
    self.fc1 = nn.Linear(20*7*7, 50)
    self.fc2 = nn.Linear(50, 10)

  def forward(self, inputs):
    x = self.conv1(inputs)
    x = self.relu(x)
    x = self.pool(x)
    x = self.conv2(x)
    x = self.relu(x)
    x = self.pool(x)
    x = self.flatten(x)
    x = self.fc1(x)
    x = self.relu(x)
    x = self.fc2(x)
    return x

model = CNNModel()
```

### 交叉熵损失

```
# 输出层不需做Softmax激活，CrossEntropyLoss函数直接处理
criterion = nn.CrossEntropyLoss()
criterion(torch.tensor([[5., 5.], [5., 5.]]), torch.tensor([0, 1]))
```

### 训练模型

```
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), 5e-4)

epochs = 10
for epoch_index in range(epochs):
  for x, y in train_loader:
    optimizer.zero_grad()
    y_pred = model(x)
    loss = criterion(y_pred, y)
    loss.backward()
    optimizer.step()
```

### 评估模型

```
correct = 0
total = 0

# 阻止autograd跟踪设置了 requires_grad=True 的张量的历史记录
with torch.no_grad():
  for x, y in test_loader:
    y_pred = model(x)
    total += y.size(0)
    correct += (torch.argmax(y_pred, -1) == y).sum().item()

print('%.4f' % (correct / total))
```

## 循环神经网络 Recurrent Neural Networks

### RNNCell

```
# input_size 每个神经元输入数
# hidden_size 神经元个数，每个神经元状态数
cell = nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh')

# weight_ih 输入权重(hidden_size, input_size)
# bias_ih 输入偏置(hidden_size,)
# weight_hh 状态权重(hidden_size, hidden_size)
# bias_hh 状态偏置(hidden_size,)
cell.weight_ih, cell.bias_ih, cell.weight_hh, cell.bias_hh

# 输入和状态
input = torch.ones((batch, input_size))
hidden = torch.ones((batch, hidden_size))

# 输入和输入权重矩阵乘，加上输入偏置
# 状态和状态权重矩阵乘，加上状态偏置
# 全部相加，激活函数激活
# 返回(batch, hidden_size)
cell(input, hidden)
```

### RNN

```
# 一个RNN是多个RNNCell首尾相连
# num_layers 包含RNNCell层数
# input_size 第一层每个神经元输入数
# hidden_size 每层神经元个数，除第一层外每个神经元输入数，每个神经元状态数
rnn = nn.RNN(input_size, hidden_size, num_layers, bias=True, nonlinearity='tanh')

# 对每一层（index从0开始），都有以下：
# weight_ih_l<index> 输入权重(hidden_size, hidden_size), weight_ih_l0(hidden_size, input_size)
# bias_ih_l<index> 输入偏置(hidden_size,)
# weight_hh_l<index> 状态权重(hidden_size, hidden_size)
# bias_hh_l<index> 状态偏置(hidden_size,)
cell.weight_ih_l<index>, cell.bias_ih_l<index>, cell.weight_hh_l<index>, cell.bias_hh_l<index>

# 输入和初始状态
# input的一个batch包含第一个cell每次循环的输入数据，seq_len次循环
input = torch.ones((seq_len, batch, input_size))
hidden = torch.ones((num_layers, batch, hidden_size))

# 对每个RNNCell，获取初始状态，进行seq_len次循环，在一次循环中：
# 输入和输入权重矩阵乘，加上输入偏置，状态和状态权重矩阵乘，加上状态偏置，全部相加，激活函数激活
# 将循环的结果作为下一次循环的状态，并取对应的输入数据，进入下一次循环
# 前一个RNNCell所有循环结束后，将得到的所有结果，作为后一个RNNCell的输入数据
# 返回最后一个RNNCell每次循环的结果output(seq_len, batch, hidden_size)
# 和每个RNNCell最后一次循环的结果hidden(num_layers, batch, hidden_size)
rnn(input, hidden)
```

## 可视化

```
pip3 install tensorboard

tensorboard --logdir=./pytorch --bind_all >/dev/null 2>&1 &

# 浏览器打开http://localhost:6006/
```

### 记录数值

```
# 创建日志文件句柄
summary_writer = torch.utils.tensorboard.SummaryWriter()
# 横坐标
step = 0

for epoch_index in range(epochs):
  for x_train, y_train in train_loader:
    optimizer.zero_grad()
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)
    loss.backward()
    optimizer.step()
    # 记录损失
    writer.add_scalar('model_loss', loss, step)
    step += 1
```

## 模型保存

### 保存模型参数

```
x = torch.tensor([1])
torch.save(x, './tensor.pt')
x = torch.load('./tensor.pt')

torch.save(model.state_dict(), './parameter.pt')

model.load_state_dict(torch.load('./parameter.pt'))
```

### 保存模型

 ```
torch.save(model, './my_model.pt')

model = torch.load('./my_model.pt')
 ```

### Hub 模型

```
# 官方网站
# https://pytorch.org/hub/

# 从GitHub加载模型 repo_owner/repo_name[:tag_name]
model = torch.hub.load('facebookresearch/pytorch_GAN_zoo:hub', model ='DCGAN', pretrained=True, useGPU=torch.cuda.is_available())

# 可以先在GitHub下载zip模型包，放入目录.cache/torch/hub/再加载
```

### 模型使用

```
# DCGAN 深度卷积生成对抗神经网络
# 生成64x64大小的图片
num_images = 1
noise, _ = model.buildNoiseData(num_images)
with torch.no_grad():
  generated_images = model.test(noise)

import matplotlib.pyplot as plt
import torchvision

# 打印结果
plt.imshow(torchvision.utils.make_grid(generated_images).permute(1, 2, 0))
plt.show()
```
