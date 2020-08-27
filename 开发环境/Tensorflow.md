1. 打开终端窗口，使用以下命令查看显卡信息和检查显卡正在使用的驱动程序，默认情况下开源nouveau驱动程序用于Nvidia卡；
```
sudo lshw -c display
```

2. 在 https://www.nvidia.com/Download/index.aspx?lang=cn 中选择对应选项下载正确的驱动程序；

3. 删除旧的NVIDIA的驱动：
```
sudo apt-get purge nvidia*
sudo apt autoremove
```

4. 将系统自带的nouveau驱动屏蔽掉，代码如下：
```
# 打开系统黑名单:
sudo gedit /etc/modprobe.d/blacklist-nouveau.conf 
# 在末尾加入如下内容：
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
# 更新内核后重启:
echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveau-kms.conf
sudo update-initramfs -u
sudo reboot
# 重启电脑后输入：
lsmod | grep nouveau
# 没有任何输出说明禁用成功
```

5. 禁用主板的 Secure Boot 功能；

6. 安装驱动：
```
sudo sh NVIDIA-Linux-x86_64-440.44.run -no-opengl-files
# 忽略 pre-install script failed 信息
# 32位兼容 安装最好 选yes
# 命令行输入：
nvidia-smi
# 正确输出信息即安装成功
```

7. 安装cuda，要注意cuda没有向后兼容，应选择需要安装的tensorflow支持的cuda版本，安装时不勾选Nvidia驱动：
```
sudo sh cuda_10.1.243_418.87.00_linux.run
# 修改环境变量
sudo gedit ~/.bashrc
# 在文件最后添加：
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.1/lib64
export PATH=$PATH:/usr/local/cuda-10.1/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.1
# 使配置生效：
source ~/.bashrc
# 命令行输入：
nvcc -V
# 正确输出信息即安装成功
```

8. 安装cudnn：
```
sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.2_amd64.deb
```

9. 安装tensorflow：
```
pip3 install --user --upgrade tensorflow
```

10. 新建python文件，若能正确执行，则安装成功：
查看tensorflow版本
```
import tensorflow as tf
print(tf.__version__)
```
查看GPU和CUDA支持
```
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
print(tf.test.is_gpu_available())
print(tf.test.is_built_with_cuda())
```
查看电脑GPU和CPU
```
import os
from tensorflow.python.client import device_lib
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "99"
print(device_lib.list_local_devices())
```
指定GPU进行计算
```
import tensorflow as tf
with tf.device("/GPU:0"):
    a = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0],shape=[2,3])
    b = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0],shape=[3,2])
    c = tf.matmul(a,b)
    print(c)
```


