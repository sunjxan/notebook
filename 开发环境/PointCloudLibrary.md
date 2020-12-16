## 安装

### apt安装

```
sudo apt install libpcl-dev
```

### 编译安装

安装依赖项：

```
sudo apt install doxygen mpi-default-dev openmpi-bin openmpi-common
sudo apt install libusb-1.0-0-dev libqhull* libusb-dev libgtest-dev libudev-dev
sudo apt install mpi-default-dev openmpi-bin openmpi-common
sudo apt install libeigen3-dev
sudo apt install libflann1.9 libflann-dev
sudo apt install libboost-all-dev
sudo apt install freeglut3-dev pkg-config
sudo apt install libxmu-dev libxi-dev
sudo apt install libphonon-dev libphonon-dev phonon-backend-gstreamer
sudo apt install phonon-backend-vlc graphviz mono-complete
sudo apt install qt5-default
```

下载VTK并解压安装：

```
# 下载地址
# https://github.com/Kitware/VTK/releases
cd ~
wget -o VTK.zip https://github.com/Kitware/VTK/archive/v9.0.0.zip
unzip VTK.zip
mv VTK-9.0.0 VTK
cd VTK && mkdir build && cd build
cmake ..
make                                                                   
sudo make install
```

下载PCL并解压：

```
# 下载地址
# https://github.com/PointCloudLibrary/pcl/releases
cd ~
wget -O pcl.zip https://github.com/PointCloudLibrary/pcl/archive/pcl-1.11.1.zip
unzip pcl.zip
mv pcl-pcl-1.11.1 pcl
```

运行CMake：

```bash
cd pcl
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=RELEASE -DBUILD_GPU=ON -DBUILD_apps=ON -DBUILD_examples=ON ..
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

## 测试

如果WSL2没有Windows X-server，要先在Windows上安装VcXsrv，并配置添加环境变量 `DISPLAY=windows:1`（windows为WSL2的Win端IP）。然后进行测试：

```bash
pcl_viewer ../test/pcl_logo.pcd
```

## C++编程

### 配置CLion

1. 修改CMakeLists.txt：

```
cmake_minimum_required(VERSION 3.10)
project(untitled)

set(CMAKE_CXX_STANDARD 14)

find_package(PCL REQUIRED)

message(STATUS "PCL_VERSION:${PCL_VERSION}")
message(STATUS "PCL_DIR:${PCL_DIR}")
message(STATUS "PCL_INCLUDE_DIRS:${PCL_INCLUDE_DIRS}")
message(STATUS "PCL_LIB_DIR:${PCL_LIBRARY_DIRS}")
message(STATUS "PCL_LIBS:${PCL_LIBRARIES}")

include_directories(${PCL_INCLUDE_DIRS})

add_definitions(${PCL_DEFINITIONS})

add_executable(untitled main.cpp)

link_directories(${PCL_LIBRARY_DIRS})
target_link_libraries (untitled ${PCL_LIBRARIES})
```

2. 在运行配置添加环境变量 `DISPLAY=windows:1`（windows为WSL2的Win端IP），或者在main函数中添加环境变量：

```
#include <iostream>
#include "pcl/common/common_headers.h"
#include "pcl/io/pcd_io.h"
#include "pcl/visualization/pcl_visualizer.h"
#include "pcl/visualization/cloud_viewer.h"
#include "pcl/console/parse.h"

using namespace std;

int main() {
    // 设置Windows X-server
    putenv((char *)"DISPLAY=windows:1");

    pcl::PointCloud<pcl::PointXYZRGB>::Ptr point_cloud_ptr (new pcl::PointCloud<pcl::PointXYZRGB>);
    uint8_t r(255), g(15), b(15);
    for (float z(-1.0); z <= 1.0; z += 0.05) {
        for (float angle(0.0); angle <= 360.0; angle += 5.0) {
            pcl::PointXYZRGB point;
            point.x = 0.5 * cosf (pcl::deg2rad(angle));
            point.y = sinf (pcl::deg2rad(angle));
            point.z = z;
            uint32_t rgb = (static_cast<uint32_t>(r) << 16 |
                static_cast<uint32_t>(g) << 8 | static_cast<uint32_t>(b));
            point.rgb = *reinterpret_cast<float*>(&rgb);
            point_cloud_ptr->points.push_back (point);
        }
        if (z < 0.0) {
            r -= 12;
            g += 12;
        } else {
            g -= 12;
            b += 12;
        }
    }
    point_cloud_ptr->width = (int) point_cloud_ptr->points.size ();
    point_cloud_ptr->height = 1;

    pcl::visualization::CloudViewer viewer ("test");
    viewer.showCloud(point_cloud_ptr);
    while (!viewer.wasStopped()) {
    }

    return 0;
}
```