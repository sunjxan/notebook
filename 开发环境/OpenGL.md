## 安装

### GLAD

https://glad.dav1d.de/ 在线配置：C/C++，OpenGL，Version 3.3及以上版本，Core，Generate a loader，点击GENERATE按钮，生成文件，复制 `glad.zip` 压缩包的链接地址，下载并解压：

```
cd ~
wget https://glad.dav1d.de/generated/tmpqhXA3_glad/glad.zip
unzip glad.zip -d glad
sudo mv glad/include/* /usr/local/include
```

### GLFW

下载GLFW并解压：

```bash
# 下载地址
# https://github.com/glfw/glfw/releases
cd ~
wget -O glfw.zip https://github.com/glfw/glfw/archive/3.3.2.zip
unzip glfw.zip
mv glfw-3.3.2 glfw
```


运行CMake：

```
cd glfw
mkdir build
cd build
cmake ..
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

如果WSL2没有Windows X-server，要先在Windows上安装VcXsrv，并配置以 `Fullscreen` 模式打开，否则会报错 `Error: GLX: Failed to create context: GLXBadFBConfig` 。

先修改环境变量为 `Fullscreen` 模式的 `Display number` ：

```
export DISPLAY=windows:1
```

然后进行测试：

```
./examples/simple
```
## C++编程

### 配置CLion

1. 修改CMakeLists.txt：
```
cmake_minimum_required(VERSION 3.10)
project(untitled)

set(CMAKE_CXX_STANDARD 14)

add_executable(untitled main.cpp ~/glad/src/glad.c)

target_link_libraries(untitled glfw3 GL m Xrandr Xi X11 pthread dl Xinerama Xcursor)
```

2. 在运行配置添加环境变量 `DISPLAY=windows:1`（windows为WSL2的Win端IP，1为 `Fullscreen` 模式的 `Display number` ），或者在main函数中添加环境变量：
```
#include <iostream>
#include "glad/glad.h"
#include "GLFW/glfw3.h"

using namespace std;

// 设置窗口大小
const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HEIGHT = 600;

// 窗口大小调整回调函数
void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
}

// 输入回调函数
void processInput(GLFWwindow *window) {
    if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}

int main() {
    // 设置Windows X-server
    putenv((char *)"DISPLAY=windows:1");

    // 初始化和配置GLFW
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // 创建窗口对象
    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGL", NULL, NULL);
    if (window == NULL) {
        cout << "Failed to create GLFW window" << endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    // 初始化GLAD
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        cout << "Failed to initialize GLAD" << endl;
        return -1;
    }

    // 设置视口
    glViewport(0, 0, SCR_WIDTH, SCR_HEIGHT);

    // 注册窗口大小调整回调函数
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    // 渲染循环
    while(!glfwWindowShouldClose(window)) {
        // 输入控制
        processInput(window);

        // 设置清空屏幕所用的颜色
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        // 清空屏幕的颜色缓冲
        glClear(GL_COLOR_BUFFER_BIT);

        // 检查并调用事件，交换缓冲
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // 渲染循环结束，释放资源
    glfwTerminate();

    return 0;
}
```

