```
pip3 install scikit-learn
```

```
# 查看版本
import sklearn
print(sklearn.__version__)
```

### 最小二乘法线性回归

```
import numpy as np
from sklearn import linear_model

# fit_intercept 是否包含截距项
# normalize 是否对每个样本做归一化
# copy_X 是否保持X不被修改
# n_jobs 并行计算时使用CPU的数量
model = linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)

# 样本数据
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.float32)
y = np.array([1, 3, 5, 7], dtype=np.float32)

# 训练
model.fit(X, y)
# 评估
model.score(X, y)
# 预测
model.predict(X)

# 特征数
model.n_features_in_
# 权重
model.coef_
# 截距
model.intercept_
```

### 岭回归

```
import numpy as np
from sklearn import linear_model

# alpha 正则项系数
# tol 计算结果精度
# solver 求解算法
model = linear_model.Ridge(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=1e-3, solver='auto', random_state=None)

# 样本数据
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.float32)
y = np.array([1, 3, 5, 7], dtype=np.float32)

# 训练
model.fit(X, y)
# 评估
model.score(X, y)
# 预测
model.predict(X)

# 特征数
model.n_features_in_
# 权重
model.coef_
# 截距
model.intercept_
```

