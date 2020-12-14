## 安装

### pip安装

```
pip3 install open3d
```

### 编译安装

克隆Open3D及其子模块：

```bash
cd ~
git clone --recursive https://github.com/intel-isl/Open3D
```

安装依赖项，修改 `Open3D/util/install_deps_ubuntu.sh` ，在 `$SUDO apt-get install "$APT_CONFIRM" "$package"` 后加上 `-y` 后执行：

```
sudo bash Open3D/util/install_deps_ubuntu.sh
```

下载安装新版CMake：

```
# 下载地址
# https://github.com/Kitware/CMake/releases
cd ~
wget -O cmake.sh https://github.com/Kitware/CMake/releases/download/v3.19.1/cmake-3.19.1-Linux-x86_64.sh
bash cmake.sh
# 安装到 ~/cmake-3.19.1-Linux-x86_64
mv cmake-3.19.1-Linux-x86_64 cmake
```

运行CMake：

```bash
# -D PYTHON_EXECUTABLE 你的目标python环境

cd Open3D
mkdir build
cd build
~/cmake/bin/cmake -D PYTHON_EXECUTABLE=/usr/bin/python3 ..
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
```

安装python库：

```bash
make -j $(nproc) pip-package
pip3 install lib/python_package/pip_package/open3d-0.11.2+bcb66865-cp38-cp38-linux_x86_64.whl
```

## Python编程

### 查看版本

```
import open3d as o3d
print(o3d.__version__)
```

### 配置PyCharm

1. 在运行配置添加环境变量 `DISPLAY=windows:1`（windows为WSL2的Win端IP），或者在代码开始处添加以下代码段：

```
import os
os.environ['DISPLAY'] = 'windows:1'
```

2. 展示pcd文件：

```
import open3d as o3d

pcd = o3d.io.read_point_cloud("/home/<user>/Open3D/examples/test_data/ICP/cloud_bin_0.pcd")
if len(pcd.points):
    print(len(pcd.points))
    pcd.normalize_normals()
    o3d.visualization.draw_geometries([pcd])
```

## C++编程

### 配置CLion

1. 修改CMakeLists.txt：

```
cmake_minimum_required(VERSION 3.10)
project(untitled)

set(CMAKE_CXX_STANDARD 14)

find_package(Open3D REQUIRED)

add_executable(untitled main.cpp)

target_link_libraries(untitled Open3D::Open3D)
```

2. 在运行配置添加环境变量 `DISPLAY=windows:0`（windows为WSL2的Win端IP），或者在main函数中添加环境变量：

```
#include <iostream>
#include "open3d/Open3D.h"

using namespace std;

int main() {
    // 设置Windows X-server
    putenv((char *)"DISPLAY=windows:1");
    
    auto pcd_ptr = std::make_shared<open3d::geometry::PointCloud>();
    if (open3d::io::ReadPointCloud("/home/<user>/Open3D/examples/test_data/ICP/cloud_bin_0.pcd", *pcd_ptr)) {
        cout << pcd_ptr->points_.size() << endl;
        pcd_ptr->NormalizeNormals();
        open3d::visualization::DrawGeometries({pcd_ptr});
    }
    
    return 0;
}
```