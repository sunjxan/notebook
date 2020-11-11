```
pip3 install numpy

import numpy as np
np.__version__
```

### 创建数组

```
a = np.ndarray((3, 4))
b = np.empty((3, 4))
c = np.array(b)
```

### 生成数组

```
x = np.zeros((3, 4))
y = np.ones((3, 4))
z = np.random.random((3, 4))
x2 = np.zeros_like(x)
y2 = np.ones_like(y)
a = np.full((2,3), 5.)
a2 = np.full_like(a, 3.)
b = np.arange(0, 20, 3)
c = np.linspace(1, 9, 5)
```

### 数组属性

```
# 维数
x.ndim
# 维度
x.shape
# 元素个数
x.size
# 数据类型
x.dtype
# 复制
x.copy()
# 转置
x.T
```

### 改变类型

```
x.astype(np.uint8)
```

### 改变形状

```
# 展平
x.flatten()

# 压缩
x.squeeze()

# 扩展维度
np.expand_dims(x, axis=0)

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

### 轴axis

指维度的某一个分量，调用函数时传入该参数，表示函数操作是在哪一个维度上进行的。

### 总结

Numpy支持的操作非常多，做大多数数组操作、矩阵操作、数学运算、统计运算时应该先查找Numpy中是否已有实现。