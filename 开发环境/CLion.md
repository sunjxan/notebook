1. 安装CLion专业版；
2. 打开Windows文件系统下的项目目录；
3. File->Settings->Editor->Font，设置字体为Consolas,14号，File->Editor->File Encodings，设置所有编码为UTF-8，勾选上Transparent native-to-ascii conversion。Keymap设置为Sublime text快捷键。Appearance & Behavior->System Settings->Updates，关闭自动检查更新；
4. File->Settings->Tools->Terminal，修改Shell path为wsl.exe；
5. WSL安装编译工具：

```
sudo apt install cmake make gcc g++ gdb
```

6. 配置WSL编译环境：File->Settings->Build, Execution, Deployment->Toolchains，添加WSL环境，登录SSH账号，自动检测编译工具路径，确定；

7. 新建或打开一个项目，Run->Edit Configurations，新建一个CMake Application运行配置，修改名字，选择项目目录；

8. 修改CMakeLists.txt：

```
# CMake最低版本号要求
cmake_minimum_required(VERSION 3.10)
# 项目名称
project(<project>)
# 使用C++ 14标准
set(CMAKE_CXX_STANDARD 14)

# 查找指定库文件
find_package(<package> REQUIRED)
# 设置包含的目录
include_directories(build/include)

# 指定生成目标
add_executable(<project> main.cpp)

# 设置链接库搜索目录
link_directories(build/lib)
# 设置 TARGET 需要链接的库
target_link_libraries(<project> <libs>)
```

编译目标文件：`cmake-build-debug/<project>`