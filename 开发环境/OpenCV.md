## 安装

### pip安装

这种安装方式在Python IDE上有代码提示功能

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
# 下载地址
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

CMake过程中下载GitHub上的文件失败的问题

https://raw.githubusercontent/ 域名下文件无法下载，要从 https://github.com/googlehosts/hosts/blob/master/hosts-files/hosts 中复制解析规则到hosts文件中。


运行CMake：

```bash
# -D OPENCV_ENABLE_NONFREE=ON 此标志可确保您可以访问SIFT / SURF和其他获得专利的算法
# -D OPENCV_EXTRA_MODULES_PATH 不要写错opencv-contrib文件夹了
# -D PYTHON_EXECUTABLE 你的目标python环境

cd opencv
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
make -j $(nproc)
```

安装：

```bash
sudo make -j $(nproc) install
sudo ldconfig
```

最终得到动态链接库 `cv2.so` 文件，可以再使用pip安装一次，然后使用编译获得的 `cv2.so` 文件进行替换，以获得Python IDE的代码提示功能：

```
pip3 install opencv-contrib-python

rm ~/.local/lib/python3.6/site-packages/cv2/*.so

ln -s /usr/local/lib/python3.6/dist-packages/cv2/python-3.6/*.so ~/.local/lib/python3.6/site-packages/cv2/cv2.so
```

## 测试

```
cd ~/opencv/samples/cpp/example_cmake
cmake .
make -j $(nproc)
./opencv_example
```

## Python编程

### 查看版本

```
import cv2
print(cv2.__version__)
```

### PIL Image打开图片

```
from PIL import Image
import numpy as np

# 读取图片
imageObj = Image.open('opencv/samples/data/lena.jpg')
# 转换为numpy数组
image = np.array(imageObj)
```

### OpenCV打开图片

```
import cv2

# 读取图片
image = cv2.imread('opencv/samples/data/lena.jpg')

# 如果不存在该名字的窗口，则创建图形窗口，设置窗口名
# 之后如果有不同名的窗口被创建，则展示该未渲染图片的窗口
cv2.namedWindow('Image')

# 设置窗口标题
cv2.setWindowTitle('Image', 'lena.jpg')

# 设置窗口位置和大小
cv2.moveWindow('Image', 10, 20)
cv2.resizeWindow('Image', 100, 100)

# 如果不存在该名字的窗口，则创建图形窗口，设置窗口名，添加图片，否则为该窗口添加图片
# 之后如果有不同名的窗口被创建，则展示该未渲染图片的窗口
cv2.imshow('Image', image)

# 更新窗口，为所有展示的窗口渲染图片
# 传参delay（必须为整数），正整数为等待时间毫秒数，非正整数或不传表示等待时间无限长
# 在任一窗口激活状态下，键盘输入停止等待，返回值为1字节key code，手动关闭或等待时间结束，返回值为-1
cv2.waitKey()
# 键盘输入返回值为2字节key code，keycode & 0xff 转换为1字节key code
cv2.waitKeyEx()

# 关闭单个窗口
cv2.destroyWindow('Image')
# 关闭所有窗口
cv2.destroyAllWindows()
```

### Matplotlib打开图片

```
import matplotlib.pyplot as plt

# 使用GTK图形库，展示figure
plt.switch_backend('GTK3Agg')
# 使用网页，展示figure内图片
plt.switch_backend('WebAgg')

# 读取图片
image = plt.imread('opencv/samples/data/lena.jpg')

# 创建figure，设置figure名
# 图形库程序默认会以从1递增的数字为编号创建figure
# 网页端只会默认创建一个编号为1的figure
figure = plt.figure('Image')
# 为当前figure添加图片
plt.imshow(image)
# 为当前figure添加标题
plt.title('lena.jpg')

# 仅适用于图形库展示：
# 展示figure
figure.show()

# 仅适用于图形库展示：
# 先展示当前figure，然后为所有展示的figure渲染图片
# 传参timeout，正数为等待时间秒数，非正数或不传表示等待时间无限长
# 只有在当前窗口激活状态下，键盘输入或鼠标点击停止等待，返回值分别为True和False，等待时间结束，返回值为None
plt.waitforbuttonpress()

# 将所有未被手动关闭的figure，先展示再渲染图片
# 始终等待，直到手动关闭所有figure
plt.show()

# 删除当前figure内图片
plt.close()
# 删除命名figure内图片
plt.close('Image')
# 删除编号figure内图片
plt.close(1)
# 删除所有figure内图片
plt.close('all')
# 手动关闭也会删除figure内图片
```

### Matplotlib用于调试

```
# 右下角显示鼠标处坐标和数值
# 移动按钮，按鼠标左键拖拽移动坐标轴位置，按鼠标右键拖拽以图片为中心放缩坐标轴
# 放缩按钮，按鼠标左键选中矩形区域放大，按鼠标右键选中矩形区域缩小
# 快捷键 q:退出 h/r/Home:还原 c/Left/Backspace:撤销 v/Right:重做 g:显示/隐藏辅助线 p:移动按钮 o:放缩按钮 s:保存 

import matplotlib.pyplot as plt
plt.switch_backend('GTK3Agg')

# 展示彩色图片
plt.imshow(image[..., (2,1,0)])
plt.show()

# 展示灰度图片
plt.imshow(image[..., 2], cmap='gray')
plt.show()

# 一次展示多张照片
plt.subplot(2, 2, 1)
plt.imshow(image[..., (2, 1, 0)])
plt.title('Image')
plt.subplot(2, 2, 2)
plt.imshow(image[..., 2], cmap='gray')
plt.title('Red')
plt.subplot(2, 2, 3)
plt.imshow(image[..., 1], cmap='gray')
plt.title('Green')
plt.subplot(2, 2, 4)
plt.imshow(image[..., 0], cmap='gray')
plt.title('Blue')
plt.show()
```

## C++编程

CMakeLists.txt

```
cmake_minimum_required(VERSION 3.10)
project(untitled LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)

message(STATUS "OpenCV_VERSION:${OpenCV_VERSION}")
message(STATUS "OpenCV_DIR:${OpenCV_DIR}")
message(STATUS "OpenCV_INSTALL_PATH:${OpenCV_INSTALL_PATH}")
message(STATUS "OpenCV_INCLUDE_DIRS:${OpenCV_INCLUDE_DIRS}")
message(STATUS "OpenCV_LIB_DIR:${OpenCV_INSTALL_PATH}/lib")
message(STATUS "OpenCV_LIBS:${OpenCV_LIBS}")

include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(untitled main.cpp)

link_directories(${OpenCV_LIB_DIR})
target_link_libraries(untitled ${OpenCV_LIBS})
```

test.cpp

```
#include <opencv2/opencv.hpp>
using namespace std;
int main()
{
    cv::Mat image = cv::imread("opencv/samples/data/lena.jpg");
    cv::imshow("Image", image);
    cv::waitKey();
    cv::destroyAllWindows();    
    return 0;
}
```

## 插件

### GDB ImageWatch / Open Image Debugger

```
git clone git@github.com:OpenImageDebugger/OpenImageDebugger.git

cd OpenImageDebugger
git submodule init
git submodule update

mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j $(nproc)
sudo make -j $(nproc) install

vim ~/.gdbinit
# 追加以下
source /usr/local/OpenImageDebugger/oid.py
```

### OpenCV Image Viewer (PyCharm / CLion)

下载安装插件（https://plugins.jetbrains.com/plugin/14371-opencv-image-viewer），debug时可以在Debugger窗口预览图片（右键 `View as Image`）。
