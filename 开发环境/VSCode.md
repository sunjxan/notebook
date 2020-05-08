1. 安装VS Code；
2. 安装插件“Remote - WSL”；
3. 点击最左下角图标，选择安装的Linux发行版；
4. 通过"/mnt/"打开Windows文件系统下的目录；
5. 安装（Install on WSL）插件“Python”，“Go”；
6. 使用Jupyter notebook：Ctrl+Shift+P输入 Create Jupyter，然后创建即可；
7. 修改launch.json文件
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Node",
            "type": "node",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "skipFiles": [
                "<node_internals>/**"
            ]
        },
        {
            "name": "Go",
            "type": "go",
            "request": "launch",
            "program": "${file}"
        }
    ]
}
```