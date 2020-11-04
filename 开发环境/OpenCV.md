### pip安装

**这种安装方式在IDE上有代码提示功能**

```
pip3 install opencv-contrib-python
```

### 编译安装

安装开发工具：

```bash
sudo apt install build-essential cmake unzip pkg-config
```

安装图片和视频的I/O库, 保证可以从磁盘中读取图像和视频：

```bash
sudo apt install libjpeg-dev libpng-dev libtiff-dev
sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt install libxvidcore-dev libx264-dev
```

安装GTK图形工具包：

```bash
sudo apt install libgtk-3-dev
```

安装数学优化库：

```bash
sudo apt install libatlas-base-dev gfortran
```

安装python开发工具：

```bash
sudo apt install python3-dev
```

下载opencv和opencv-contrib并解压：

```bash
# 最新版本下载地址
# opencv https://github.com/opencv/opencv/releases
# opencv_contrib https://github.com/opencv/opencv_contrib/releases
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.0.zip
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-4.5.0 opencv
mv opencv_contrib-4.5.0 opencv_contrib
```

GitHub源文件下载问题

https://raw.githubusercontent/ 域名下文件无法下载，要从 https://github.com/googlehosts/hosts/blob/master/hosts-files/hosts 中复制解析规则到hosts文件中。


运行CMake：

```bash
# -D OPENCV_ENABLE_NONFREE=ON 此标志可确保您可以访问SIFT / SURF和其他获得专利的算法
# -D OPENCV_EXTRA_MODULES_PATH 不要写错opencv-contrib文件夹了
# -D PYTHON_EXECUTABLE 你的目标python环境

cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D PYTHON_EXECUTABLE=/usr/bin/python3 \
	-D BUILD_EXAMPLES=ON ..
```

编译：

```bash
# -j8代表用8个核编译, 核越多, 编译的速度越快
# 使用以下命令查看逻辑CPU的个数
# nproc
make -j8
```

安装：

```bash
sudo make -j8 install
sudo ldconfig
```

最终得到动态链接库 `.so` 文件，可以再使用pip安装一次，然后使用编译获得的 `.so` 文件进行替换，以获得IDE的代码提示功能：

```
pip3 install opencv-contrib-python
sudo cp /usr/local/lib/python3.6/dist-packages/cv2/python-3.6/cv2.cpython-36m-x86_64-linux-gnu.so ~/.local/lib/python3.6/site-packages/cv2/
```

### 安装Windows X-server图形界面

如果WSL2没有Windows X-server，要先在Windows上安装VcXsrv，并配置打开；

### 测试

```
cd ~/opencv/samples/cpp/example_cmake
cmake .
make -j8
./opencv_example
```

### 查看版本

```
import cv2
print(cv2.__version__)
```

### 打开图片

```
import cv2
img = cv2.imread('/home/<user>/opencv/samples/data/lena.jpg')
cv2.imshow('lena.jpg', img)
cv2.waitKey()
cv2.destroyAllWindows()
```

### 使用Matplotlib展示图片

```
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('/home/<user>/opencv/samples/data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
plt.axis(False)
plt.imshow(img)
plt.show()
```

### 配置PyCharm

1. 运行配置添加环境变量 `DISPLAY=windows:0`（windows为WSL2的Win端IP），或者在代码开始处添加以下代码段：

```
import os
os.environ['DISPLAY'] = 'windows:0'
```

2. 下载安装插件（https://plugins.jetbrains.com/plugin/14371-opencv-image-viewer），debug时可以在Debugger窗口预览图片（右键 `View as Image`）;