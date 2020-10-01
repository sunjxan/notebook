```
# 打开 https://pytorch.org/get-started/locally/
pip3 install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

```
# 查看版本
from __future__ import print_function
import torch
print(torch.__version__)

# 查看GPU和CUDA支持
print(torch.cuda.is_available())

# 查看电脑GPU
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))
print(torch.cuda.current_device())

# 示例
a = torch.tensor([1.0,2.0,3.0,4.0,5.0,6.0])
a = a.reshape(2, 3)
b = torch.tensor([1.0,2.0,3.0,4.0,5.0,6.0])
b = b.reshape(3, 2)
c = a.matmul(b)
print(c)
```

